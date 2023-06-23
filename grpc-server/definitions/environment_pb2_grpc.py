# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from definitions import environment_pb2 as environment__pb2


class environmentStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.createEnvironment = channel.unary_stream(
                '/environment.environment/createEnvironment',
                request_serializer=environment__pb2.EnvironmentRequest.SerializeToString,
                response_deserializer=environment__pb2.EnvCreationResponse.FromString,
                )
        self.deleteEnvironment = channel.unary_unary(
                '/environment.environment/deleteEnvironment',
                request_serializer=environment__pb2.EnvModReq.SerializeToString,
                response_deserializer=environment__pb2.Response.FromString,
                )
        self.stopEnvironment = channel.unary_unary(
                '/environment.environment/stopEnvironment',
                request_serializer=environment__pb2.EnvModReq.SerializeToString,
                response_deserializer=environment__pb2.Response.FromString,
                )


class environmentServicer(object):
    """Missing associated documentation comment in .proto file."""

    def createEnvironment(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def deleteEnvironment(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def stopEnvironment(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_environmentServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'createEnvironment': grpc.unary_stream_rpc_method_handler(
                    servicer.createEnvironment,
                    request_deserializer=environment__pb2.EnvironmentRequest.FromString,
                    response_serializer=environment__pb2.EnvCreationResponse.SerializeToString,
            ),
            'deleteEnvironment': grpc.unary_unary_rpc_method_handler(
                    servicer.deleteEnvironment,
                    request_deserializer=environment__pb2.EnvModReq.FromString,
                    response_serializer=environment__pb2.Response.SerializeToString,
            ),
            'stopEnvironment': grpc.unary_unary_rpc_method_handler(
                    servicer.stopEnvironment,
                    request_deserializer=environment__pb2.EnvModReq.FromString,
                    response_serializer=environment__pb2.Response.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'environment.environment', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class environment(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def createEnvironment(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_stream(request, target, '/environment.environment/createEnvironment',
            environment__pb2.EnvironmentRequest.SerializeToString,
            environment__pb2.EnvCreationResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def deleteEnvironment(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/environment.environment/deleteEnvironment',
            environment__pb2.EnvModReq.SerializeToString,
            environment__pb2.Response.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def stopEnvironment(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/environment.environment/stopEnvironment',
            environment__pb2.EnvModReq.SerializeToString,
            environment__pb2.Response.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
