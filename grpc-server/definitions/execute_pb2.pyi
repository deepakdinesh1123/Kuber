from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class ExecuteRequest(_message.Message):
    __slots__ = ["container_name", "command", "dir", "stdin"]
    CONTAINER_NAME_FIELD_NUMBER: _ClassVar[int]
    COMMAND_FIELD_NUMBER: _ClassVar[int]
    DIR_FIELD_NUMBER: _ClassVar[int]
    STDIN_FIELD_NUMBER: _ClassVar[int]
    container_name: str
    command: str
    dir: str
    stdin: str
    def __init__(self, container_name: _Optional[str] = ..., command: _Optional[str] = ..., dir: _Optional[str] = ..., stdin: _Optional[str] = ...) -> None: ...

class ExecutionResponse(_message.Message):
    __slots__ = ["message"]
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    message: str
    def __init__(self, message: _Optional[str] = ...) -> None: ...
