from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class File(_message.Message):
    __slots__ = ["file_name", "path", "container_name", "file_content"]
    FILE_NAME_FIELD_NUMBER: _ClassVar[int]
    PATH_FIELD_NUMBER: _ClassVar[int]
    CONTAINER_NAME_FIELD_NUMBER: _ClassVar[int]
    FILE_CONTENT_FIELD_NUMBER: _ClassVar[int]
    file_name: str
    path: str
    container_name: str
    file_content: str
    def __init__(self, file_name: _Optional[str] = ..., path: _Optional[str] = ..., container_name: _Optional[str] = ..., file_content: _Optional[str] = ...) -> None: ...

class FileDetails(_message.Message):
    __slots__ = ["container_name", "file_name", "path"]
    CONTAINER_NAME_FIELD_NUMBER: _ClassVar[int]
    FILE_NAME_FIELD_NUMBER: _ClassVar[int]
    PATH_FIELD_NUMBER: _ClassVar[int]
    container_name: str
    file_name: str
    path: str
    def __init__(self, container_name: _Optional[str] = ..., file_name: _Optional[str] = ..., path: _Optional[str] = ...) -> None: ...

class FolderDetails(_message.Message):
    __slots__ = ["container_name", "folder_name", "path"]
    CONTAINER_NAME_FIELD_NUMBER: _ClassVar[int]
    FOLDER_NAME_FIELD_NUMBER: _ClassVar[int]
    PATH_FIELD_NUMBER: _ClassVar[int]
    container_name: str
    folder_name: str
    path: str
    def __init__(self, container_name: _Optional[str] = ..., folder_name: _Optional[str] = ..., path: _Optional[str] = ...) -> None: ...

class CopyResponse(_message.Message):
    __slots__ = ["success"]
    SUCCESS_FIELD_NUMBER: _ClassVar[int]
    success: bool
    def __init__(self, success: bool = ...) -> None: ...

class FilesResponse(_message.Message):
    __slots__ = ["line"]
    LINE_FIELD_NUMBER: _ClassVar[int]
    line: str
    def __init__(self, line: _Optional[str] = ...) -> None: ...

class DirectoryStrcuture(_message.Message):
    __slots__ = ["yaml_rep"]
    YAML_REP_FIELD_NUMBER: _ClassVar[int]
    yaml_rep: str
    def __init__(self, yaml_rep: _Optional[str] = ...) -> None: ...
