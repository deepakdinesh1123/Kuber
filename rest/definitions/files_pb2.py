# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: definitions/files.proto
"""Generated protocol buffer code."""
from google.protobuf import (
    descriptor as _descriptor, descriptor_pool as _descriptor_pool,
    symbol_database as _symbol_database,
)
from google.protobuf.internal import builder as _builder

# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(
    b'\n\x17\x64\x65\x66initions/files.proto\x12\x05\x66iles""\n\x04\x46ile\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x0c\n\x04path\x18\x02 \x01(\t";\n\x0b\x46ilesToCopy\x12\x11\n\tcontainer\x18\x01 \x01(\t\x12\x19\n\x04\x66ile\x18\x02 \x03(\x0b\x32\x0b.files.File"\x1f\n\x0c\x43opyResponse\x12\x0f\n\x07success\x18\x01 \x01(\x08\x32L\n\x05\x46iles\x12\x43\n\x14\x63opyFilesToContainer\x12\x12.files.FilesToCopy\x1a\x13.files.CopyResponse"\x00(\x01\x62\x06proto3'
)

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, "definitions.files_pb2", globals())
if _descriptor._USE_C_DESCRIPTORS == False:
    DESCRIPTOR._options = None
    _FILE._serialized_start = 34
    _FILE._serialized_end = 68
    _FILESTOCOPY._serialized_start = 70
    _FILESTOCOPY._serialized_end = 129
    _COPYRESPONSE._serialized_start = 131
    _COPYRESPONSE._serialized_end = 162
    _FILES._serialized_start = 164
    _FILES._serialized_end = 240
# @@protoc_insertion_point(module_scope)
