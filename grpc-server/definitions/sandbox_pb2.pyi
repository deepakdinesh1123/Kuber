from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class SandboxRequest(_message.Message):
    __slots__ = ["name", "tag", "config", "images", "files", "env_type", "project_name"]
    NAME_FIELD_NUMBER: _ClassVar[int]
    TAG_FIELD_NUMBER: _ClassVar[int]
    CONFIG_FIELD_NUMBER: _ClassVar[int]
    IMAGES_FIELD_NUMBER: _ClassVar[int]
    FILES_FIELD_NUMBER: _ClassVar[int]
    ENV_TYPE_FIELD_NUMBER: _ClassVar[int]
    PROJECT_NAME_FIELD_NUMBER: _ClassVar[int]
    name: str
    tag: str
    config: str
    images: _containers.RepeatedScalarFieldContainer[str]
    files: _containers.RepeatedScalarFieldContainer[str]
    env_type: str
    project_name: str
    def __init__(self, name: _Optional[str] = ..., tag: _Optional[str] = ..., config: _Optional[str] = ..., images: _Optional[_Iterable[str]] = ..., files: _Optional[_Iterable[str]] = ..., env_type: _Optional[str] = ..., project_name: _Optional[str] = ...) -> None: ...

class SbxModReq(_message.Message):
    __slots__ = ["id"]
    ID_FIELD_NUMBER: _ClassVar[int]
    id: str
    def __init__(self, id: _Optional[str] = ...) -> None: ...

class SbxCreationResponse(_message.Message):
    __slots__ = ["message", "containers", "success"]
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    CONTAINERS_FIELD_NUMBER: _ClassVar[int]
    SUCCESS_FIELD_NUMBER: _ClassVar[int]
    message: str
    containers: _containers.RepeatedScalarFieldContainer[str]
    success: bool
    def __init__(self, message: _Optional[str] = ..., containers: _Optional[_Iterable[str]] = ..., success: bool = ...) -> None: ...

class Response(_message.Message):
    __slots__ = ["message"]
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    message: str
    def __init__(self, message: _Optional[str] = ...) -> None: ...
