from typing import (
    ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union,
)

from google.protobuf import descriptor as _descriptor, message as _message

DESCRIPTOR: _descriptor.FileDescriptor

class Error(_message.Message):
    __slots__ = ["error", "type"]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    error: str
    type: str
    def __init__(
        self, type: _Optional[str] = ..., error: _Optional[str] = ...
    ) -> None: ...

class GenericResponse(_message.Message):
    __slots__ = ["error", "success"]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    SUCCESS_FIELD_NUMBER: _ClassVar[int]
    error: Error
    success: Success
    def __init__(
        self,
        success: _Optional[_Union[Success, _Mapping]] = ...,
        error: _Optional[_Union[Error, _Mapping]] = ...,
    ) -> None: ...

class Image(_message.Message):
    __slots__ = ["dockerfile", "name", "tag"]
    DOCKERFILE_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    TAG_FIELD_NUMBER: _ClassVar[int]
    dockerfile: bytes
    name: str
    tag: str
    def __init__(
        self,
        name: _Optional[str] = ...,
        dockerfile: _Optional[bytes] = ...,
        tag: _Optional[str] = ...,
    ) -> None: ...

class ImageBuildResponse(_message.Message):
    __slots__ = ["error", "success"]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    SUCCESS_FIELD_NUMBER: _ClassVar[int]
    error: Error
    success: ImageBuildSuccess
    def __init__(
        self,
        success: _Optional[_Union[ImageBuildSuccess, _Mapping]] = ...,
        error: _Optional[_Union[Error, _Mapping]] = ...,
    ) -> None: ...

class ImageBuildSuccess(_message.Message):
    __slots__ = ["logs", "name"]
    LOGS_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    logs: str
    name: str
    def __init__(
        self, name: _Optional[str] = ..., logs: _Optional[str] = ...
    ) -> None: ...

class ImageRegistryDetails(_message.Message):
    __slots__ = ["credential", "hub", "name", "tag"]
    CREDENTIAL_FIELD_NUMBER: _ClassVar[int]
    HUB_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    TAG_FIELD_NUMBER: _ClassVar[int]
    credential: str
    hub: str
    name: str
    tag: str
    def __init__(
        self,
        name: _Optional[str] = ...,
        tag: _Optional[str] = ...,
        hub: _Optional[str] = ...,
        credential: _Optional[str] = ...,
    ) -> None: ...

class Success(_message.Message):
    __slots__ = ["msg", "type"]
    MSG_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    msg: str
    type: str
    def __init__(
        self, type: _Optional[str] = ..., msg: _Optional[str] = ...
    ) -> None: ...
