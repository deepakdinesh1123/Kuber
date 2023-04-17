from typing import (
    ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping,
    Optional as _Optional, Union as _Union,
)

from google.protobuf import descriptor as _descriptor, message as _message
from google.protobuf.internal import containers as _containers

DESCRIPTOR: _descriptor.FileDescriptor

class CopyResponse(_message.Message):
    __slots__ = ["success"]
    SUCCESS_FIELD_NUMBER: _ClassVar[int]
    success: bool
    def __init__(self, success: bool = ...) -> None: ...

class File(_message.Message):
    __slots__ = ["name", "path"]
    NAME_FIELD_NUMBER: _ClassVar[int]
    PATH_FIELD_NUMBER: _ClassVar[int]
    name: str
    path: str
    def __init__(
        self, name: _Optional[str] = ..., path: _Optional[str] = ...
    ) -> None: ...

class FilesToCopy(_message.Message):
    __slots__ = ["container", "file"]
    CONTAINER_FIELD_NUMBER: _ClassVar[int]
    FILE_FIELD_NUMBER: _ClassVar[int]
    container: str
    file: _containers.RepeatedCompositeFieldContainer[File]
    def __init__(
        self,
        container: _Optional[str] = ...,
        file: _Optional[_Iterable[_Union[File, _Mapping]]] = ...,
    ) -> None: ...
