"""The host of a hetero_nn task.

Reference: https://arxiv.org/pdf/2007.06849.pdf
"""

import io
import json
import os
import random
import shutil
import sys
import traceback
from abc import ABCMeta, abstractmethod
from dataclasses import dataclass
from tempfile import TemporaryFile
from typing import Dict, List, Set, Tuple, Union
from zipfile import ZipFile

import tenseal as ts
import torch
import torch.nn as nn
import torch.optim as optim
from torch.utils.tensorboard import SummaryWriter

from .. import get_result_dir, get_runtime_dir, logger
from ..data_channel import SharedFileDataChannel
from ..scheduler import ConfigError, Scheduler, TaskComplete, TaskFailed
from .hetero_nn import ResetRound, _SimplifiedOptimizer
from .psi import RSAPSICollaboratorScheduler, RSAPSIInitiatorScheduler
from .secure_contractor import (CheckinEvent, CheckinResponseEvent,
                                CloseRoundEvent, CloseTestRoundEvent,
                                CollaboratorCompleteEvent, CompleteTaskEvent,
                                FailTaskEvent, HeteroNNContractor,
                                ReadyForFusionEvent,
                                ReadyForNoisedProjectionEvent,
                                ReadyForNoisedWGradEvent, ResetRoundEvent,
                                SendCipherFeatureGradEvent,
                                SendCipherPorjectionEvent,
                                SendCipherWGradEvent, SendFeatureEvent,
                                SendNoisedPorjectionEvent,
                                SendNoisedWGradEvent, StartRoundEvent,
                                StartTestRoundEvent, SyncStateEvent,
                                SyncStateResponseEvent)

__all__ = ['SecureHeteroNNHostScheduler', 'SecureHeteroNNCollaboratorScheduler']

_HE_Tensor = Union[torch.Tensor, ts.CKKSTensor]
_FEATURE_KEY = str

_ENCODING = 'utf-8'
_LEN_BYTES = 4
_BYTES_ORDER = 'big'


@dataclass
class _CKKSTensorWrapper:

    feature_key: str
    cipher: bytes
    context: bytes = None

    def to_bytes(self) -> bytes:
        """Encode to bytes data."""
        assert (
            self.feature_key and isinstance(self.feature_key, str)
        ), f'Invalid feature key: {self.feature_key}.'
        assert self.cipher and isinstance(self.cipher, bytes), f'Invalid cipher: {self.cipher}.'
        assert (
            not self.context or isinstance(self.context, bytes)
        ), f'Invalid context: {self.context}.'

        data_stream = b''
        key_bytes = self.feature_key.encode(encoding=_ENCODING)
        key_len = len(key_bytes)
        data_stream += key_len.to_bytes(_LEN_BYTES, _BYTES_ORDER) + key_bytes
        cipher_len = len(self.cipher)
        data_stream += cipher_len.to_bytes(_LEN_BYTES, _BYTES_ORDER) + self.cipher
        data_stream += self.context if self.context else b''
        return data_stream

    @classmethod
    def from_bytes(self, data: bytes) -> '_CKKSTensorWrapper':
        """Initialize a _FeatureCipher object from bytes data."""
        archor = 0
        assert len(data) > archor + _LEN_BYTES, 'Invalid feature key length data.'
        key_len = int.from_bytes(data[archor:(archor + _LEN_BYTES)], _BYTES_ORDER)
        archor += _LEN_BYTES
        assert len(data) > archor + key_len, 'Invalid feature key data.'
        feature_key = data[archor:(archor + key_len)].decode(encoding=_ENCODING)
        archor += key_len
        assert len(data) > archor + _LEN_BYTES, 'Invalid cipher length data.'
        cipher_len = int.from_bytes(data[archor:(archor + _LEN_BYTES)], _BYTES_ORDER)
        archor += _LEN_BYTES
        assert len(data) >= archor + cipher_len, 'Invalid cipher data.'
        cipher = data[archor:(archor + cipher_len)]
        archor += cipher_len
        context = data[archor:] or None
        return _CKKSTensorWrapper(feature_key=feature_key, cipher=cipher, context=context)


@dataclass
class _NoisedWGradWrapper:

    feature_key: str
    noised_grad: torch.Tensor
    cipher_epsilon_acc: bytes
    context: bytes

    def to_bytes(self) -> bytes:
        """Encode to bytes data."""
        assert (
            self.feature_key and isinstance(self.feature_key, str)
        ), f'Invalid feature key: {self.feature_key}.'
        assert (
            self.noised_grad is not None and isinstance(self.noised_grad, torch.Tensor)
        ), f'Invalid noised grad: {self.noised_grad}.'
        assert (
            self.cipher_epsilon_acc and isinstance(self.cipher_epsilon_acc, bytes)
        ), f'Invalid cipher epsilon acc: {self.cipher_epsilon_acc}.'
        assert (
            self.context and isinstance(self.context, bytes)
        ), f'Invalid context: {self.context}.'

        data_stream = b''
        key_bytes = self.feature_key.encode(encoding=_ENCODING)
        key_len = len(key_bytes)
        data_stream += key_len.to_bytes(_LEN_BYTES, _BYTES_ORDER) + key_bytes
        with TemporaryFile() as tf:
            torch.save(self.noised_grad, tf)
            tf.seek(0)
            grad_bytes = tf.read()
            grad_len = len(grad_bytes)
            data_stream += grad_len.to_bytes(_LEN_BYTES, _BYTES_ORDER) + grad_bytes
        cipher_len = len(self.cipher_epsilon_acc)
        data_stream += cipher_len.to_bytes(_LEN_BYTES, _BYTES_ORDER) + self.cipher_epsilon_acc
        data_stream += self.context
        return data_stream

    @classmethod
    def from_bytes(self, data: bytes) -> '_NoisedWGradWrapper':
        """Initialize a _NoisedWGradWrapper object from bytes data."""
        archor = 0
        assert len(data) > archor + _LEN_BYTES, 'Invalid feature key length data.'
        key_len = int.from_bytes(data[archor:(archor + _LEN_BYTES)], _BYTES_ORDER)
        archor += _LEN_BYTES
        assert len(data) > archor + key_len, 'Invalid feature key data.'
        feature_key = data[archor:(archor + key_len)].decode(encoding=_ENCODING)
        archor += key_len
        assert len(data) > archor + _LEN_BYTES, 'Invalid grad length data.'
        grad_len = int.from_bytes(data[archor:(archor + _LEN_BYTES)], _BYTES_ORDER)
        archor += _LEN_BYTES
        assert len(data) >= archor + grad_len, 'Invalid grad data.'
        grad_bytes = data[archor:(archor + grad_len)]
        buffer = io.BytesIO(grad_bytes)
        noised_grad = torch.load(buffer)
        archor += grad_len
        assert len(data) > archor + _LEN_BYTES, 'Invalid cipher length data.'
        cipher_len = int.from_bytes(data[archor:(archor + _LEN_BYTES)], _BYTES_ORDER)
        archor += _LEN_BYTES
        assert len(data) >= archor + cipher_len, 'Invalid cipher data.'
        cipher_epsilon_acc = data[archor:(archor + cipher_len)]
        archor += cipher_len
        assert len(data) > archor, 'Invalid context data.'
        context = data[archor:]
        return _NoisedWGradWrapper(feature_key=feature_key,
                                   noised_grad=noised_grad,
                                   cipher_epsilon_acc=cipher_epsilon_acc,
                                   context=context)


class _ProjectLayer(nn.Module):
    """An interactive layer used for fusion features with privacy preserving."""

    def __init__(self, project_config: List[Tuple[str, int, int]]) -> None:
        super().__init__()
        for _key, _in, _out in project_config:
            if not _key or not isinstance(_key, str):
                raise ConfigError(f'Invalid key in project rule: {project_config}')
            if not _in or not isinstance(_in, int) or _in < 1:
                raise ConfigError(f'Invalid input dimension in project rule: {project_config}')
            if not _out or not isinstance(_out, int) or _out < 1:
                raise ConfigError(f'Invalid output dimension in project rule: {project_config}')

        for _key, _in, _out in project_config:
            self.add_module(name=_key, module=nn.Linear(_in, _out, bias=False))

    def forward(self, input_map: Dict[str, _HE_Tensor]) -> Dict[str, _HE_Tensor]:
        output_map = {}
        for _key, _input in input_map.items():
            if isinstance(_input, ts.CKKSTensor):
                W_tensor = self.__getattr__(_key).weight
                output_map[_key] = _input.mm(W_tensor.T.tolist())
            else:
                output_map[_key] = self.__getattr__(_key)(_input)
        return output_map


class SecureHeteroNNScheduler(Scheduler, metaclass=ABCMeta):
    """Base scheduler for heteto_nn tasks."""

    _INIT = 'init'
    _GETHORING = 'gethoring'
    _ID_INTERSECTION = 'id_intersection'
    _READY = 'ready'
    _SYNCHRONIZING = 'synchronizing'
    _IN_A_ROUND = 'in_a_round'
    _PROJECTING = 'projecting'
    _FINISHING = 'finishing'
    _UPDATING = 'updating'
    _PERSISTING = 'persisting'
    _TESTING = 'testing'
    _CLOSING_ROUND = 'closing_round'

    def __init__(self) -> None:
        super().__init__()
        self.feature_model
        self.feature_optimizer

        self._id_intersection = None
        self._local_features: torch.Tensor = None
        self._example_feature_inputs = None

    @abstractmethod
    def _setup_context(self, id: str, task_id: str, is_initiator: bool = False):
        assert id, 'must specify a unique id for every participant'
        assert task_id, 'must specify a task_id for every participant'

        self.id = id
        self.task_id = task_id
        self.is_host = is_initiator
        self._result_dir = get_result_dir(self.task_id)
        self._log_dir = os.path.join(self._result_dir, 'tb_logs')
        self.tb_writer = SummaryWriter(log_dir=self._log_dir)

        self.contractor = HeteroNNContractor(task_id=task_id)
        self.data_channel = SharedFileDataChannel(self.contractor)

    @abstractmethod
    def _launch_process(self):
        ...

    @abstractmethod
    def load_local_ids(self) -> List[str]:
        """Load all local data IDs for PSI."""

    @abstractmethod
    def make_feature_model(self) -> nn.Module:
        """Return a model object to project input to features.

        The output of feature model MUST be a (str_keyword, torch.Tensor) tuple, where
        str_keyword is used by the host to distinguish features from collaborators
        and Tensor is a two dimension (batch, feature_vector) tensor as the input
        of projection layer.
        """

    @property
    def feature_model(self) -> nn.Module:
        if not hasattr(self, '_feature_model'):
            def get_example_input(module, input, output):
                if self._example_feature_inputs is None:
                    self._example_feature_inputs = input

            self._feature_model = self.make_feature_model()
            self._feature_model.register_forward_hook(get_example_input)

        return self._feature_model

    @abstractmethod
    def make_feature_optimizer(self, feature_model: nn.Module) -> optim.Optimizer:
        """Return a optimizer object to facilitate training feature model.

        :args
            :feature_model
                The feature model object to train & test.
        """

    @property
    def feature_optimizer(self) -> optim.Optimizer:
        if not hasattr(self, '_feature_optimizer'):
            assert self.feature_model, 'Must initialize feature model at first.'
            self._feature_optimizer = self.make_feature_optimizer(self.feature_model)
        return self._feature_optimizer

    @property
    def id_intersection(self) -> Set[str]:
        """Return the intersection of whole dataset IDs."""
        assert self._id_intersection is not None, 'Have not run ID intersection process.'
        return self._id_intersection

    @abstractmethod
    def split_dataset(self, id_intersection: Set[str]) -> Tuple[Set[str], Set[str]]:
        """Split dataset into train set and test set.

        NOTE: Must make sure each node gets the same split results.

        :return
            A tuple of ID set of training dataset and of testing dataset:
            (Set[train_ids], Set[test_ids]).
        """

    @property
    def train_ids(self) -> Set[str]:
        """Return the ID set of training dataset intersection."""
        if not hasattr(self, '_train_ids'):
            assert self.id_intersection, 'Must get the whole ID intersection at first.'
            self._train_ids, self._test_ids = self.split_dataset(self.id_intersection.copy())
        return self._train_ids

    @property
    def test_ids(self) -> Set[str]:
        """Return the ID set of testing dataset intersection."""
        if not hasattr(self, '_test_ids'):
            assert self.id_intersection, 'Must get the whole ID intersection at first.'
            self._train_ids, self._test_ids = self.split_dataset(self.id_intersection.copy())
        return self._test_ids

    @abstractmethod
    def _recover_progress():
        """Try to recover progress from last running."""

    @abstractmethod
    def _clean_progress(self):
        """Clean existing progress data."""

    def _run(self, id: str, task_id: str, is_initiator: bool = False, recover: bool = False):
        self._setup_context(id=id, task_id=task_id, is_initiator=is_initiator)
        self.push_log(message='Local context is ready.')
        try:
            if recover:
                self._recover_progress()
            else:
                self._clean_progress()
            self._launch_process()
        except Exception:
            err_stack = '\n'.join(traceback.format_exception(*sys.exc_info()))
            self.push_log(err_stack)

    def push_log(self, message: str):
        """Push a running log message to the task manager."""
        super().push_log(message=message)
        logger.info(message)


class SecureHeteroNNHostScheduler(SecureHeteroNNScheduler):
    """Schedule the process of the host in a hetero_nn task."""

    _WAITING_FOR_FEATURES = 'wait_4_feature'
    _DISTRIBUTING_CIPHER_PROJECTION = 'distribute_cipher_proj'
    _COLLECTING_NOISED_PROJECTION = 'collect_proj'
    _GETTING_GRAD = 'calc_loss'
    _DISTRIBUTING_CIPHER_W_GRAD = 'distribute_w_grad'
    _COLLECTING_NOISED_W_GRAD = 'collect_w_grad'
    _DISTRIBUTING_CIPHER_FEATURE_GRAD = 'distribute_feature_grad'

    def __init__(self,
                 feature_key: str,
                 project_layer_config: List[Tuple[str, int, int]],
                 project_layer_lr: float,
                 max_rounds: int = 0,
                 calculation_timeout: int = 300,
                 schedule_timeout: int = 30,
                 log_rounds: int = 0,
                 is_feature_trainable: bool = True) -> None:
        r"""Init.

        :args
            :feature_key
                A unique key of feature used by the host to distinguish features
                from collaborators.
            :project_layer_config
                The input => output rule to define projection matrics which are used
                to project each node's feature tensor to fuse into the input of infer model.
                Each record contains three element: keyword, input_dimension, output_dimension.
                The keyword is used to distinguish features' owner, the input_dimension
                gives the dimension of the feature, the output_dimension defines the
                dimension of the projection result.
            :project_layer_lr
                The learning rate of project layer.
            :max_rounds
                Maximal number of training rounds.
            :calculation_timeout
                Seconds to timeout for calculation in a round. Takeing off timeout
                by setting its value to 0.
            :schedule_timeout
                Seconds to timeout for process scheduling. Takeing off timeout
                by setting its value to 0.
            :log_rounds
                The number of rounds to run testing and log the result. Skip it
                by setting its value to 0.
            :is_feature_trainable
                Decide whether or not train the feature model
        """
        super().__init__()
        self._switch_status(self._INIT)

        self.feature_key = feature_key
        self.project_layer_config = project_layer_config
        self.project_layer_lr = project_layer_lr
        self.max_rounds = max_rounds
        self.calculation_timeout = calculation_timeout
        self.schedule_timeout = schedule_timeout
        self.log_rounds = log_rounds
        self.is_feature_trainable = is_feature_trainable  # TODO 暂时不考虑

        self._validate_config()

        self.project_layer
        self.infer_model
        self.infer_optimizer

        self.current_round = 1
        self._partners: List[str] = []

        self._example_project_input = None
        self._example_infer_input = None

        self._alpha_map: Dict[str, Dict[_FEATURE_KEY, _HE_Tensor]] = {}
        self._feature_projection_map: Dict[_FEATURE_KEY, _HE_Tensor] = {}
        self._feature_fusion_map: Dict[_FEATURE_KEY, torch.Tensor] = {}
        self._noised_w_grad_map: Dict[_FEATURE_KEY, _NoisedWGradWrapper] = {}
        self._batched_test_features: List[List[Dict[_FEATURE_KEY, _HE_Tensor]]] = []
        self._epsilon_host = None

    def _validate_config(self):
        if not self.feature_key or not isinstance(self.feature_key, str):
            raise ConfigError('Must specify a feature_key of type string.')
        if not self.project_layer_config or not isinstance(self.project_layer_config, list):
            raise ConfigError(f'Invalid project layer config: {self.project_layer_config}.')
        for _config in self.project_layer_config:
            if not _config or not isinstance(_config, tuple) or len(_config) != 3:
                raise ConfigError(f'Invalid project layer config items: {_config}.')
            _key, _in_dim, _out_dim = _config
            if (
                not _key or not isinstance(_key, str)
                or not _in_dim or not isinstance(_in_dim, int) or _in_dim < 1
                or not _out_dim or not isinstance(_out_dim, int) or _out_dim < 1
            ):
                raise ConfigError(f'Invalid project layer config items: {_config}.')
        if (
            not self.project_layer_lr
            or not isinstance(self.project_layer_lr, float)
            or self.project_layer_lr <= 0
        ):
            raise ConfigError(f'Invalid project layer learning rate: {self.project_layer_lr}.')

    @property
    def project_layer(self) -> nn.Module:
        """Return a model object to project features."""
        if not hasattr(self, '_project_layer'):
            def get_example_input(module, input, output):
                if self._example_project_input is None:
                    self._example_project_input = input

            self._project_layer = _ProjectLayer(project_config=self.project_layer_config)
            self._project_layer.register_forward_hook(get_example_input)

        return self._project_layer

    @property
    def project_optimizer(self) -> _SimplifiedOptimizer:
        """Return a proxy optimizer to facilitate updating parameters of the project layer."""

        class _ProjectOptimizerImpl(_SimplifiedOptimizer):

            def __init__(self, host_obj: SecureHeteroNNHostScheduler) -> None:
                super().__init__()
                self.host_obj = host_obj

            def zero_grad(self):
                if self.host_obj.project_layer is not None:
                    for _param in self.host_obj.project_layer.parameters():
                        if _param.grad is not None:
                            _param.grad.zero_()
                if self.host_obj._feature_fusion_map is not None:
                    for _proj in self.host_obj._feature_fusion_map.values():
                        if _proj.grad is not None:
                            _proj.grad.zero_()

            def step(self):
                self.host_obj._switch_status(self.host_obj._DISTRIBUTING_CIPHER_W_GRAD)
                self.host_obj._distribute_cipher_w_grad()
                self.host_obj._switch_status(self.host_obj._COLLECTING_NOISED_W_GRAD)
                self.host_obj._collect_noised_w_grad()
                self.host_obj._switch_status(self.host_obj._DISTRIBUTING_CIPHER_FEATURE_GRAD)
                self.host_obj._distribute_cipher_feature_grad()
                self.host_obj._switch_status(self.host_obj._UPDATING)
                self.host_obj._update_project_layer_weight()

        if not hasattr(self, '_project_optimizer'):
            self._project_optimizer = _ProjectOptimizerImpl(host_obj=self)
        return self._project_optimizer

    @abstractmethod
    def make_infer_model(self) -> nn.Module:
        """Return a model object to infer business results."""

    @property
    def infer_model(self) -> nn.Module:
        if not hasattr(self, '_infer_model'):
            def get_example_input(module, input, output):
                if self._example_infer_input is None:
                    self._example_infer_input = input

            self._infer_model = self.make_infer_model()
            self._infer_model.register_forward_hook(get_example_input)

        return self._infer_model

    @abstractmethod
    def make_infer_optimizer(self, infer_model: nn.Module) -> optim.Optimizer:
        """Return a optimizer object to facilitate training infer model.

        :args
            :infer_model
                The infer model object to train & test.
        """

    @property
    def infer_optimizer(self) -> optim.Optimizer:
        if not hasattr(self, '_infer_optimizer'):
            assert self.infer_model, 'Must initialize infor model at first.'
            self._infer_optimizer = self.make_infer_optimizer(self.infer_model)
        return self._infer_optimizer

    @property
    def optimizer(self) -> _SimplifiedOptimizer:
        """Return a general optimizer to wrap the 3 (feature, project, infer) optimizers."""

        class _OptimizerImpl(_SimplifiedOptimizer):

            def __init__(self, host_obj: SecureHeteroNNHostScheduler) -> None:
                super().__init__()
                self.host_obj = host_obj

            def zero_grad(self):
                self.host_obj.infer_optimizer.zero_grad()
                self.host_obj.project_optimizer.zero_grad()
                self.host_obj.feature_optimizer.zero_grad()

            def step(self):
                self.host_obj.infer_optimizer.step()
                self.host_obj.project_optimizer.step()
                self.host_obj.feature_optimizer.step()

        if not hasattr(self, '_optimizer'):
            self._optimizer = _OptimizerImpl(host_obj=self)
        return self._optimizer

    @abstractmethod
    def iterate_train_feature(self,
                              feature_model: nn.Module,
                              train_ids: Set[str]) -> Tuple[torch.Tensor, torch.Tensor]:
        """Iterate over train dataset and features a batch of data each time.

        :args
            :feature_model
                The feature model object to train & test.
            :train_ids
                The ID set of train dataset.
        :return
            A tuple of a batch of train data and their labels. (train_data, labels)
        """

    @abstractmethod
    def iterate_test_feature(self,
                             feature_model: nn.Module,
                             test_ids: Set[str]) -> Tuple[torch.Tensor, torch.Tensor]:
        """Iterate over test dataset and features a batch of data each time.

        :args
            :feature_model
                The feature model object to train & test.
            :train_ids
                The ID set of test dataset.
        :return
            A tuple of a batch of test data and their labels. (test_data, labels)
        """

    @abstractmethod
    def train_a_batch(self, feature_projection: Dict[str, torch.Tensor], labels: torch.Tensor):
        """Train a batch of data in infer model.

        :args
            :feature_projection
                A map containing features from all nodes of type feature_key => feature_tensor.
            :labels
                Corresponding labels of the batch of data.
        """

    @abstractmethod
    def test(self,
             batched_feature_projection: List[Dict[str, torch.Tensor]],
             batched_labels: List[torch.Tensor]):
        """Define the testing steps.

        If you do not want to do testing after training, simply make it pass.

        :args
            :batched_feature_projections
                A list of feature projection grouped by batch of testing data. Each batch
                is a map containing features from all nodes of type feature_key => feature_tensor.
            :batched_labels
                A list of labels grouped by batch of testing data.
        """

    def validate_context(self):
        """Validate if the local running context is ready.

        For example: check if train and test dataset could be loaded successfully.
        """
        if self.feature_model is None:
            raise ConfigError('Failed to initialize a feature model.')
        if not isinstance(self.feature_model, nn.Module):
            err_msg = 'Support feature model of type torch.Module only.'
            err_msg += f'Got a {type(self.feature_model)} object.'
            raise ConfigError(err_msg)
        if self.feature_optimizer is None:
            raise ConfigError('Failed to initialize a feature optimizer.')
        if not isinstance(self.feature_optimizer, optim.Optimizer):
            err_msg = 'Support feature optimizer of type torch.optim.Optimizer only.'
            err_msg += f'Got a {type(self.feature_optimizer)} object.'
            raise ConfigError(err_msg)

        if self.infer_model is None:
            raise ConfigError('Failed to initialize a infer model.')
        if not isinstance(self.infer_model, nn.Module):
            err_msg = 'Support infer model of type torch.Module only.'
            err_msg += f'Got a {type(self.infer_model)} object.'
            raise ConfigError(err_msg)
        if self.infer_optimizer is None:
            raise ConfigError('Failed to initialize a infer optimizer.')
        if not isinstance(self.infer_optimizer, optim.Optimizer):
            err_msg = 'Support infer optimizer of type torch.optim.Optimizer only.'
            err_msg += f'Got a {type(self.infer_optimizer)} object.'
            raise ConfigError(err_msg)

        if self.project_layer is None:
            raise TaskFailed('Failed to initialize the project layer.')

        if not self._partners:
            raise TaskFailed('No partners.')

    def is_task_finished(self) -> bool:
        """By default true if reach the max rounds configured."""
        return self._is_reach_max_rounds()

    def _init_partners(self):
        """Query and set all partners in this task."""
        self._partners = self.contractor.query_partners()
        self._partners.remove(self.id)

    def _setup_context(self, id: str, task_id: str, is_initiator: bool = False):
        super()._setup_context(id=id, task_id=task_id, is_initiator=is_initiator)

        self._init_partners()
        self._check_in_status = {_partner: False for _partner in self._partners}
        self._is_gathering_complete = False

        self._runtime_dir = get_runtime_dir(self.task_id)
        self._context_file = os.path.join(self._runtime_dir, ".context.json")
        self._checkpoint_dir = os.path.join(self._runtime_dir, 'checkpoint')
        self._feature_ckpt_file = os.path.join(self._checkpoint_dir, "feature_model_ckp.pt")
        self._project_ckpt_file = os.path.join(self._checkpoint_dir, "project_layer_ckp.pt")
        self._infer_ckpt_file = os.path.join(self._checkpoint_dir, "infer_model_ckp.pt")

        self.push_log(message='Begin to validate local context.')
        self.validate_context()

    def _recover_progress(self):
        if not os.path.isfile(self._context_file):
            raise TaskFailed('Failed to recover progress: missing cached context.')

        with open(self._context_file, 'r') as f:
            context_info = json.load(f)
        round = context_info.get('round')
        feature_ckpt_file = context_info.get('feature_ckpt_file')
        project_ckpt_file = context_info.get('project_ckpt_file')
        infer_ckpt_file = context_info.get('infer_ckpt_file')
        assert round and isinstance(round, int) and round > 0, f'Invalid round: {round} .'
        assert (
            feature_ckpt_file and isinstance(feature_ckpt_file, str)
        ), f'Invalid feature_ckpt_file: {feature_ckpt_file} .'
        assert (
            project_ckpt_file and isinstance(project_ckpt_file, str)
        ), f'Invalid project_ckpt_file: {project_ckpt_file} .'
        assert (
            infer_ckpt_file and isinstance(infer_ckpt_file, str)
        ), f'Invalid infer_ckpt_file: {infer_ckpt_file} .'
        if (
            not os.path.isfile(feature_ckpt_file)
            or not os.path.isfile(project_ckpt_file)
            or not os.path.isfile(infer_ckpt_file)
        ):
            raise TaskFailed('Failed to recover progress: missing checkpoint parameters.')

        self.current_round = round
        with open(feature_ckpt_file, 'rb') as f:
            state_dict = torch.load(f)
            self.feature_model.load_state_dict(state_dict)
        with open(project_ckpt_file, 'rb') as f:
            state_dict = torch.load(f)
            self.project_layer.load_state_dict(state_dict)
        with open(infer_ckpt_file, 'rb') as f:
            state_dict = torch.load(f)
            self.infer_model.load_state_dict(state_dict)

    def _clean_progress(self):
        """Clean existing progress data."""
        shutil.rmtree(self._runtime_dir, ignore_errors=True)
        shutil.rmtree(self._result_dir, ignore_errors=True)
        os.makedirs(self._runtime_dir, exist_ok=True)
        os.makedirs(self._checkpoint_dir, exist_ok=True)
        os.makedirs(self._result_dir, exist_ok=True)
        os.makedirs(self._log_dir, exist_ok=True)

    def _is_reach_max_rounds(self) -> bool:
        """Is the max rounds configuration reached."""
        return self.current_round >= self.max_rounds

    def _validate_feature_dict(self, features: Dict[str, ts.CKKSTensor]):
        """Validate feature format."""
        if not features or not isinstance(features, dict) or len(features) != 1:
            self.push_log(f'Received invalid features: {features}')
            err_msg = r'Invalid feature type. It must be a dict of {feature_key: feature tensor}.'
            raise TaskFailed(err_msg)
        _key, _val = features.copy().popitem()
        if not _key or not isinstance(_key, str):
            self.push_log(f'Received invalid feature key: {_key}')
            raise TaskFailed('Invalid feature type. It must contain a keyword of string.')
        if _val is None or not isinstance(_val, ts.CKKSTensor) or len(_val.shape) != 2:
            self.push_log(f'Received invalid feature value: {_val}')
            raise TaskFailed('Invalid feature type. Its value must be a tensor of two dimension.')

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

                    if not self._id_intersection:
                        self._switch_status(self._ID_INTERSECTION)
                        self._make_id_intersection()

                    self._switch_status(self._IN_A_ROUND)
                    self._run_a_round()
                    self._switch_status(self._READY)
                except ResetRound:
                    self.push_log('WARNING: Reset runtime context, there might be an error raised.')
                    self._switch_status(self._READY)
                    self._id_intersection = None
                    continue

                if self.is_task_finished():
                    self.push_log(f'Obtained the final results of task {self.task_id}')
                    self._switch_status(self._FINISHING)
                    self._close_task(is_succ=True)

                self.current_round += 1

        except TaskFailed as err:
            logger.exception(err)
            self._close_task(is_succ=False)

    def _check_in(self):
        """Check in task and connect every partners."""
        self.push_log('Waiting for participants taking part in ...')
        for _event in self.contractor.contract_events():
            if isinstance(_event, CheckinEvent):
                self._handle_check_in(_event)
                if all(self._check_in_status.values()):
                    self._is_gathering_complete = True
                    break
        self.push_log('All partners have gethored.')

    def _handle_check_in(self, _event: CheckinEvent):
        self._check_in_status[_event.peer_id] = True
        self.push_log(f'Welcome a new partner ID: {_event.peer_id}.')
        self.push_log(f'There are {sum(self._check_in_status.values())} partners now.')
        self.contractor.respond_check_in(round=self.current_round,
                                         host=self.id,
                                         nonce=_event.nonce,
                                         requester_id=_event.peer_id)
        if self._is_gathering_complete:
            self.contractor.sync_state(round=self.current_round, host=self.id)

    def _sync_state(self):
        """Synchronize state before each round, so it's easier to manage the process.

        As a host, iterates round, broadcasts and resets context of the new round.
        """
        self.push_log(f'Initiate state synchronization of round {self.current_round}.')
        self.contractor.sync_state(round=self.current_round, host=self.id)

        sync_status = {_partner: False for _partner in self._partners}
        self.push_log('Waiting for synchronization responses ...')
        for _event in self.contractor.contract_events(timeout=0):
            if isinstance(_event, SyncStateResponseEvent):
                if _event.round != self.current_round:
                    continue
                if sync_status.get(_event.peer_id) is False:
                    sync_status[_event.peer_id] = True
                    self.push_log(f'Successfully synchronized state with ID: {_event.peer_id}.')
                if sum(sync_status.values()) == len(self._partners):
                    break
            elif isinstance(_event, CheckinEvent):
                self._handle_check_in(_event)

        self.push_log(f'Successfully synchronized state in round {self.current_round}')

    def _make_id_intersection(self) -> List[str]:
        """Make PSI and get id intersection for training."""
        local_ids = self.load_local_ids()
        psi_scheduler = RSAPSIInitiatorScheduler(
            task_id=self.task_id,
            initiator_id=self.id,
            ids=local_ids,
            collaborator_ids=self._partners,
            contractor=self.contractor
        )
        self._id_intersection = psi_scheduler.make_intersection()

    def _run_a_round(self):
        try:
            self._start_round()
            self.infer_model.train()
            self.project_layer.train()
            self.feature_model.train()
            for _feature_batch, _labels in self.iterate_train_feature(
                self.feature_model, self.train_ids
            ):
                self.push_log('Featured a batch of data.')
                self._local_features = _feature_batch
                self._switch_status(self._WAITING_FOR_FEATURES)
                self._collect_features()
                self._switch_status(self._PROJECTING)
                self._make_projection()
                self._switch_status(self._DISTRIBUTING_CIPHER_PROJECTION)
                self._distribute_cipher_projection()
                self._switch_status(self._COLLECTING_NOISED_PROJECTION)
                self._collect_noised_projection()

                self._switch_status(self._GETTING_GRAD)
                self.train_a_batch(self._feature_fusion_map, _labels)

            self._switch_status(self._PERSISTING)
            self._save_model()
            self._save_runtime_context()
            self._switch_status(self._TESTING)
            self._check_and_run_test()
            self._switch_status(self._CLOSING_ROUND)
            self._close_round()
        except TaskFailed as err:
            err_stack = '\n'.join(traceback.format_exception(*sys.exc_info()))
            self.push_log(err_stack)
            self.contractor.reset_round()
            raise ResetRound(err)

    def _start_round(self):
        """Prepare and start calculation of a round."""
        self.push_log(f'Begin the training of round {self.current_round}.')
        self.contractor.start_round(round=self.current_round)
        self.push_log(f'Calculation of round {self.current_round} is started.')

    def _collect_features(self) -> Dict[str, _HE_Tensor]:
        """Collect all input features from all partners."""
        self.push_log('Waiting for collecting all features from partners ...')
        self.contractor.notify_ready_for_fusion(self.current_round)
        feature_map: Dict[str, Dict[str, _HE_Tensor]] = {
            self.id: {self.feature_key: self._local_features}
        }
        for _event in self.contractor.contract_events(timeout=self.calculation_timeout):
            if isinstance(_event, SendFeatureEvent):
                feature_stream = self.data_channel.receive_stream(apply_event=_event,
                                                                  receiver=self.id)
                cipher_feature = _CKKSTensorWrapper.from_bytes(feature_stream)
                cipher_context = ts.context_from(cipher_feature.context)
                cipher_tensor = ts.ckks_tensor_from(cipher_context, cipher_feature.cipher)
                features = {cipher_feature.feature_key: cipher_tensor}
                self._validate_feature_dict(features)
                feature_map[_event.source] = features
                if len(feature_map) == len(self._partners) + 1:  # plus self
                    self._alpha_map = feature_map
                    return
        # timeout
        raise TaskFailed('Failed to collect all features.')

    def _make_projection(self):
        """Fuse features and get cipher feature projection."""
        self.push_log('Calculating features projection ...')
        features = dict(feature_dict.copy().popitem()
                        for feature_dict in self._alpha_map.values())
        self._feature_projection_map = self.project_layer(features)

    def _distribute_cipher_projection(self):
        """Distribute cipher feature projection to collaborators."""
        self.push_log('Distributing cipher projection to collaborators ...')
        self._epsilon_host = random.randint(1, 2**10)
        for _partner, _cipher_feature in self._alpha_map.items():
            if _partner == self.id:
                continue
            feature_key, _ = _cipher_feature.copy().popitem()
            cipher_tensor: ts.CKKSTensor = self._feature_projection_map[feature_key]
            cipher_tensor.add_(self._epsilon_host)
            cipher_projection = _CKKSTensorWrapper(feature_key=feature_key,
                                                   cipher=cipher_tensor.serialize())
            self.data_channel.send_stream(source=self.id,
                                          target=_partner,
                                          data_stream=cipher_projection.to_bytes())
            self.push_log(f'Distributed cipher projection to collaborator ID: {_partner}')

    @torch.no_grad()
    def _collect_noised_projection(self):
        """Collect noised but plain projection from collaborators."""
        self.push_log('Collecting noised but plain projection from collaborators ...')
        self.contractor.notify_ready_for_noised_projection(round=self.current_round)
        self._feature_fusion_map = {
            self.feature_key: self._feature_projection_map[self.feature_key]
        }
        for _event in self.contractor.contract_events(timeout=self.calculation_timeout):
            if isinstance(_event, SendNoisedPorjectionEvent):
                stream = self.data_channel.receive_stream(apply_event=_event,
                                                          receiver=self.id)
                buffer = io.BytesIO(stream)
                proj_dict: Dict[str, torch.Tensor] = torch.load(buffer)
                feature_key, proj_tensor = proj_dict.copy().popitem()
                proj_tensor.sub_(self._epsilon_host)
                proj_tensor.requires_grad_()
                self._feature_fusion_map[feature_key] = proj_tensor
                self.push_log(f'Received noised projection from ID: {_event.source}.')
                if len(self._feature_fusion_map) == len(self._partners) + 1:  # and self
                    self.push_log('Received all copies of noised projection.')
                    return
        # timeout
        raise TaskFailed('Failed to collect all noised projection.')

    def _distribute_cipher_w_grad(self):
        self._epsilon_host = random.randint(1, 2**10)
        self.push_log('Distributing cipher W grad to collaborators ...')
        for _partner, feature_dict in self._alpha_map.items():
            if _partner == self.id:
                continue
            feature_key, feature_tensor = feature_dict.copy().popitem()
            feature_tensor: ts.CKKSTensor
            proj = self._feature_fusion_map[feature_key]
            cipher_W_grad: ts.CKKSTensor = feature_tensor.transpose()
            try:
                cipher_W_grad.mm_(proj.grad).add_(self._epsilon_host)
            except ValueError:
                logger.error(f'{proj.grad=}')
                raise
            self.data_channel.send_stream(source=self.id,
                                          target=_partner,
                                          data_stream=cipher_W_grad.serialize())
            self.push_log(f'Sent cipher W grad to ID: {_partner}.')
        self.push_log('Distributed all cipher W grad to collaborators.')

    def _collect_noised_w_grad(self):
        """Collect decrypted but noised W grad of project layer from collaborators."""
        self.contractor.notify_ready_for_noised_w_grad(round=self.current_round)
        self.push_log('Collecting noised W grad from collaborators ...')
        self._noised_w_grad_map.clear()
        for _event in self.contractor.contract_events(timeout=self.schedule_timeout):
            if isinstance(_event, SendNoisedWGradEvent):
                stream = self.data_channel.receive_stream(apply_event=_event,
                                                          receiver=self.id)
                noised_grad = _NoisedWGradWrapper.from_bytes(stream)
                self._noised_w_grad_map[noised_grad.feature_key] = noised_grad
                self.push_log(f'Received noised W grad from parter ID: {_event.source}.')
                if len(self._noised_w_grad_map) == len(self._partners):
                    break
        self.push_log('Received all copies of noised W grad.')

    def _distribute_cipher_feature_grad(self):
        """Send cipher feature grad to collaborators."""
        self.push_log('Distributing cipher feature grad to collaborators ...')
        for _partner, feature_dict in self._alpha_map.items():
            if _partner == self.id:
                continue
            feature_key, _ = feature_dict.copy().popitem()
            noised_w_grad = self._noised_w_grad_map[feature_key]
            he_context = ts.context_from(noised_w_grad.context)
            cipher_acc = ts.ckks_tensor_from(he_context, noised_w_grad.cipher_epsilon_acc)
            partner_linear: nn.Linear = self.project_layer.__getattr__(feature_key)
            partner_W = partner_linear.weight
            proj_grad = self._feature_fusion_map[feature_key].grad
            cipher_grad = cipher_acc.broadcast_(partner_W.shape).add_(partner_W.tolist())
            try:
                cipher_grad.mm_(proj_grad.T).transpose_()
            except ValueError:
                logger.error(f'{proj_grad.T=}')
                raise
            self.data_channel.send_stream(source=self.id,
                                          target=_partner,
                                          data_stream=cipher_grad.serialize())
            self.push_log(f'Sent cipher feature grad to ID {_partner}.')
        self.push_log('Distributed all cipher feature grad to collaborators.')

    @torch.no_grad()
    def _update_project_layer_weight(self):
        """Update parameters of project layer."""
        self.push_log('Updating parameters of project layer ...')

        # update self owned project linear layer
        proj_linear: nn.Linear = self.project_layer.__getattr__(self.feature_key)
        proj_linear.weight.sub_(self.project_layer_lr * proj_linear.weight.grad)

        # update partners' project linear layer
        for _feature_key, _noised_w_grad in self._noised_w_grad_map.items():
            proj_linear: nn.Linear = self.project_layer.__getattr__(_feature_key)
            _noised_tensor = _noised_w_grad.noised_grad
            _noised_tensor.sub_(self._epsilon_host)
            proj_linear.weight.sub_(self.project_layer_lr * _noised_tensor)

        self.push_log('Updated parameters of project layer.')

    def _save_model(self):
        """Save latest model state."""
        with open(self._feature_ckpt_file, 'wb') as f:
            torch.save(self.feature_model.state_dict(), f)
        with open(self._project_ckpt_file, 'wb') as f:
            torch.save(self.project_layer.state_dict(), f)
        with open(self._infer_ckpt_file, 'wb') as f:
            torch.save(self.infer_model.state_dict(), f)
        self.push_log('Saved latest parameters locally.')

    def _save_runtime_context(self):
        """Save runtime context information in case of restoring."""
        context_info = {
            'round': self.current_round,
            'feature_ckpt_file': self._feature_ckpt_file,
            'project_ckpt_file': self._project_ckpt_file,
            'infer_ckpt_file': self._infer_ckpt_file
        }
        with open(self._context_file, 'w') as f:
            f.write(json.dumps(context_info, ensure_ascii=False))
        self.push_log('Saved latest runtime context.')

    @torch.no_grad()
    def _check_and_run_test(self):
        """Run test if match configured conditions."""
        if (
            self.current_round == 1
            or (self.log_rounds > 0 and self.current_round % self.log_rounds == 0)
            or self.current_round == self.max_rounds
        ):
            self.push_log('Start a round of test.')

            self.feature_model.eval()
            self.project_layer.eval()
            self.infer_model.eval()

            self.contractor.start_test_round(round=self.current_round)

            batched_feature_projections = []
            batched_labels = []
            for _feature_batch, _labels in self.iterate_test_feature(
                self.feature_model, self.test_ids
            ):
                self._local_features = _feature_batch
                self._switch_status(self._WAITING_FOR_FEATURES)
                self._collect_features()
                self._switch_status(self._PROJECTING)
                self._make_projection()
                self._switch_status(self._DISTRIBUTING_CIPHER_PROJECTION)
                self._distribute_cipher_projection()
                self._switch_status(self._COLLECTING_NOISED_PROJECTION)
                self._collect_noised_projection()
                batched_labels.append(_labels)
                batched_feature_projections.append(self._feature_fusion_map)
                self.push_log('Fused a batch of test data features.')

            self.test(batched_feature_projections=batched_feature_projections,
                      batched_labels=batched_labels)
            self.push_log('Complete a round of test.')

        self.push_log('Skip or close a round of testing.')
        self.contractor.close_test_round(round=self.current_round)

    def _close_round(self):
        """Close current round when finished."""
        self.contractor.close_round(round=self.current_round)
        self.push_log(f'The training of Round {self.current_round} complete.')

    def _close_task(self, is_succ: bool = True):
        """Close the task.

        Broadcasts the finish task event to all participants,
        uploads the final parameters and tells L1 task manager the task is complete.
        """
        self.push_log(f'Closing task {self.task_id} ...')

        self._switch_status(self._FINISHING)
        self.contractor.finish_task(is_succ=is_succ)
        if is_succ:
            report_file_path, model_file_path = self._prepare_task_output()
            self.contractor.upload_task_achivement(aggregator=self.id,
                                                   report_file=report_file_path,
                                                   model_file=model_file_path)
            self._wait_for_all_complete()
            self.contractor.notify_task_completion(result=True)
            self.push_log(f'Task {self.task_id} complete. Byebye!')
        else:
            self.push_log(f'Task {self.task_id} failed. Byebye!')

    def _prepare_task_output(self) -> Tuple[str, str]:
        """Generate final output files of the task.

        :return
            Local paths of the report file and model file.
        """
        self.push_log('Generating task achievement files ...')

        report_file = os.path.join(self._result_dir, 'report.zip')
        with ZipFile(report_file, 'w') as report_zip:
            for path, _, filenames in os.walk(self._log_dir):
                rel_dir = os.path.relpath(path=path, start=self._result_dir)
                rel_dir = rel_dir.lstrip('.')  # ./file => file
                for _file in filenames:
                    rel_path = os.path.join(rel_dir, _file)
                    report_zip.write(os.path.join(path, _file), rel_path)
        report_file_path = os.path.abspath(report_file)

        # torch.jit doesn't work with a TemporaryFile
        feature_model_file = os.path.join(self._result_dir,
                                          f'feature_model_{self.feature_key}.pt')
        with open(feature_model_file, 'wb') as f:
            torch.save(self.feature_model.state_dict(), f)
        project_layer_file = os.path.join(self._result_dir, 'project_layer.pt')
        with open(project_layer_file, 'wb') as f:
            torch.save(self.project_layer.state_dict(), f)
        infer_model_file = f'{os.path.join(self._result_dir, "infer_model.pt")}'
        with open(infer_model_file, 'wb') as f:
            torch.save(self.infer_model.state_dict(), f)
        model_file = os.path.join(self._result_dir, 'model.zip')
        with ZipFile(model_file, 'w') as model_zip:
            model_zip.write(feature_model_file, os.path.basename(feature_model_file))
            model_zip.write(project_layer_file, os.path.basename(project_layer_file))
            model_zip.write(infer_model_file, os.path.basename(infer_model_file))
        model_file_path = os.path.abspath(model_file)

        self.push_log('Task achievement files are ready.')
        return report_file_path, model_file_path

    def _wait_for_all_complete(self):
        """Wait for all collaborators complete their tasks."""
        self.push_log('Waiting for all collaborators complete their tasks ...')
        results = {_peer_id: False for _peer_id in self._partners}
        for _event in self.contractor.contract_events():
            if isinstance(_event, CollaboratorCompleteEvent):
                results[_event.peer_id] = True
                if all(results.values()):
                    break
        self.push_log('All collaborators have completed their tasks.')


class SecureHeteroNNCollaboratorScheduler(SecureHeteroNNScheduler):
    """Schedule the process of a collaborator in a hetero_nn task."""

    _WAITING_FOR_CIPHER_PROJECTION = 'wait_4_proj'
    _SENDING_NOISED_PROJECTION = 'send_proj'
    _WAITING_FOR_W_GRAD = 'wait_4_w_grad'
    _SENDING_NOISED_W_GRAD = 'send_w_grad'
    _WAITING_FOR_FEATUE_GRAD = 'wait_4_feature_grad'

    def __init__(self,
                 feature_key: str,
                 project_layer_lr: int,
                 schedule_timeout: int = 30,
                 is_feature_trainable: bool = True) -> None:
        """Init.

        :args
            :feature_key
                A unique key of feature used by the host to distinguish features
                from collaborators.
            :project_layer_lr
                The learning rate of project layer.
            :schedule_timeout
                Seconds to timeout for process scheduling. Takeing off timeout
                by setting its value to 0.
            :is_feature_trainable
                Decide whether or not train the feature model
        """
        super().__init__()
        self._switch_status(self._INIT)

        self.feature_key = feature_key
        self.project_layer_lr = project_layer_lr
        self.schedule_timeout = schedule_timeout
        self.is_feature_trainable = is_feature_trainable

        self._validate_config()

        self.current_round = 0

        self.host = None

        self._he_context: ts.Context = None
        self._he_context_serialize: bytes = None
        self._epsilon_acc: float = None
        self._proj_tensor: torch.Tensor = None
        self._noised_w_grad: torch.Tensor = None
        self._feature_grad: torch.Tensor = None

    def _validate_config(self):
        if not self.feature_key or not isinstance(self.feature_key, str):
            raise ConfigError('Must specify a feature_key of type string.')
        if (
            not self.project_layer_lr
            or not isinstance(self.project_layer_lr, float)
            or self.project_layer_lr <= 0
        ):
            raise ConfigError(f'Invalid project layer learning rate: {self.project_layer_lr}.')

    def validate_context(self):
        """Validate if the local running context is ready.

        For example: check if train and test dataset could be loaded successfully.
        """
        if self.feature_model is None:
            raise ConfigError('Failed to initialize a feature model.')
        if not isinstance(self.feature_model, nn.Module):
            err_msg = 'Support feature model of type torch.Module only.'
            err_msg += f'Got a {type(self.feature_model)} object.'
            raise ConfigError(err_msg)
        if self.feature_optimizer is None:
            raise ConfigError('Failed to initialize a feature optimizer.')
        if not isinstance(self.feature_optimizer, optim.Optimizer):
            err_msg = 'Support feature optimizer of type torch.optim.Optimizer only.'
            err_msg += f'Got a {type(self.feature_optimizer)} object.'
            raise ConfigError(err_msg)

    @abstractmethod
    def iterate_train_feature(self,
                              feature_model: nn.Module,
                              train_ids: Set[str]) -> torch.Tensor:
        """Iterate over train dataset and features a batch of data each time.

        :args
            :feature_model
                The feature model object to train & test.
            :train_ids
                The ID set of train dataset.
        """

    @abstractmethod
    def iterate_test_feature(self,
                             feature_model: nn.Module,
                             test_ids: Set[str]) -> torch.Tensor:
        """Iterate over test dataset and features a batch of data each time.

        :args
            :feature_model
                The feature model object to train & test.
            :train_ids
                The ID set of test dataset.
        """

    def _setup_context(self, id: str, task_id: str, is_initiator: bool = False):
        super()._setup_context(id=id, task_id=task_id, is_initiator=is_initiator)

        self._he_context = ts.context(ts.SCHEME_TYPE.CKKS,
                                      poly_modulus_degree=2**12,
                                      coeff_mod_bit_sizes=[21, 20, 20, 21])
        self._he_context.global_scale = 2**20
        self._he_context_serialize = self._he_context.serialize()
        self._epsilon_acc = random.gauss(0, 0.1)

        self._runtime_dir = get_runtime_dir(self.task_id)
        self._context_file = os.path.join(self._runtime_dir, ".context.json")
        self._checkpoint_dir = os.path.join(self._runtime_dir, 'checkpoint')
        self._feature_ckpt_file = os.path.join(self._checkpoint_dir, "feature_model_ckp.pt")

        self.push_log(message='Begin to validate local context.')
        self.validate_context()

    def _recover_progress(self):
        if not os.path.isfile(self._context_file):
            raise TaskFailed('Failed to recover progress: missing cached context.')

        with open(self._context_file, 'r') as f:
            context_info = json.load(f)
        feature_ckpt_file = context_info.get('feature_ckpt_file')
        assert (
            feature_ckpt_file and isinstance(feature_ckpt_file, str)
        ), f'Invalid feature_ckpt_file: {feature_ckpt_file} .'
        if not os.path.isfile(feature_ckpt_file):
            raise TaskFailed('Failed to recover progress: missing checkpoint parameters.')

        self.current_round = round
        with open(feature_ckpt_file, 'rb') as f:
            state_dict = torch.load(f)
            self.feature_model.load_state_dict(state_dict)

    def _clean_progress(self):
        """Clean existing progress data."""
        shutil.rmtree(self._runtime_dir, ignore_errors=True)
        shutil.rmtree(self._result_dir, ignore_errors=True)
        os.makedirs(self._runtime_dir, exist_ok=True)
        os.makedirs(self._checkpoint_dir, exist_ok=True)
        os.makedirs(self._result_dir, exist_ok=True)

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

                    if not self._id_intersection:
                        self._switch_status(self._ID_INTERSECTION)
                        self._make_id_intersection()

                    self._switch_status(self._IN_A_ROUND)
                    self._run_a_round()
                    self._switch_status(self._READY)
                except ResetRound:
                    self.push_log('WARNING: Reset runtime context, there might be an error raised.')
                    self._switch_status(self._READY)
                    self._id_intersection = None
                    continue

        except TaskComplete:
            logger.info('Task complete')
            self._close_task(is_succ=True)

        except TaskFailed as err:
            logger.exception(err)
            self._close_task(is_succ=False)

    def _check_in(self):
        """Check in task."""
        is_checked_in = False
        # the host may be in special state so can not response
        # correctly nor in time, then retry periodically
        self.push_log('Checking in the task ...')
        while not is_checked_in:
            nonce = self.contractor.checkin(peer_id=self.id)
            logger.debug('_wait_for_check_in_response ...')
            for _event in self.contractor.contract_events(timeout=self.schedule_timeout):
                if isinstance(_event, CheckinResponseEvent):
                    if _event.nonce != nonce:
                        continue
                    self.current_round = _event.round
                    self.host = _event.host
                    is_checked_in = True
                    break

                elif isinstance(_event, FailTaskEvent):
                    raise TaskFailed('Aborted by host.')

        self.push_log(f'Node {self.id} have taken part in the task.')

    def _sync_state(self):
        """Synchronize state before each round, so it's easier to manage the process.

        As a partner, synchronizes state and gives a response.
        """
        self.push_log('Waiting for synchronizing state with the host ...')
        for _event in self.contractor.contract_events():
            if isinstance(_event, SyncStateEvent):
                self.current_round = _event.round
                self.contractor.respond_sync_state(round=self.current_round,
                                                   peer_id=self.id,
                                                   host=_event.host)
                self.push_log('Successfully synchronized state with the host.')
                return
            elif isinstance(_event, FailTaskEvent):
                raise TaskFailed('Aborted by host.')
            elif isinstance(_event, CompleteTaskEvent):
                raise TaskComplete()
            elif isinstance(_event, ResetRoundEvent):
                raise ResetRound()

        self.push_log(f'Successfully synchronized state in round {self.current_round}')

    def _make_id_intersection(self) -> List[str]:
        """Make PSI and get id intersection for training."""
        local_ids = self.load_local_ids()
        psi_scheduler = RSAPSICollaboratorScheduler(
            task_id=self.task_id,
            collaborator_id=self.id,
            ids=local_ids,
            contractor=self.contractor
        )
        self._id_intersection = psi_scheduler.collaborate_intersection()

    def _run_a_round(self):
        self._wait_for_starting_round()
        self.feature_model.train()
        for _batch_features in self.iterate_train_feature(self.feature_model, self.train_ids):
            self.push_log('Featured a batch of data.')
            self._switch_status(self._PROJECTING)
            self._local_features = _batch_features
            self._send_feature_cipher()
            self._switch_status(self._WAITING_FOR_CIPHER_PROJECTION)
            self._wait_for_cipher_projection()
            self._switch_status(self._SENDING_NOISED_PROJECTION)
            self._send_noised_projection()

            self._switch_status(self._WAITING_FOR_W_GRAD)
            self._wait_for_w_grad()
            self._switch_status(self._SENDING_NOISED_W_GRAD)
            self._send_noised_w_grad()
            self._switch_status(self._WAITING_FOR_FEATUE_GRAD)
            self._wait_for_feature_grad()
            self._switch_status(self._UPDATING)
            self.feature_optimizer.zero_grad()
            self._local_features.backward(self._feature_grad)
            self.feature_optimizer.step()

        self._switch_status(self._PERSISTING)
        self._save_model()
        self._save_runtime_context()

        self._switch_status(self._TESTING)
        self._wait_for_testing_round()

        self._switch_status(self._CLOSING_ROUND)
        self._wait_for_closing_round()

        self.push_log(f'ID: {self.id} finished training task of round {self.current_round}.')

    def _wait_for_starting_round(self):
        """Wait for starting a new round of training ..."""
        self.push_log(f'Waiting for training of round {self.current_round} begin ...')
        for _event in self.contractor.contract_events():
            if isinstance(_event, StartRoundEvent):
                assert (
                    _event.round == self.current_round
                ), f'Lost synchronization, host: {_event.round}; local: {self.current_round}.'
                self.push_log(f'Training of round {self.current_round} begins.')
                return
            elif isinstance(_event, FailTaskEvent):
                raise TaskFailed('Aborted by host.')
            elif isinstance(_event, ResetRoundEvent):
                raise ResetRound()

    def _send_feature_cipher(self):
        """Send local features of a batch of data to the host."""
        self.push_log('Waiting for sending features ...')
        for _event in self.contractor.contract_events():
            if isinstance(_event, ReadyForFusionEvent):
                assert (
                    _event.round == self.current_round
                ), f'Lost synchronization, host: {_event.round}; local: {self.current_round}.'
                break
            elif isinstance(_event, FailTaskEvent):
                raise TaskFailed('Aborted by host.')
            elif isinstance(_event, ResetRoundEvent):
                raise ResetRound()

        self.push_log('Begin to send features.')
        cipher_tensor = ts.ckks_tensor(self._he_context, self._local_features.detach())
        cipher_feature = _CKKSTensorWrapper(feature_key=self.feature_key,
                                            cipher=cipher_tensor.serialize(),
                                            context=self._he_context_serialize)
        self.data_channel.send_stream(source=self.id,
                                      target=self.host,
                                      data_stream=cipher_feature.to_bytes())
        self.push_log('Sending features complete.')

    def _wait_for_cipher_projection(self):
        """Wait for receiving cipher projection of the self owned features."""
        self.push_log('Waiting for receiving cipher projection ...')
        for _event in self.contractor.contract_events():
            if isinstance(_event, SendCipherPorjectionEvent):
                stream = self.data_channel.receive_stream(apply_event=_event,
                                                          receiver=self.id)
                cipher_projection = _CKKSTensorWrapper.from_bytes(stream)
                cipher_tensor = ts.ckks_tensor_from(context=self._he_context,
                                                    data=cipher_projection.cipher)
                projection = cipher_tensor.decrypt()
                self._proj_tensor = torch.tensor(projection.tolist())
                self._proj_tensor.add_(self._local_features * self._epsilon_acc)
                self.push_log('Received cipher projection.')
                return
            elif isinstance(_event, FailTaskEvent):
                raise TaskFailed('Aborted by host.')
            elif isinstance(_event, ResetRoundEvent):
                raise ResetRound()

    def _send_noised_projection(self):
        """Send noised projection to the host for fusion."""
        self.push_log('Waiting for sending noised projection ...')
        for _event in self.contractor.contract_events():
            if isinstance(_event, ReadyForNoisedProjectionEvent):
                with TemporaryFile() as tf:
                    torch.save({self.feature_key: self._proj_tensor}, tf)
                    tf.seek(0)
                    self.data_channel.send_stream(source=self.id,
                                                  target=self.host,
                                                  data_stream=tf.read())
                return
            elif isinstance(_event, FailTaskEvent):
                raise TaskFailed('Aborted by host.')
            elif isinstance(_event, ResetRoundEvent):
                raise ResetRound()

    def _wait_for_w_grad(self):
        """Wait for cipher grad of project layer W to decrypt."""
        self.push_log('Waiting for cipher grad of project layer W ...')
        for _event in self.contractor.contract_events():
            if isinstance(_event, SendCipherWGradEvent):
                stream = self.data_channel.receive_stream(apply_event=_event,
                                                          receiver=self.id)
                cipher_grad = ts.ckks_tensor_from(self._he_context, stream)
                # sample from (-0.005, 0.015) to decrease the overrall speed of
                # accumulation, thus facilitate convergence
                epsilon_collab = random.uniform(-0.005, 0.015)
                self._noised_w_grad = torch.tensor(cipher_grad.decrypt().tolist())
                self._noised_w_grad.add_(epsilon_collab / self.project_layer_lr)
                self._epsilon_acc += epsilon_collab
                break
            elif isinstance(_event, FailTaskEvent):
                raise TaskFailed('Aborted by host.')
            elif isinstance(_event, ResetRoundEvent):
                raise ResetRound()
        self.push_log('Received and decrypted cipher grad of project layer W.')

    def _send_noised_w_grad(self):
        """Send decrypted grad of project layer W to the host."""
        self.push_log('Sending noised grad of project layer W to host ...')
        for _event in self.contractor.contract_events():
            cipher_acc = ts.ckks_tensor(self._he_context, [self._epsilon_acc])
            if isinstance(_event, ReadyForNoisedWGradEvent):
                noised_w_grad = _NoisedWGradWrapper(feature_key=self.feature_key,
                                                    noised_grad=self._noised_w_grad,
                                                    cipher_epsilon_acc=cipher_acc.serialize(),
                                                    context=self._he_context_serialize)
                self.data_channel.send_stream(source=self.id,
                                              target=self.host,
                                              data_stream=noised_w_grad.to_bytes())
                break
            elif isinstance(_event, ResetRoundEvent):
                raise ResetRound()
        self.push_log('Sent noised grad of project layer W to host.')

    def _wait_for_feature_grad(self):
        """Wait for cipher grad of feature model output."""
        self.push_log('Waiting for cipher grad of feature model output ...')
        for _event in self.contractor.contract_events():
            if isinstance(_event, SendCipherFeatureGradEvent):
                stream = self.data_channel.receive_stream(apply_event=_event,
                                                          receiver=self.id)
                cipher_grad = ts.ckks_tensor_from(self._he_context, stream)
                self._feature_grad = torch.tensor(cipher_grad.decrypt().tolist())
                break
            elif isinstance(_event, ResetRoundEvent):
                raise ResetRound()
        self.push_log('Received and decrypted cipher grad of feature model output.')

    def _save_model(self):
        """Save latest model state."""
        with open(self._feature_ckpt_file, 'wb') as f:
            torch.save(self.feature_model.state_dict(), f)
        self.push_log('Saved latest parameters locally.')

    def _save_runtime_context(self):
        """Save runtime context information in case of restoring."""
        context_info = {
            'feature_ckpt_file': self._feature_ckpt_file
        }
        with open(self._context_file, 'w') as f:
            f.write(json.dumps(context_info, ensure_ascii=False))
        self.push_log('Saved latest runtime context.')

    def _wait_for_testing_round(self):
        """Wait for handle a round of testing."""
        self.push_log('Waiting for start a round of testing ...')
        for _event in self.contractor.contract_events():
            if isinstance(_event, StartTestRoundEvent):
                assert (
                    _event.round == self.current_round
                ), f'Lost synchronization, host: {_event.round}; local: {self.current_round}.'

                self.feature_model.eval()
                for _batch_features in self.iterate_test_feature(self.feature_model,
                                                                 self.test_ids):
                    self._switch_status(self._PROJECTING)
                    self._local_features = _batch_features
                    self._send_feature_cipher()
                    self._switch_status(self._WAITING_FOR_CIPHER_PROJECTION)
                    self._wait_for_cipher_projection()
                    self._switch_status(self._SENDING_NOISED_PROJECTION)
                    self._send_noised_projection()
                    self.push_log('Fused a batch of test data features.')

            elif isinstance(_event, CloseTestRoundEvent):
                self.push_log('Skipped or closed a round of testing.')
                return
            elif isinstance(_event, FailTaskEvent):
                raise TaskFailed('Aborted by host.')
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
            elif isinstance(_event, CompleteTaskEvent):
                raise TaskComplete()
            elif isinstance(_event, ResetRoundEvent):
                raise ResetRound()

    def _close_task(self, is_succ: bool = True):
        """Close the task and upload the final parameters."""
        self.push_log(f'Closing task {self.task_id} ...')

        self._switch_status(self._FINISHING)
        if is_succ:
            model_file_path = self._prepare_task_output()
            self.contractor.upload_task_achivement(aggregator=self.id,
                                                   model_file=model_file_path)
            self.contractor.notify_collaborator_complete(peer_id=self.id, host=self.host)
            self.push_log(f'Task {self.task_id} complete. Byebye!')
        else:
            self.push_log(f'Task {self.task_id} failed. Byebye!')

    def _prepare_task_output(self) -> Tuple[str, str]:
        """Generate final output files of the task.

        :return
            Local paths of the model file.
        """
        self.push_log('Generating task achievement files ...')

        # torch.jit doesn't work with a TemporaryFile
        feature_model_file = os.path.join(self._result_dir,
                                          f'feature_model_{self.feature_key}.pt')
        with open(feature_model_file, 'wb') as f:
            torch.save(self.feature_model.state_dict(), f)
        model_file_path = os.path.abspath(feature_model_file)

        self.push_log('Task achievement files are ready.')
        return model_file_path
