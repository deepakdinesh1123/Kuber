from typing import (
    ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union,
)

from google.protobuf import descriptor as _descriptor, message as _message

DESCRIPTOR: _descriptor.FileDescriptor

class Container(_message.Message):
    __slots__ = ["image", "name", "network"]
    IMAGE_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    NETWORK_FIELD_NUMBER: _ClassVar[int]
    image: str
    name: str
    network: str
    def __init__(
        self,
        name: _Optional[str] = ...,
        image: _Optional[str] = ...,
        network: _Optional[str] = ...,
    ) -> None: ...

class ContainerCreated(_message.Message):
    __slots__ = ["logs", "name"]
    LOGS_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    logs: str
    name: str
    def __init__(
        self, name: _Optional[str] = ..., logs: _Optional[str] = ...
    ) -> None: ...

class ContainerCreationError(_message.Message):
    __slots__ = ["error"]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    error: str
    def __init__(self, error: _Optional[str] = ...) -> None: ...

class ContainerCreationResponse(_message.Message):
    __slots__ = ["container_created", "container_error"]
    CONTAINER_CREATED_FIELD_NUMBER: _ClassVar[int]
    CONTAINER_ERROR_FIELD_NUMBER: _ClassVar[int]
    container_created: ContainerCreated
    container_error: ContainerCreationError
    def __init__(
        self,
        container_created: _Optional[_Union[ContainerCreated, _Mapping]] = ...,
        container_error: _Optional[_Union[ContainerCreationError, _Mapping]] = ...,
    ) -> None: ...
