from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class Container(_message.Message):
    __slots__ = ["container_name"]
    CONTAINER_NAME_FIELD_NUMBER: _ClassVar[int]
    container_name: str
    def __init__(self, container_name: _Optional[str] = ...) -> None: ...

class Project(_message.Message):
    __slots__ = ["project_name"]
    PROJECT_NAME_FIELD_NUMBER: _ClassVar[int]
    project_name: str
    def __init__(self, project_name: _Optional[str] = ...) -> None: ...

class ContainerLogs(_message.Message):
    __slots__ = ["message"]
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    message: str
    def __init__(self, message: _Optional[str] = ...) -> None: ...
