from typing import Any, Callable
from grpc_interceptor import ClientCallDetails, ClientInterceptor

import grpc 

class MetadataClientInterceptor(ClientInterceptor):

    def __init__(self, client_id, api_key) -> None:
        super().__init__()
        self.client_id = client_id
        self.api_key = api_key

    def intercept(
        self,
        method: Callable,
        request_or_iterator: Any,
        call_details: grpc.ClientCallDetails,
    ):
        """Override this method to implement a custom interceptor.

        This method is called for all unary and streaming RPCs. The interceptor
        implementation should call `method` using a `grpc.ClientCallDetails` and the
        `request_or_iterator` object as parameters. The `request_or_iterator`
        parameter may be type checked to determine if this is a singluar request
        for unary RPCs or an iterator for client-streaming or client-server streaming
        RPCs.

        Args:
            method: A function that proceeds with the invocation by executing the next
                interceptor in the chain or invoking the actual RPC on the underlying
                channel.
            request_or_iterator: RPC request message or iterator of request messages
                for streaming requests.
            call_details: Describes an RPC to be invoked.

        Returns:
            The type of the return should match the type of the return value received
            by calling `method`. This is an object that is both a
            `Call <https://grpc.github.io/grpc/python/grpc.html#grpc.Call>`_ for the
            RPC and a `Future <https://grpc.github.io/grpc/python/grpc.html#grpc.Future>`_.

            The actual result from the RPC can be got by calling `.result()` on the
            value returned from `method`.
        """
        new_details = ClientCallDetails(
            call_details.method,
            600,
            [("client_id", self.client_id), ("api_key", self.api_key), ],
            call_details.credentials,
            call_details.wait_for_ready,
            call_details.compression,
        )

        return method(request_or_iterator, new_details)
