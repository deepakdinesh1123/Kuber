# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from definitions import sandbox_pb2 as sandbox__pb2


class SandboxStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.create_sandbox = channel.unary_unary(
                '/sandbox.Sandbox/create_sandbox',
                request_serializer=sandbox__pb2.SandboxRequest.SerializeToString,
                response_deserializer=sandbox__pb2.SbxCreationResponse.FromString,
                )
        self.delete_sandbox = channel.unary_unary(
                '/sandbox.Sandbox/delete_sandbox',
                request_serializer=sandbox__pb2.SbxModReq.SerializeToString,
                response_deserializer=sandbox__pb2.Response.FromString,
                )
        self.stop_sandbox = channel.unary_unary(
                '/sandbox.Sandbox/stop_sandbox',
                request_serializer=sandbox__pb2.SbxModReq.SerializeToString,
                response_deserializer=sandbox__pb2.Response.FromString,
                )


class SandboxServicer(object):
    """Missing associated documentation comment in .proto file."""

    def create_sandbox(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def delete_sandbox(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def stop_sandbox(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_SandboxServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'create_sandbox': grpc.unary_unary_rpc_method_handler(
                    servicer.create_sandbox,
                    request_deserializer=sandbox__pb2.SandboxRequest.FromString,
                    response_serializer=sandbox__pb2.SbxCreationResponse.SerializeToString,
            ),
            'delete_sandbox': grpc.unary_unary_rpc_method_handler(
                    servicer.delete_sandbox,
                    request_deserializer=sandbox__pb2.SbxModReq.FromString,
                    response_serializer=sandbox__pb2.Response.SerializeToString,
            ),
            'stop_sandbox': grpc.unary_unary_rpc_method_handler(
                    servicer.stop_sandbox,
                    request_deserializer=sandbox__pb2.SbxModReq.FromString,
                    response_serializer=sandbox__pb2.Response.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'sandbox.Sandbox', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class Sandbox(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def create_sandbox(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/sandbox.Sandbox/create_sandbox',
            sandbox__pb2.SandboxRequest.SerializeToString,
            sandbox__pb2.SbxCreationResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def delete_sandbox(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/sandbox.Sandbox/delete_sandbox',
            sandbox__pb2.SbxModReq.SerializeToString,
            sandbox__pb2.Response.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def stop_sandbox(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/sandbox.Sandbox/stop_sandbox',
            sandbox__pb2.SbxModReq.SerializeToString,
            sandbox__pb2.Response.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
