# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: sandbox.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\rsandbox.proto\x12\x07sandbox\"\x82\x01\n\x0eSandboxRequest\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x0b\n\x03tag\x18\x02 \x01(\t\x12\x0e\n\x06\x63onfig\x18\x03 \x01(\t\x12\x0e\n\x06images\x18\x04 \x03(\t\x12\r\n\x05\x66iles\x18\x05 \x03(\t\x12\x10\n\x08\x65nv_type\x18\x06 \x01(\t\x12\x14\n\x0cproject_name\x18\x07 \x01(\t\"\x17\n\tSbxModReq\x12\n\n\x02id\x18\x01 \x01(\t\"K\n\x13SbxCreationResponse\x12\x0f\n\x07message\x18\x01 \x01(\t\x12\x12\n\ncontainers\x18\x02 \x03(\t\x12\x0f\n\x07success\x18\x03 \x01(\x08\"\x1b\n\x08Response\x12\x0f\n\x07message\x18\x01 \x01(\t2\xc8\x01\n\x07Sandbox\x12I\n\x0e\x63reate_sandbox\x12\x17.sandbox.SandboxRequest\x1a\x1c.sandbox.SbxCreationResponse\"\x00\x12\x39\n\x0e\x64\x65lete_sandbox\x12\x12.sandbox.SbxModReq\x1a\x11.sandbox.Response\"\x00\x12\x37\n\x0cstop_sandbox\x12\x12.sandbox.SbxModReq\x1a\x11.sandbox.Response\"\x00\x62\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'sandbox_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _globals['_SANDBOXREQUEST']._serialized_start=27
  _globals['_SANDBOXREQUEST']._serialized_end=157
  _globals['_SBXMODREQ']._serialized_start=159
  _globals['_SBXMODREQ']._serialized_end=182
  _globals['_SBXCREATIONRESPONSE']._serialized_start=184
  _globals['_SBXCREATIONRESPONSE']._serialized_end=259
  _globals['_RESPONSE']._serialized_start=261
  _globals['_RESPONSE']._serialized_end=288
  _globals['_SANDBOX']._serialized_start=291
  _globals['_SANDBOX']._serialized_end=491
# @@protoc_insertion_point(module_scope)
