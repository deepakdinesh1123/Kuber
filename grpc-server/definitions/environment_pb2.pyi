from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class EnvCreationResponse(_message.Message):
    __slots__ = ["containers", "message", "token"]
    CONTAINERS_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    TOKEN_FIELD_NUMBER: _ClassVar[int]
    containers: _containers.RepeatedScalarFieldContainer[str]
    message: str
    token: str
    def __init__(self, message: _Optional[str] = ..., containers: _Optional[_Iterable[str]] = ..., token: _Optional[str] = ...) -> None: ...

class EnvModReq(_message.Message):
    __slots__ = ["id"]
    ID_FIELD_NUMBER: _ClassVar[int]
    id: str
    def __init__(self, id: _Optional[str] = ...) -> None: ...

class EnvironmentRequest(_message.Message):
    __slots__ = ["config", "files", "images", "name", "project_name", "tag", "type"]
    CONFIG_FIELD_NUMBER: _ClassVar[int]
    FILES_FIELD_NUMBER: _ClassVar[int]
    IMAGES_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    PROJECT_NAME_FIELD_NUMBER: _ClassVar[int]
    TAG_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    config: str
    files: _containers.RepeatedScalarFieldContainer[str]
    images: _containers.RepeatedScalarFieldContainer[str]
    name: str
    project_name: str
    tag: str
    type: str
    def __init__(self, name: _Optional[str] = ..., tag: _Optional[str] = ..., config: _Optional[str] = ..., images: _Optional[_Iterable[str]] = ..., files: _Optional[_Iterable[str]] = ..., type: _Optional[str] = ..., project_name: _Optional[str] = ...) -> None: ...

class Response(_message.Message):
    __slots__ = ["message"]
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    message: str
    def __init__(self, message: _Optional[str] = ...) -> None: ...
