"""FedAvg scheduler."""

import io
import json
import os
import shutil
import sys
import traceback
from abc import ABCMeta, abstractmethod
from typing import Any, Dict, List, Tuple, final
from zipfile import ZipFile

import torch
from torch.nn import Module
from torch.optim import Optimizer
from torch.utils.data import DataLoader
from torch.utils.tensorboard import SummaryWriter

from .. import get_result_dir, get_runtime_dir, logger
from ..data_channel import SharedFileDataChannel
from ..scheduler import ConfigError, Scheduler, TaskComplete, TaskFailed
from .contractor import (CheckinEvent, CheckinResponseEvent, CloseRoundEvent,
                         DistributeParametersEvent, FedAvgContractor,
                         FinishTaskEvent, ReadyForAggregationEvent,
                         ResetRoundEvent, StartRoundEvent, SyncStateEvent,
                         SyncStateResponseEvent, UploadTrainingResultsEvent)

__all__ = [
    'FedAvgScheduler',
    'FedSGDScheduler'
]


class AggregationError(Exception):
    ...


class SkipRound(Exception):
    ...


class ResetRound(Exception):
    ...


class FedAvgScheduler(Scheduler, metaclass=ABCMeta):
    """Implementation of FedAvg."""

    _INIT = 'init'
    _GETHORING = 'gethering'
    _READY = 'ready'
    _SYNCHRONIZING = 'synchronizing'
    _IN_A_ROUND = 'in_a_round'
    _UPDATING = 'updating'
    _CALCULATING = 'calculating'
    _WAIT_FOR_AGGR = 'wait_4_aggr'
    _AGGREGATING = 'aggregating'
    _PERSISTING = 'persisting'
    _CLOSING_ROUND = 'closing_round'
    _FINISHING = 'finishing'

    def __init__(self,
                 max_rounds: int = 0,
                 merge_epochs: int = 1,
                 calculation_timeout: int = 300,
                 schedule_timeout: int = 30,
                 log_rounds: int = 0,
                 involve_aggregator: bool = False):
        """Init.

        Args:
            max_rounds:
                Maximal number of training rounds.
            merge_epochs:
                The number of epochs to run before aggregation is performed.
            calculation_timeout:
                Seconds to timeout for calculation in a round. Takeing off timeout
                by setting its value to 0.
            schedule_timeout:
                Seconds to timeout for process scheduling. Takeing off timeout
                by setting its value to 0.
            log_rounds:
                The number of rounds to run testing and log the result. Skip it
                by setting its value to 0.
            involve_aggregator:
                If set true, the aggregator should have its local data and conduct
                training other than merely schedule and aggregate.
        """
        super().__init__()
        self._switch_status(self._INIT)

        self.max_rounds = max_rounds
        self.merge_epochs = merge_epochs
        self.calculation_timeout = calculation_timeout
        self.schedule_timeout = schedule_timeout
        self.log_rounds = log_rounds
        self.involve_aggregator = involve_aggregator

        self._validate_config()
        self.current_round = 1

        self.participants: List[str] = []
        self.gethered: List[str] = []
        self.is_gathering_complete = False

    def _validate_config(self):
        if self.merge_epochs <= 0:
            raise ConfigError('merge_epochs must be a positive integer')

    @abstractmethod
    def build_model(self) -> Module:
        """Return a model object which will be used for training."""

    @final
    @property
    def model(self) -> Module:
        """Get the model object which is used for training."""
        if not hasattr(self, '_model'):
            self._model = self.build_model()
        return self._model

    @abstractmethod
    def build_optimizer(self, model: Module) -> Optimizer:
        """Return a optimizer object which will be used for training.

        Args:
            model:
                The model object which is used for training.
        """

    @final
    @property
    def optimizer(self) -> Optimizer:
        """Get the optimizer object which is used for training."""
        if not hasattr(self, '_optimizer'):
            self._optimizer = self.build_optimizer(model=self.model)
        return self._optimizer

    @abstractmethod
    def build_train_dataloader(self) -> DataLoader:
        """Define the training dataloader.

        You can transform the dataset, do some preprocess to the dataset.

        Return:
            training dataloader
        """

    @final
    @property
    def train_loader(self) -> DataLoader:
        """Get the training dataloader object."""
        if not hasattr(self, '_train_loader'):
            self._train_loader = self.build_train_dataloader()
        return self._train_loader

    def build_validation_dataloader(self) -> DataLoader:
        """Define the validation dataloader if needed.

        You can transform the dataset, do some preprocess to the dataset.

        Return:
            validation dataloader
        """
        raise NotImplementedError()

    @final
    @property
    def validation_loader(self) -> DataLoader:
        """Get the validation dataloader object if needed."""
        if not hasattr(self, '_validation_loader'):
            self._validation_loader = self.build_validation_dataloader()
        return self._validation_loader

    @abstractmethod
    def build_test_dataloader(self) -> DataLoader:
        """Define the testing dataloader.

        You can transform the dataset, do some preprocess to the dataset. If you do not
        want to do testing after training, simply make it return None.

        Args:
            dataset:
                training dataset
        Return:
            testing dataloader
        """

    @final
    @property
    def test_loader(self) -> DataLoader:
        """Get the testing dataloader object."""
        if not hasattr(self, '_test_loader'):
            self._test_loader = self.build_test_dataloader()
        return self._test_loader

    def state_dict(self) -> Dict[str, torch.Tensor]:
        """Get the params that need to train and update.

        Only the params returned by this function will be updated and saved during aggregation.
        Return self.model.state_dict() by default.

        Return:
            List[torch.Tensor], The list of model params.
        """
        return self.model.state_dict()

    def load_state_dict(self, state_dict: Dict[str, torch.Tensor]):
        """Load the params that trained and updated.

        Only the params returned by state_dict() should be loaded by this function.
        Execute self.model.load_state_dict(state_dict) by default.
        """
        self.model.load_state_dict(state_dict)

    def validate_context(self):
        """Validate if the local running context is ready.

        For example: check if train and test dataset could be loaded successfully.
        """
        if self.model is None:
            raise ConfigError('Must specify a model to train')
        if not isinstance(self.model, Module):
            raise ConfigError('Support torch.Module only')
        if self.optimizer is None:
            raise ConfigError('Must specify an optimizer to train')
        if not isinstance(self.optimizer, Optimizer):
            raise ConfigError('Support torch.optim.Optimizer only')

    @abstractmethod
    def train_an_epoch(self) -> Any:
        """Define the training steps in an epoch."""

    @abstractmethod
    def run_test(self) -> Any:
        """Define the testing steps.

        If you do not want to do testing after training, simply make it pass.
        """

    def is_task_finished(self) -> bool:
        """By default true if reach the max rounds configured."""
        return self._is_reach_max_rounds()

    def _run(self, id: str, task_id: str, is_initiator: bool = False, recover: bool = False):
        self._setup_context(id=id, task_id=task_id, is_initiator=is_initiator)
        self.push_log(message='Local context is ready.')
        try:
            if self.is_aggregator and recover:
                self._recover_progress()
            else:
                self._clean_progress()
            self._launch_process()
        except Exception:
            err_stack = '\n'.join(traceback.format_exception(*sys.exc_info()))
            self.push_log(err_stack)

    def _setup_context(self, id: str, task_id: str, is_initiator: bool = False):
        assert id, 'must specify a unique id for every participant'
        assert task_id, 'must specify a task_id for every participant'

        self.id = id
        self.task_id = task_id
        self._runtime_dir = get_runtime_dir(self.task_id)
        self._context_file = os.path.join(self._runtime_dir, ".context.json")
        self._checkpoint_dir = os.path.join(self._runtime_dir, 'checkpoint')
        self._ckpt_file = os.path.join(self._checkpoint_dir, "model_ckpt.pt")
        self._result_dir = get_result_dir(self.task_id)
        self._log_dir = os.path.join(self._result_dir, 'tb_logs')
        self.tb_writer = SummaryWriter(log_dir=self._log_dir)

        self.is_initiator = is_initiator
        self.is_aggregator = self.is_initiator

        self.contractor = self._init_contractor()
        self.data_channel = SharedFileDataChannel(self.contractor)
        self.model
        self.optimizer

        self.participants = self.contractor.query_nodes()
        if len(self.participants) < 2:
            raise TaskFailed('Failed to get participants list.')

        self.push_log(message='Begin to validate local context.')
        self.validate_context()

    def _init_contractor(self):
        return FedAvgContractor(task_id=self.task_id)

    def _recover_progress(self):
        """Try to recover and continue from last running."""
        if not os.path.isfile(self._context_file):
            raise TaskFailed('Failed to recover progress: missing cached context.')

        with open(self._context_file, 'r') as f:
            context_info: dict = json.load(f)
        round = context_info.get('round')
        ckpt_file = context_info.get('ckpt_file')
        assert round and isinstance(round, int) and round > 0, f'Invalid round: {round} .'
        assert ckpt_file and isinstance(ckpt_file, str), f'Invalid ckpt_file: {ckpt_file} .'
        if not os.path.isfile(ckpt_file):
            raise TaskFailed('Failed to recover progress: missing checkpoint parameters.')

        self.current_round = round
        with open(ckpt_file, 'rb') as f:
            state_dict = torch.load(f)
            self.load_state_dict(state_dict)

    def _clean_progress(self):
        """Clean existing progress data."""
        shutil.rmtree(self._runtime_dir, ignore_errors=True)
        shutil.rmtree(self._result_dir, ignore_errors=True)
        os.makedirs(self._runtime_dir, exist_ok=True)
        os.makedirs(self._checkpoint_dir, exist_ok=True)
        os.makedirs(self._result_dir, exist_ok=True)
        os.makedirs(self._log_dir, exist_ok=True)

    def push_log(self, message: str):
        """Push a running log message to the task manager."""
        super().push_log(message=message)
        logger.info(message)

    def _launch_process(self):
        try:
            assert self.status == self._INIT, 'must begin from initial status'
            self.push_log(f'Node {self.id} is up.')

            self._switch_status(self._GETHORING)
            self._check_in()

            self._switch_status(self._READY)
            while self.status == self._READY:
                try:
                    self._switch_status(self._SYNCHRONIZING)
                    self._sync_state()

                    self._switch_status(self._IN_A_ROUND)
                    self._run_a_round()
                    self._switch_status(self._READY)
                except ResetRound:
                    self.push_log('WARNING: Reset runtime context, there might be an error raised.')
                    self._switch_status(self._READY)
                    continue

                if self.is_aggregator:
                    is_finished = self.is_task_finished()
                    self._persistent_running_context()
                    self._switch_status(self._READY)
                    self.current_round += 1
                    if is_finished:
                        self.push_log(f'Obtained the final results of task {self.task_id}')
                        self._switch_status(self._FINISHING)
                        self._close_task()

        except TaskComplete:
            logger.info('training task complete')

    def _check_in(self):
        """Check in task and get ready.

        As an initiator (and default the first aggregator), records each participants
        and launches election or training process accordingly.
        As a participant, checkins and gets ready for election or training.
        """
        if self.is_initiator:
            self.push_log('Waiting for participants taking part in ...')
            self._wait_for_gathering()
            self.is_gathering_complete = True
        else:
            is_checked_in = False
            # the aggregator may be in special state so can not response
            # correctly nor in time, then retry periodically
            self.push_log('Checking in the task ...')
            while not is_checked_in:
                is_checked_in = self._check_in_task()
            self.push_log(f'Node {self.id} have taken part in the task.')

    def _sync_state(self):
        """Synchronize state before each round, so it's easier to manage the process.

        As an aggregator, iterates round, broadcasts and resets context of the new round.
        As a participant, synchronizes state and gives a response.
        """
        self.push_log('Synchronizing round state ...')
        if self.is_aggregator:
            self.push_log(f'Initiate state synchronization of round {self.current_round}.')
            self.contractor.sync_state(round=self.current_round, aggregator=self.id)
            self._wait_for_sync_response()
        else:
            self._wait_for_sync_state()
        self.push_log(f'Successfully synchronized state in round {self.current_round}')

    def _run_a_round(self):
        """Perform a round of FedAvg calculation.

        As an aggregator, selects a part of participants as actual calculators
        in the round, distributes latest parameters to them, collects update and
        makes aggregation.
        As a participant, if is selected as a calculator, calculates and uploads
        parameter update.
        """
        if self.is_aggregator:
            try:
                self._run_as_aggregator()
            except AggregationError as err:
                err_stack = '\n'.join(traceback.format_exception(*sys.exc_info()))
                self.push_log(err_stack)
                self.contractor.reset_round()
                raise ResetRound(err)
        else:
            self._run_as_data_owner()

    def _close_task(self, is_succ: bool = True):
        """Close the FedAvg calculation.

        As an aggregator, broadcasts the finish task event to all participants,
        uploads the final parameters and tells L1 task manager the task is complete.
        As a participant, do nothing.
        """
        self.push_log(f'Closing task {self.task_id} ...')
        if is_succ and self.is_aggregator:
            self._switch_status(self._FINISHING)
            self.contractor.finish_task()
            report_file_path, model_file_path = self._prepare_task_output()
            self.contractor.upload_task_achivement(aggregator=self.contractor.EVERYONE[0],
                                                   report_file=report_file_path,
                                                   model_file=model_file_path)
            self.contractor.notify_task_completion(result=True)
        elif self.is_aggregator:
            self.contractor.finish_task()
            self.contractor.notify_task_completion(result=False)
        self.push_log(f'Task {self.task_id} closed. Byebye!')

    def _wait_for_gathering(self):
        """Wait for participants gethering."""
        logger.debug('_wait_for_gathering ...')
        for _event in self.contractor.contract_events():
            if isinstance(_event, CheckinEvent):
                self._handle_check_in(_event)
                if len(self.gethered) == len(self.participants) - 1:
                    return

    def _handle_check_in(self, _event: CheckinEvent):
        if _event.peer_id not in self.gethered:
            self.gethered.append(_event.peer_id)
            self.push_log(f'Welcome a new participant ID: {_event.peer_id}.')
            self.push_log(f'There are {len(self.gethered) + 1} participants now.')
        self.contractor.respond_check_in(round=self.current_round,
                                         aggregator=self.id,
                                         nonce=_event.nonce,
                                         requester_id=_event.peer_id)
        if self.is_gathering_complete:
            self.contractor.sync_state(round=self.current_round, aggregator=self.id)

    def _wait_for_sync_response(self):
        """Wait for participants' synchronizing state response."""
        self.push_log('Waiting for synchronization responses ...')
        synced = set()
        for _event in self.contractor.contract_events(timeout=0):
            if isinstance(_event, SyncStateResponseEvent):
                if _event.round != self.current_round:
                    continue
                synced.add(_event.peer_id)
                self.push_log(f'Successfully synchronized state with ID: {_event.peer_id}.')
                self.push_log(f'Successfully synchronized with {len(synced)} participants.')
                if len(synced) == len(self.gethered):
                    return

            elif isinstance(_event, CheckinEvent):
                self._handle_check_in(_event)

    def _check_in_task(self) -> bool:
        """Try to check in the task."""
        nonce = self.contractor.checkin(peer_id=self.id)
        return self._wait_for_check_in_response(nonce=nonce,
                                                timeout=self.schedule_timeout)

    def _wait_for_check_in_response(self, nonce: str, timeout: int = 0) -> bool:
        """Wait for checkin response.

        Return True if received response successfully otherwise False.
        """
        logger.debug('_wait_for_check_in_response ...')
        for _event in self.contractor.contract_events(timeout=timeout):
            if isinstance(_event, CheckinResponseEvent):
                if _event.nonce != nonce:
                    continue
                self.current_round = _event.round
                return True
            elif isinstance(_event, FinishTaskEvent):
                raise TaskComplete()
        return False

    def _wait_for_sync_state(self, timeout: int = 0) -> bool:
        """Wait for synchronising latest task state.

        Return True if synchronising successfully otherwise False.
        """
        self.push_log('Waiting for synchronizing state with the aggregator ...')
        for _event in self.contractor.contract_events(timeout=timeout):
            if isinstance(_event, SyncStateEvent):
                self.current_round = _event.round
                self.contractor.respond_sync_state(round=self.current_round,
                                                   peer_id=self.id,
                                                   aggregator=_event.aggregator)
                self.push_log('Successfully synchronized state with the aggregator.')
                return
            elif isinstance(_event, FinishTaskEvent):
                raise TaskComplete()

    def _run_as_aggregator(self):
        self._start_round()
        self._distribute_model()

        self._process_aggregation()

        self._check_and_run_test()
        self._close_round()

    def _close_round(self):
        """Close current round when finished."""
        self._switch_status(self._CLOSING_ROUND)
        self.contractor.close_round(round=self.current_round)
        self.push_log(f'The training of Round {self.current_round} complete.')

    def _start_round(self):
        """Prepare and start calculation of a round."""
        self.push_log(f'Begin the training of round {self.current_round}.')
        self.contractor.start_round(round=self.current_round,
                                    calculators=self.gethered,
                                    aggregator=self.id)
        self.push_log(f'Calculation of round {self.current_round} is started.')

    def _distribute_model(self):
        buffer = io.BytesIO()
        torch.save(self.state_dict(), buffer)
        self.push_log('Distributing parameters ...')
        results = {_target: False for _target in self.gethered}
        accept_list = self.data_channel.send_stream(source=self.id,
                                                    target=list(results.keys()),
                                                    data_stream=buffer.getvalue())
        self.push_log(f'Successfully distributed parameters to: {accept_list}')
        if len(results.keys()) != len(accept_list):
            reject_list = [_target for _target in results.keys()
                           if _target not in accept_list]
            self.push_log(f'Failed to distribute parameters to: {reject_list}')
        results.update({_target: True for _target in accept_list})

        if sum(results.values()) < len(self.gethered):
            self.push_log('Task failed because of too few calculators getting ready')
            raise AggregationError(f'Too few calculators getting ready: {results}.')
        self.push_log(f'Distributed parameters to {sum(results.values())} calculators.')

    def _process_aggregation(self):
        """Process aggregation depending on specific algorithm."""
        self._switch_status(self._WAIT_FOR_AGGR)
        self.contractor.notify_ready_for_aggregation(round=self.current_round)
        self.push_log('Now waiting for executing calculation ...')
        accum_result, result_count = self._wait_for_calculation()
        if result_count < len(self.gethered) + int(self.involve_aggregator):
            self.push_log('Task failed because of too few calculation results gathered.')
            raise AggregationError(f'Too few results gathered: {result_count} copies.')
        self.push_log(f'Received {result_count} copies of calculation results.')

        self._switch_status(self._AGGREGATING)
        self.push_log('Begin to aggregate and update parameters.')
        for _key in accum_result.keys():
            if accum_result[_key].dtype in (
                torch.uint8, torch.int8, torch.int16, torch.int32, torch.int64
            ):
                logger.warn(f'average a int value may lose precision: {_key=}')
                accum_result[_key].div_(result_count, rounding_mode='trunc')
            else:
                accum_result[_key].div_(result_count)
        self.load_state_dict(accum_result)
        self.push_log('Obtained a new version of parameters.')

    def _persistent_running_context(self):
        self._switch_status(self._PERSISTING)
        self._save_model()
        self._save_runtime_context()

    def _check_and_run_test(self):
        """Run test if match configured conditions."""
        if (
            self.current_round == 1
            or (self.log_rounds > 0 and self.current_round % self.log_rounds == 0)
            or self.current_round == self.max_rounds
        ):
            self.push_log('Begin to make a model test.')
            self.run_test()
            self.push_log('Finished a round of test.')

    def _wait_for_calculation(self) -> Tuple[Dict[str, torch.Tensor], int]:
        """Wait for every calculator finish its task or timeout."""
        result_count = 0
        if self.involve_aggregator:
            self._execute_training()
            result_count += 1
            self.push_log(f'The aggregator ID: {self.id} obtained its calculation results.')
            accum_result = self.state_dict()
        else:
            accum_result = self.state_dict()
            for _param in accum_result.values():
                if isinstance(_param, torch.Tensor):
                    _param.zero_()

        self.push_log('Waiting for training results ...')
        for _event in self.contractor.contract_events(timeout=self.calculation_timeout):
            if isinstance(_event, UploadTrainingResultsEvent):
                if self.id not in _event.target:
                    continue
                training_result = self.data_channel.receive_stream(apply_event=_event,
                                                                   receiver=self.id)
                buffer = io.BytesIO(training_result)
                _new_state_dict = torch.load(buffer)
                for _key in accum_result.keys():
                    accum_result[_key].add_(_new_state_dict[_key])
                result_count += 1
                self.push_log(f'Received calculation results from ID: {_event.source}')
                logger.info('======================================')
                logger.info(f'{result_count=}')
                logger.info(f'{len(self.gethered)=}')
                logger.info(f'{int(self.involve_aggregator)=}')
                logger.info(f'{(result_count == len(self.gethered) + int(self.involve_aggregator))=}')
                if result_count == len(self.gethered) + int(self.involve_aggregator):
                    return accum_result, result_count

        return accum_result, result_count

    def _is_reach_max_rounds(self) -> bool:
        """Is the max rounds configuration reached."""
        return self.current_round >= self.max_rounds

    def _save_model(self):
        """Save latest model state."""
        with open(self._ckpt_file, 'wb') as f:
            torch.save(self.state_dict(), f)
        self.push_log('Saved latest parameters locally.')

    def _save_runtime_context(self):
        """Save runtime context information in case of restoring."""
        context_info = {
            'round': self.current_round,
            'ckpt_file': self._ckpt_file
        }
        with open(self._context_file, 'w') as f:
            f.write(json.dumps(context_info, ensure_ascii=False))
        self.push_log('Saved latest runtime context.')

    def _prepare_task_output(self) -> Tuple[str, str]:
        """Generate final output files of the task.

        Return:
            Local paths of the report file and model file.
        """
        self.push_log('Uploading task achievement and closing task ...')

        report_file = os.path.join(self._result_dir, "report.zip")
        with ZipFile(report_file, 'w') as report_zip:
            for path, _, filenames in os.walk(self._log_dir):
                rel_dir = os.path.relpath(path=path, start=self._result_dir)
                rel_dir = rel_dir.lstrip('.')  # ./file => file
                for _file in filenames:
                    rel_path = os.path.join(rel_dir, _file)
                    report_zip.write(os.path.join(path, _file), rel_path)
        report_file_path = os.path.abspath(report_file)

        model_file = os.path.join(self._result_dir, "model.pt")
        with open(model_file, 'wb') as f:
            torch.save(self.state_dict(), f)
        model_file_path = os.path.abspath(model_file)

        self.push_log('Task achievement files are ready.')
        return report_file_path, model_file_path

    def _run_as_data_owner(self):
        try:
            self._wait_for_starting_round()
            self._switch_status(self._UPDATING)
            self._wait_for_updating_model()
            self._save_model()
            self._switch_status(self._CALCULATING)
            self.push_log('Begin to run calculation ...')
            self._execute_training()
            self.push_log('Local calculation complete.')

            self._wait_for_uploading_model()
            buffer = io.BytesIO()
            torch.save(self.state_dict(), buffer)
            self.push_log('Pushing local update to the aggregator ...')
            self.data_channel.send_stream(source=self.id,
                                          target=[self._aggregator],
                                          data_stream=buffer.getvalue())
            self.push_log('Successfully pushed local update to the aggregator.')
            self._switch_status(self._CLOSING_ROUND)
            self._wait_for_closing_round()
        except SkipRound:
            pass

        self.push_log(f'ID: {self.id} finished training task of round {self.current_round}.')

    def _execute_training(self):
        for _ in range(self.merge_epochs):
            self.train_an_epoch()

    def _wait_for_starting_round(self):
        """Wait for starting a new round of training."""
        self.push_log(f'Waiting for training of round {self.current_round} begin ...')
        for _event in self.contractor.contract_events():
            if isinstance(_event, StartRoundEvent):
                if _event.round != self.current_round:
                    continue
                if self.id not in _event.calculators:
                    raise SkipRound()
                self._aggregator = _event.aggregator
                self.push_log(f'Training of round {self.current_round} begins.')
                return
            elif isinstance(_event, FinishTaskEvent):
                raise TaskComplete()
            elif isinstance(_event, ResetRoundEvent):
                raise ResetRound()

    def _wait_for_updating_model(self):
        """Wait for receiving latest parameters from aggregator."""
        self.push_log('Waiting for receiving latest parameters from the aggregator ...')
        for _event in self.contractor.contract_events():
            if isinstance(_event, DistributeParametersEvent):
                if self.id not in _event.target:
                    continue
                parameters = self.data_channel.receive_stream(apply_event=_event,
                                                              receiver=self.id)
                buffer = io.BytesIO(parameters)
                new_state_dict = torch.load(buffer)
                self.load_state_dict(new_state_dict)
                self.push_log('Successfully received latest parameters.')
                return
            elif isinstance(_event, FinishTaskEvent):
                raise TaskComplete()
            elif isinstance(_event, ResetRoundEvent):
                raise ResetRound()

    def _wait_for_uploading_model(self):
        """Wait for uploading trained parameters to aggregator."""
        self.push_log('Waiting for aggregation begin ...')
        for _event in self.contractor.contract_events():
            if isinstance(_event, ReadyForAggregationEvent):
                if _event.round != self.current_round:
                    continue
                return
            elif isinstance(_event, FinishTaskEvent):
                raise TaskComplete()
            elif isinstance(_event, ResetRoundEvent):
                raise ResetRound()

    def _wait_for_closing_round(self):
        """Wait for closing current round of training."""
        self.push_log(f'Waiting for closing signal of training round {self.current_round} ...')
        for _event in self.contractor.contract_events():
            if isinstance(_event, CloseRoundEvent):
                if _event.round != self.current_round:
                    continue
                return
            elif isinstance(_event, FinishTaskEvent):
                raise TaskComplete()
            elif isinstance(_event, ResetRoundEvent):
                raise ResetRound()


class FedSGDScheduler(FedAvgScheduler):
    """Implementation of FedSGD."""

    def __init__(self,
                 max_rounds: int = 0,
                 calculation_timeout: int = 300,
                 schedule_timeout: int = 30,
                 log_rounds: int = 0):
        """Init.

        By now, IterableDataset with no length is not supported.

        Args:
            max_rounds:
                Maximal number of training rounds.
            calculation_timeout:
                Seconds to timeout for calculation in a round. Takeing off timeout
                by setting its value to 0.
            schedule_timeout:
                Seconds to timeout for process scheduling. Takeing off timeout
                by setting its value to 0.
            log_rounds:
                The number of rounds to run testing and log the result. Skip it
                by setting its value to 0.
        """
        super().__init__(max_rounds=max_rounds,
                         merge_epochs=1,
                         calculation_timeout=calculation_timeout,
                         schedule_timeout=schedule_timeout,
                         log_rounds=log_rounds)

    def _setup_context(self, id: str, task_id: str, is_initiator: bool = False):
        super()._setup_context(id=id, task_id=task_id, is_initiator=is_initiator)
        # Since build_train_dataloader is implemented by the user, and DataLoader base
        # implementation does not allow to modify batch_size after initialization,
        # there is no way to mandatorily set batch size to the correct value.
        # So a post check is used.
        self.push_log(f'train batch size = {self.train_loader.batch_size}')
        try:
            num_samples = len(self.train_loader.dataset)
            self.push_log(f'train examples = {num_samples}')
            if self.train_loader.batch_size != num_samples:
                raise ConfigError('batch size must be the total number of samples.')
        except TypeError:
            raise ConfigError('Does not support iterable dataset with no length.')
