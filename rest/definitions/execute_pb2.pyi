from typing import (
    ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union,
)

from google.protobuf import descriptor as _descriptor, message as _message

DESCRIPTOR: _descriptor.FileDescriptor

class Error(_message.Message):
    __slots__ = ["error"]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    error: str
    def __init__(self, error: _Optional[str] = ...) -> None: ...

class ExecuteRequest(_message.Message):
    __slots__ = ["command", "container_name"]
    COMMAND_FIELD_NUMBER: _ClassVar[int]
    CONTAINER_NAME_FIELD_NUMBER: _ClassVar[int]
    command: str
    container_name: str
    def __init__(
        self, container_name: _Optional[str] = ..., command: _Optional[str] = ...
    ) -> None: ...

class ExecutionOutput(_message.Message):
    __slots__ = ["output"]
    OUTPUT_FIELD_NUMBER: _ClassVar[int]
    output: str
    def __init__(self, output: _Optional[str] = ...) -> None: ...

class ExecutionResponse(_message.Message):
    __slots__ = ["error", "output", "success"]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    OUTPUT_FIELD_NUMBER: _ClassVar[int]
    SUCCESS_FIELD_NUMBER: _ClassVar[int]
    error: Error
    output: ExecutionOutput
    success: ExecutionSuccess
    def __init__(
        self,
        success: _Optional[_Union[ExecutionSuccess, _Mapping]] = ...,
        error: _Optional[_Union[Error, _Mapping]] = ...,
        output: _Optional[_Union[ExecutionOutput, _Mapping]] = ...,
    ) -> None: ...

class ExecutionSuccess(_message.Message):
    __slots__ = ["result"]
    RESULT_FIELD_NUMBER: _ClassVar[int]
    result: str
    def __init__(self, result: _Optional[str] = ...) -> None: ...
