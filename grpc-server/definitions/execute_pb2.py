# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: execute.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\rexecute.proto\x12\texecution\"F\n\x0e\x45xecuteRequest\x12\x16\n\x0e\x63ontainer_name\x18\x01 \x01(\t\x12\x0f\n\x07\x63ommand\x18\x02 \x01(\t\x12\x0b\n\x03\x64ir\x18\x03 \x01(\t\"\xaa\x01\n\x0bTestRequest\x12\x16\n\x0e\x63ontainer_name\x18\x01 \x01(\t\x12\x13\n\x0btest_script\x18\x02 \x01(\t\x12\x18\n\x10test_script_name\x18\x03 \x01(\t\x12\x10\n\x08test_cmd\x18\x04 \x01(\t\x12\x10\n\x08test_dir\x18\x05 \x01(\t\x12\x17\n\x0ftest_script_dir\x18\x06 \x01(\t\x12\x17\n\x0f\x65xpected_output\x18\x07 \x01(\t\"-\n\nTestResult\x12\x0e\n\x06result\x18\x01 \x01(\t\x12\x0f\n\x07success\x18\x02 \x01(\x08\"$\n\x11\x45xecutionResponse\x12\x0f\n\x07message\x18\x01 \x01(\t2\x9a\x01\n\x07\x45xecute\x12N\n\x0f\x65xecute_command\x12\x19.execution.ExecuteRequest\x1a\x1c.execution.ExecutionResponse\"\x00\x30\x01\x12?\n\x0c\x65xecute_test\x12\x16.execution.TestRequest\x1a\x15.execution.TestResult\"\x00\x62\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'execute_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _globals['_EXECUTEREQUEST']._serialized_start=28
  _globals['_EXECUTEREQUEST']._serialized_end=98
  _globals['_TESTREQUEST']._serialized_start=101
  _globals['_TESTREQUEST']._serialized_end=271
  _globals['_TESTRESULT']._serialized_start=273
  _globals['_TESTRESULT']._serialized_end=318
  _globals['_EXECUTIONRESPONSE']._serialized_start=320
  _globals['_EXECUTIONRESPONSE']._serialized_end=356
  _globals['_EXECUTE']._serialized_start=359
  _globals['_EXECUTE']._serialized_end=513
# @@protoc_insertion_point(module_scope)
