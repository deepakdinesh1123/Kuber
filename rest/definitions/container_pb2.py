# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: definitions/container.proto
"""Generated protocol buffer code."""
from google.protobuf import (
    descriptor as _descriptor, descriptor_pool as _descriptor_pool,
    symbol_database as _symbol_database,
)
from google.protobuf.internal import builder as _builder

# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(
    b'\n\x1b\x64\x65\x66initions/container.proto\x12\tcontainer"I\n\tContainer\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\r\n\x05image\x18\x02 \x01(\t\x12\x0f\n\x07network\x18\x03 \x01(\t\x12\x0e\n\x06\x63onfig\x18\x04 \x01(\t".\n\x10\x43ontainerCreated\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x0c\n\x04logs\x18\x03 \x01(\t"\'\n\x16\x43ontainerCreationError\x12\r\n\x05\x65rror\x18\x01 \x01(\t"\x9f\x01\n\x19\x43ontainerCreationResponse\x12\x38\n\x11\x63ontainer_created\x18\x01 \x01(\x0b\x32\x1b.container.ContainerCreatedH\x00\x12<\n\x0f\x63ontainer_error\x18\x02 \x01(\x0b\x32!.container.ContainerCreationErrorH\x00\x42\n\n\x08response2_\n\nContainers\x12Q\n\x0f\x63reateContainer\x12\x14.container.Container\x1a$.container.ContainerCreationResponse"\x00\x30\x01\x42\rZ\x0b./containerb\x06proto3'
)

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(
    DESCRIPTOR, "definitions.container_pb2", globals()
)
if _descriptor._USE_C_DESCRIPTORS == False:
    DESCRIPTOR._options = None
    DESCRIPTOR._serialized_options = b"Z\013./container"
    _CONTAINER._serialized_start = 42
    _CONTAINER._serialized_end = 115
    _CONTAINERCREATED._serialized_start = 117
    _CONTAINERCREATED._serialized_end = 163
    _CONTAINERCREATIONERROR._serialized_start = 165
    _CONTAINERCREATIONERROR._serialized_end = 204
    _CONTAINERCREATIONRESPONSE._serialized_start = 207
    _CONTAINERCREATIONRESPONSE._serialized_end = 366
    _CONTAINERS._serialized_start = 368
    _CONTAINERS._serialized_end = 463
# @@protoc_insertion_point(module_scope)
