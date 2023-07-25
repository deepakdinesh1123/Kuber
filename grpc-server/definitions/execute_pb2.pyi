from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class ExecuteRequest(_message.Message):
    __slots__ = ["container_name", "command", "dir"]
    CONTAINER_NAME_FIELD_NUMBER: _ClassVar[int]
    COMMAND_FIELD_NUMBER: _ClassVar[int]
    DIR_FIELD_NUMBER: _ClassVar[int]
    container_name: str
    command: str
    dir: str
    def __init__(self, container_name: _Optional[str] = ..., command: _Optional[str] = ..., dir: _Optional[str] = ...) -> None: ...

class TestRequest(_message.Message):
    __slots__ = ["container_name", "test_script", "test_script_name", "test_cmd", "test_dir", "test_script_dir", "expected_output"]
    CONTAINER_NAME_FIELD_NUMBER: _ClassVar[int]
    TEST_SCRIPT_FIELD_NUMBER: _ClassVar[int]
    TEST_SCRIPT_NAME_FIELD_NUMBER: _ClassVar[int]
    TEST_CMD_FIELD_NUMBER: _ClassVar[int]
    TEST_DIR_FIELD_NUMBER: _ClassVar[int]
    TEST_SCRIPT_DIR_FIELD_NUMBER: _ClassVar[int]
    EXPECTED_OUTPUT_FIELD_NUMBER: _ClassVar[int]
    container_name: str
    test_script: str
    test_script_name: str
    test_cmd: str
    test_dir: str
    test_script_dir: str
    expected_output: str
    def __init__(self, container_name: _Optional[str] = ..., test_script: _Optional[str] = ..., test_script_name: _Optional[str] = ..., test_cmd: _Optional[str] = ..., test_dir: _Optional[str] = ..., test_script_dir: _Optional[str] = ..., expected_output: _Optional[str] = ...) -> None: ...

class TestResult(_message.Message):
    __slots__ = ["result", "success"]
    RESULT_FIELD_NUMBER: _ClassVar[int]
    SUCCESS_FIELD_NUMBER: _ClassVar[int]
    result: str
    success: bool
    def __init__(self, result: _Optional[str] = ..., success: bool = ...) -> None: ...

class ExecutionResponse(_message.Message):
    __slots__ = ["message"]
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    message: str
    def __init__(self, message: _Optional[str] = ...) -> None: ...
