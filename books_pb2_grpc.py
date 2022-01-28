# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

import books_pb2 as books__pb2


class RecommendationsStub(object):
    """message GenreResponse
    {
    repeated BookRecommendation recommendations=1;
    }

    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.Recommend = channel.unary_unary(
                '/Recommendations/Recommend',
                request_serializer=books__pb2.GenreRequest.SerializeToString,
                response_deserializer=books__pb2.BookRecommendation.FromString,
                )


class RecommendationsServicer(object):
    """message GenreResponse
    {
    repeated BookRecommendation recommendations=1;
    }

    """

    def Recommend(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_RecommendationsServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'Recommend': grpc.unary_unary_rpc_method_handler(
                    servicer.Recommend,
                    request_deserializer=books__pb2.GenreRequest.FromString,
                    response_serializer=books__pb2.BookRecommendation.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'Recommendations', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class Recommendations(object):
    """message GenreResponse
    {
    repeated BookRecommendation recommendations=1;
    }

    """

    @staticmethod
    def Recommend(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/Recommendations/Recommend',
            books__pb2.GenreRequest.SerializeToString,
            books__pb2.BookRecommendation.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
