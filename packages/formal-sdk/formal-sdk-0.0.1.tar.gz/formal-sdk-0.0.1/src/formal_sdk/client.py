from __future__ import print_function


import grpc

# import aa_service_pb2_grpc,interceptor
from . import aa_service_pb2_grpc,interceptor


SERVER_URL = "adminv2.api.formalcloud.net"
# SERVER_URL = "localhost:8080"

class Client(object):
    """Formal Admin API Client"""

    def __init__(self, client_id, api_key):
        """Constructor.

        Args:
            client_id: Formal Client ID
            api_key: Formal API Key
        """
        
        channel = grpc.secure_channel(SERVER_URL, grpc.ssl_channel_credentials())
        interceptors = [interceptor.MetadataClientInterceptor(client_id, api_key)]
        channel = grpc.intercept_channel(channel, *interceptors)
        stub = aa_service_pb2_grpc.AdminApiServiceStub(channel)
        self.Service = stub