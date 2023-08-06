import json
import uuid
from copy import deepcopy

from dataclasses import dataclass
from enum import Enum, auto
from typing import Dict, List, Optional, Union


class StepStatus(Enum):
    # Note: this protocol needs to consider Dead-locking:
    #   examples: we should not have a step get stuck because of a failed communication or otherwise
    INIT = auto()
    ACK = auto()
    DONE = auto()
    FAIL = auto()


class DeviceType(Enum):
    STANDARD = "standard"
    GP3 = "gp3"
    GP2 = "gp2"
    ST1 = "st1"
    SC1 = "sc1"
    IO1 = "io1"
    IO2 = "io2"


class InstructionMetaclass(type):

    def __new__(mcs, instruction_type: str, action_id: str, *args, **kwargs):
        cls = globals()[instruction_type]
        if not issubclass(cls, StepInstruction):
            raise TypeError(f"{cls.__name__} is not of StepInstruction type")

        instruction = cls(action_id, *args, **kwargs)
        return instruction

    @classmethod
    def deserialize_instruction(mcs, instruction_val: Union[str, dict]) -> 'StepInstruction':
        if isinstance(instruction_val, str):
            instruction_val = json.loads(instruction_val)
        try:
            instruction_type = instruction_val.pop('instruction_type')
            instruction = mcs(instruction_type=instruction_type, **instruction_val)
        except Exception as e:
            raise Exception(f"Failed to create instance from {instruction_type} class | Error: {e}")
        instruction.set_values_from_dict(instruction_val)
        return instruction


@dataclass
class StepInstruction:
    action_id: str
    step_id: Optional[str]
    status: Optional[StepStatus]

    def __post_init__(self) -> None:
        if self.status is None:
            self.status = StepStatus.INIT
        if self.step_id is None:
            self.step_id = str(uuid.uuid4())
        self._instruction_type = None

    def as_dict(self) -> dict:
        dict_values = deepcopy(self.__dict__)
        # Enum members
        for key, value in filter(lambda t: isinstance(t[1], Enum), self.__dict__.items()):
            dict_values[key] = value.name

            dict_values.update({
                key: getattr(self, key).name
            })

        dict_values['instruction_type'] = self.instruction_type
        dict_values.pop('_instruction_type')

        return dict_values

    def serialize(self) -> str:
        return json.dumps(self.as_dict())

    @property
    def instruction_type(self):
        if not self._instruction_type:
            self._instruction_type = type(self).__name__
        return self._instruction_type

    def set_values_from_dict(self, instruction_data: dict):
        # Set Enum members values
        enum_members = list(filter(lambda k: isinstance(getattr(self, k), Enum), self.__dict__.keys()))
        for key in enum_members:
            enum_cls = getattr(self, key).__class__
            setattr(self, key, getattr(enum_cls, instruction_data[key]))

        for key, val in instruction_data.items():
            if key in enum_members or key == 'instruction_type':
                continue
            setattr(self, key, val)


# TODO: move correct/common elements here
@dataclass
class MachineInstruction(StepInstruction):
    ...

@dataclass
class CloudInstruction(StepInstruction):
    ...


@dataclass
class AddDiskCloud(CloudInstruction):
    instance_id: str # Note: will need region/az but should
                     # be available from other source/context
    dev_type: DeviceType
    dev_delete_on_terminate: bool
    dev_size_gb: int
    dev_iops: Optional[int] = None
    dev_throughput: Optional[int] = None


@dataclass
class AddDiskMachine(MachineInstruction):
    dev_path: str
    fs_id: str
    fs_mount_path: str
    volume_id: str
    dev_map: Optional[str] = None


@dataclass
class ModifyDiskCloud(CloudInstruction):
    dev_id: str  # this is volume id
    dev_type: Optional[DeviceType] = None
    dev_size_gb: Optional[int] = None  # Note: today this is change in size - should be final size
    dev_iops: Optional[int] = None
    dev_throughput: Optional[int] = None
    # check if we need dev old size

    def __post_init__(self) -> None:
        super().__post_init__() # TODO: check if necessary for __post_init__
        if self.dev_type is None \
            and self.dev_size_gb is None \
            and self.dev_iops is None \
            and self.dev_throughput is None:
            raise Exception(f"Must modify at least one attribute")


@dataclass
class ExtendDiskSizeMachine(MachineInstruction):
    # Note: this is a copy of AddDiskMachine
    fs_id: str  # will there be ability to grab this from context?
    fs_mount_path: str
    # dev_path: str  # This is necessary for Monitored disk Extend only actions
                     # Probably better to have a separate payload/step
    btrfs_dev_id: int


@dataclass
class ResizeDisksMachine(MachineInstruction):
    fs_id: str  # will there be ability to grab this from context?
    fs_mount_path: str

    resize_btrfs_dev_ids: Dict[str, int] # action_id, btrfs_dev_id


@dataclass
class GradualRemoveChunk:
    iterations: int # Note: 0 iterations will represent delete
    chunk_size_gb: int # Note: respective chunk_size for 0 iter represents pause/delete threshold


@dataclass
class RemoveDiskMachine(MachineInstruction):
    fs_id: str  # will there be ability to grab this from context?
    fs_mount_path: str
    btrfs_dev_id: int
    dev_path: str
    chunk_scheme: List[GradualRemoveChunk]  # Note: Order matters
    cutoff_gb: int


###### TODO: discuss with Osher - separate instructions, or overlap into one
@dataclass
class ModifyRemoveDisksMachine(MachineInstruction):
    # will service Revert/ChangingTarget/NewResize
    # because they are all correlated to the same
    # instruction data - changing cutoff
    fs_id: str  # will there be ability to grab this from context?
    cutoff_gb: int
    revert_btrfs_dev_ids: Dict[str, int] # action_id, btrfs_dev_id

###### TODO: END discuss with Osher


@dataclass
class RemoveDiskCloud(CloudInstruction):
    volume_id: str
