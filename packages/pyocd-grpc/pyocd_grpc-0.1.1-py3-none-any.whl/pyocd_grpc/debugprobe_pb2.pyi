from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

AssertReset: Command
Connect: Command
DESCRIPTOR: _descriptor.FileDescriptor
Disconnect: Command
Error: ResponseStatus
IsResetAsserted: Command
JtagSequence: Command
Ok: ResponseStatus
ReadRegister: Command
Reset: Command
SetClock: Command
SwdSequence: Command
SwjSequence: Command
SwoRead: Command
SwoStart: Command
SwoStop: Command
WriteRegister: Command

class AssertResetRequest(_message.Message):
    __slots__ = ["asserted"]
    ASSERTED_FIELD_NUMBER: _ClassVar[int]
    asserted: bool
    def __init__(self, asserted: bool = ...) -> None: ...

class DebugProbeRequest(_message.Message):
    __slots__ = ["assert_reset_req", "command", "id", "read_reg_req", "set_clock_req", "swd_seq_req", "swj_seq_req", "write_reg_req"]
    ASSERT_RESET_REQ_FIELD_NUMBER: _ClassVar[int]
    COMMAND_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    READ_REG_REQ_FIELD_NUMBER: _ClassVar[int]
    SET_CLOCK_REQ_FIELD_NUMBER: _ClassVar[int]
    SWD_SEQ_REQ_FIELD_NUMBER: _ClassVar[int]
    SWJ_SEQ_REQ_FIELD_NUMBER: _ClassVar[int]
    WRITE_REG_REQ_FIELD_NUMBER: _ClassVar[int]
    assert_reset_req: AssertResetRequest
    command: Command
    id: int
    read_reg_req: ReadRegisterRequest
    set_clock_req: SetClockRequest
    swd_seq_req: SwdSequenceRequest
    swj_seq_req: SwjSequenceRequest
    write_reg_req: WriteRegisterRequest
    def __init__(self, id: _Optional[int] = ..., command: _Optional[_Union[Command, str]] = ..., swj_seq_req: _Optional[_Union[SwjSequenceRequest, _Mapping]] = ..., swd_seq_req: _Optional[_Union[SwdSequenceRequest, _Mapping]] = ..., read_reg_req: _Optional[_Union[ReadRegisterRequest, _Mapping]] = ..., write_reg_req: _Optional[_Union[WriteRegisterRequest, _Mapping]] = ..., set_clock_req: _Optional[_Union[SetClockRequest, _Mapping]] = ..., assert_reset_req: _Optional[_Union[AssertResetRequest, _Mapping]] = ...) -> None: ...

class DebugProbeResponse(_message.Message):
    __slots__ = ["id", "is_reset_asserted_rst", "read_reg_rsp", "status", "swd_seq_rsp"]
    ID_FIELD_NUMBER: _ClassVar[int]
    IS_RESET_ASSERTED_RST_FIELD_NUMBER: _ClassVar[int]
    READ_REG_RSP_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    SWD_SEQ_RSP_FIELD_NUMBER: _ClassVar[int]
    id: int
    is_reset_asserted_rst: IsResetAssertedResponse
    read_reg_rsp: ReadRegisterResponse
    status: ResponseStatus
    swd_seq_rsp: SwdSequenceResponse
    def __init__(self, id: _Optional[int] = ..., status: _Optional[_Union[ResponseStatus, str]] = ..., swd_seq_rsp: _Optional[_Union[SwdSequenceResponse, _Mapping]] = ..., read_reg_rsp: _Optional[_Union[ReadRegisterResponse, _Mapping]] = ..., is_reset_asserted_rst: _Optional[_Union[IsResetAssertedResponse, _Mapping]] = ...) -> None: ...

class IsResetAssertedResponse(_message.Message):
    __slots__ = ["asserted"]
    ASSERTED_FIELD_NUMBER: _ClassVar[int]
    asserted: bool
    def __init__(self, asserted: bool = ...) -> None: ...

class ReadRegisterRequest(_message.Message):
    __slots__ = ["address", "ap_n_dp", "count"]
    ADDRESS_FIELD_NUMBER: _ClassVar[int]
    AP_N_DP_FIELD_NUMBER: _ClassVar[int]
    COUNT_FIELD_NUMBER: _ClassVar[int]
    address: int
    ap_n_dp: bool
    count: int
    def __init__(self, ap_n_dp: bool = ..., address: _Optional[int] = ..., count: _Optional[int] = ...) -> None: ...

class ReadRegisterResponse(_message.Message):
    __slots__ = ["values"]
    VALUES_FIELD_NUMBER: _ClassVar[int]
    values: _containers.RepeatedScalarFieldContainer[int]
    def __init__(self, values: _Optional[_Iterable[int]] = ...) -> None: ...

class SetClockRequest(_message.Message):
    __slots__ = ["frequency"]
    FREQUENCY_FIELD_NUMBER: _ClassVar[int]
    frequency: int
    def __init__(self, frequency: _Optional[int] = ...) -> None: ...

class SwdSequenceRequest(_message.Message):
    __slots__ = ["sequence"]
    class Sequence(_message.Message):
        __slots__ = ["cycles", "value"]
        CYCLES_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        cycles: int
        value: int
        def __init__(self, cycles: _Optional[int] = ..., value: _Optional[int] = ...) -> None: ...
    SEQUENCE_FIELD_NUMBER: _ClassVar[int]
    sequence: _containers.RepeatedCompositeFieldContainer[SwdSequenceRequest.Sequence]
    def __init__(self, sequence: _Optional[_Iterable[_Union[SwdSequenceRequest.Sequence, _Mapping]]] = ...) -> None: ...

class SwdSequenceResponse(_message.Message):
    __slots__ = ["bits", "status"]
    BITS_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    bits: _containers.RepeatedScalarFieldContainer[bytes]
    status: int
    def __init__(self, status: _Optional[int] = ..., bits: _Optional[_Iterable[bytes]] = ...) -> None: ...

class SwjSequenceRequest(_message.Message):
    __slots__ = ["bits", "length"]
    BITS_FIELD_NUMBER: _ClassVar[int]
    LENGTH_FIELD_NUMBER: _ClassVar[int]
    bits: _containers.RepeatedScalarFieldContainer[int]
    length: int
    def __init__(self, length: _Optional[int] = ..., bits: _Optional[_Iterable[int]] = ...) -> None: ...

class WriteRegisterRequest(_message.Message):
    __slots__ = ["address", "ap_n_dp", "count", "values"]
    ADDRESS_FIELD_NUMBER: _ClassVar[int]
    AP_N_DP_FIELD_NUMBER: _ClassVar[int]
    COUNT_FIELD_NUMBER: _ClassVar[int]
    VALUES_FIELD_NUMBER: _ClassVar[int]
    address: int
    ap_n_dp: bool
    count: int
    values: _containers.RepeatedScalarFieldContainer[int]
    def __init__(self, ap_n_dp: bool = ..., address: _Optional[int] = ..., count: _Optional[int] = ..., values: _Optional[_Iterable[int]] = ...) -> None: ...

class Command(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = []

class ResponseStatus(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = []
