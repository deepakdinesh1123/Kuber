# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: uptime.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x0cuptime.proto\x12\x06uptime\"\x19\n\tContainer\x12\x0c\n\x04name\x18\x01 \x01(\t\"\x1b\n\x08Response\x12\x0f\n\x07success\x18\x01 \x01(\x08\x32R\n\x0f\x43ontainerUptime\x12?\n\x14get_container_status\x12\x11.uptime.Container\x1a\x10.uptime.Response\"\x00\x30\x01\x62\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'uptime_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _globals['_CONTAINER']._serialized_start=24
  _globals['_CONTAINER']._serialized_end=49
  _globals['_RESPONSE']._serialized_start=51
  _globals['_RESPONSE']._serialized_end=78
  _globals['_CONTAINERUPTIME']._serialized_start=80
  _globals['_CONTAINERUPTIME']._serialized_end=162
# @@protoc_insertion_point(module_scope)
