# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from definitions import retrieve_pb2 as retrieve__pb2


class DataServiceStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.RetrieveInformation = channel.unary_unary(
                '/data_service.DataService/RetrieveInformation',
                request_serializer=retrieve__pb2.RetrieveInformationRequest.SerializeToString,
                response_deserializer=retrieve__pb2.RetrieveInformationResponse.FromString,
                )


class DataServiceServicer(object):
    """Missing associated documentation comment in .proto file."""

    def RetrieveInformation(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_DataServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'RetrieveInformation': grpc.unary_unary_rpc_method_handler(
                    servicer.RetrieveInformation,
                    request_deserializer=retrieve__pb2.RetrieveInformationRequest.FromString,
                    response_serializer=retrieve__pb2.RetrieveInformationResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'data_service.DataService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class DataService(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def RetrieveInformation(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/data_service.DataService/RetrieveInformation',
            retrieve__pb2.RetrieveInformationRequest.SerializeToString,
            retrieve__pb2.RetrieveInformationResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
