from timeit import default_timer

import grpc
from prometheus_client import Histogram, Counter
from prometheus_client.registry import REGISTRY

from handyman.grpc_utils import split_method_call

DEFAULT_PROMETHEUS_PORT = 8003
UNARY = "UNARY"
SERVER_STREAMING = "SERVER_STREAMING"
CLIENT_STREAMING = "CLIENT_STREAMING"
BIDI_STREAMING = "BIDI_STREAMING"
UNKNOWN = "UNKNOWN"


def wrap_iterator_inc_counter(iterator, counter, grpc_type, grpc_service_name, grpc_method_name):
    """Wraps an iterator and collect metrics."""

    for item in iterator:
        counter.labels(
            grpc_type=grpc_type,
            grpc_service=grpc_service_name,
            grpc_method=grpc_method_name).inc()
        yield item


def get_method_type(request_streaming, response_streaming):
    """
    Infers the method type from if the request or the response is streaming.
    # The Method type is coming from:
    # https://grpc.io/grpc-java/javadoc/io/grpc/MethodDescriptor.MethodType.html
    """
    if request_streaming and response_streaming:
        return BIDI_STREAMING
    elif request_streaming and not response_streaming:
        return CLIENT_STREAMING
    elif not request_streaming and response_streaming:
        return SERVER_STREAMING
    return UNARY


def init_grpc_metrics(registry):
    return {
        "grpc_server_started_counter": Counter(
            "v8r_grpc_started_total",
            "Total number of RPCs started on the server",
            ["grpc_type", "grpc_service", "grpc_method"],
            registry=registry
        ),
        "grpc_server_stream_msg_received": Counter(
            "v8r_grpc_msg_received_total",
            "Total number of RPC stream messages received on the server",
            ["grpc_type", "grpc_service", "grpc_method"],
            registry=registry
        ),
        "grpc_server_stream_msg_sent": Counter(
            "v8r_grpc_msg_sent_total",
            "Total number of gRPC stream messages sent by the server",
            ["grpc_type", "grpc_service", "grpc_method"],
            registry=registry
        ),
        "grpc_server_handled_histogram": Histogram(
            "v8r_grpc_handling_seconds",
            "Histogram of response latency (seconds) of gRPC that had been application-level handled by the server",
            ["grpc_type", "grpc_service", "grpc_method"],
            registry=registry
        ),
        "grpc_server_handled_total": Counter(
            "v8r_grpc_handled_total",
            "Total number of RPCs completed on the server, regardless of success or failure",
            ["grpc_type", "grpc_service", "grpc_method", "grpc_code"],
            registry=registry
        )
    }


class PromGrpcServerInterceptor(grpc.ServerInterceptor):

    def __init__(self,
                 skip_exceptions=False,
                 registry=REGISTRY):
        self._metrics = init_grpc_metrics(registry)
        self._skip_exceptions = skip_exceptions

    def intercept_service(self, continuation, handler_call_details):
        """
        Intercepts the server function calls.
        This implements referred to:
        https://github.com/census-instrumentation/opencensus-python/blob/master/opencensus/
        trace/ext/grpc/server_interceptor.py
        and
        https://grpc.io/grpc/python/grpc.html#service-side-interceptor
        """

        grpc_service_name, grpc_method_name, _ = split_method_call(
            handler_call_details)

        def metrics_wrapper(behavior, request_streaming, response_streaming):
            def new_behavior(request_or_iterator, servicer_context):
                response_or_iterator = None
                try:
                    start = default_timer()
                    grpc_type = get_method_type(
                        request_streaming, response_streaming)
                    try:
                        if request_streaming:
                            request_or_iterator = wrap_iterator_inc_counter(
                                request_or_iterator,
                                self._metrics["grpc_server_stream_msg_received"],
                                grpc_type,
                                grpc_service_name,
                                grpc_method_name)
                        else:
                            self._metrics["grpc_server_started_counter"].labels(
                                grpc_type=grpc_type,
                                grpc_service=grpc_service_name,
                                grpc_method=grpc_method_name).inc()

                        # Invoke the original rpc behavior.
                        response_or_iterator = behavior(
                            request_or_iterator, servicer_context)

                        if response_streaming:
                            sent_metric = self._metrics["grpc_server_stream_msg_sent"]
                            response_or_iterator = wrap_iterator_inc_counter(
                                response_or_iterator,
                                sent_metric,
                                grpc_type,
                                grpc_service_name,
                                grpc_method_name)

                        else:
                            self.increase_grpc_server_handled_total_counter(grpc_type,
                                                                            grpc_service_name,
                                                                            grpc_method_name,
                                                                            self._compute_status_code(
                                                                                servicer_context).name)
                        return response_or_iterator
                    except grpc.RpcError as e:
                        self.increase_grpc_server_handled_total_counter(grpc_type,
                                                                        grpc_service_name,
                                                                        grpc_method_name,
                                                                        self._compute_error_code(e).name)
                        raise e

                    finally:

                        if not response_streaming:
                            self._metrics["grpc_server_handled_histogram"].labels(
                                grpc_type=grpc_type,
                                grpc_service=grpc_service_name,
                                grpc_method=grpc_method_name) \
                                .observe(max(default_timer() - start, 0))
                except Exception as e:  # pylint: disable=broad-except
                    # Allow user to skip the exceptions in order to maintain
                    # the basic functionality in the server
                    # The logging function in exception can be toggled with log_exceptions
                    # in order to suppress the noise in logging
                    if self._skip_exceptions:
                        if response_or_iterator is None:
                            return response_or_iterator
                        return behavior(request_or_iterator, servicer_context)
                    raise e

            return new_behavior

        optional_any = self._wrap_rpc_behavior(
            continuation(handler_call_details), metrics_wrapper)

        return optional_any

    # pylint: disable=protected-access
    def _compute_status_code(self, servicer_context):
        if servicer_context._state.client == "cancelled":
            return grpc.StatusCode.CANCELLED

        if servicer_context._state.code is None:
            return grpc.StatusCode.OK

        return servicer_context._state.code

    def _compute_error_code(self, grpc_exception):
        if isinstance(grpc_exception, grpc.Call):
            return grpc_exception.code()

        return grpc.StatusCode.UNKNOWN

    def increase_grpc_server_handled_total_counter(
            self, grpc_type, grpc_service_name, grpc_method_name, grpc_code):
        self._metrics["grpc_server_handled_total"].labels(
            grpc_type=grpc_type,
            grpc_service=grpc_service_name,
            grpc_method=grpc_method_name,
            grpc_code=grpc_code).inc()

    def _wrap_rpc_behavior(self, handler, fn):
        """Returns a new rpc handler that wraps the given function"""
        if handler is None:
            return None

        if handler.request_streaming and handler.response_streaming:
            behavior_fn = handler.stream_stream
            handler_factory = grpc.stream_stream_rpc_method_handler
        elif handler.request_streaming and not handler.response_streaming:
            behavior_fn = handler.stream_unary
            handler_factory = grpc.stream_unary_rpc_method_handler
        elif not handler.request_streaming and handler.response_streaming:
            behavior_fn = handler.unary_stream
            handler_factory = grpc.unary_stream_rpc_method_handler
        else:
            behavior_fn = handler.unary_unary
            handler_factory = grpc.unary_unary_rpc_method_handler

        return handler_factory(
            fn(behavior_fn, handler.request_streaming, handler.response_streaming),
            request_deserializer=handler.request_deserializer,
            response_serializer=handler.response_serializer)
