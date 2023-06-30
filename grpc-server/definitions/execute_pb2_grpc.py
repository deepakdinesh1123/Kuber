# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from definitions import execute_pb2 as execute__pb2


class ExecuteStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.executeCommand = channel.unary_stream(
                '/execution.Execute/executeCommand',
                request_serializer=execute__pb2.ExecuteRequest.SerializeToString,
                response_deserializer=execute__pb2.ExecutionResponse.FromString,
                )


class ExecuteServicer(object):
    """Missing associated documentation comment in .proto file."""

    def executeCommand(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_ExecuteServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'executeCommand': grpc.unary_stream_rpc_method_handler(
                    servicer.executeCommand,
                    request_deserializer=execute__pb2.ExecuteRequest.FromString,
                    response_serializer=execute__pb2.ExecutionResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'execution.Execute', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class Execute(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def executeCommand(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_stream(request, target, '/execution.Execute/executeCommand',
            execute__pb2.ExecuteRequest.SerializeToString,
            execute__pb2.ExecutionResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
