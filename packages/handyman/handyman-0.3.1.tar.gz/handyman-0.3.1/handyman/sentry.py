import grpc
import os
import sentry_sdk
from sentry_sdk import capture_exception

from handyman.grpc_utils import split_method_call


def init_sentry_sdk():
    sentry_dsn = os.environ.get("SENTRY_DSN")
    if sentry_dsn:
        sentry_sdk.init(sentry_dsn, traces_sample_rate=1.0)


def send_error(err):
    capture_exception(err)


class SentryServerInterceptor(grpc.ServerInterceptor):

    def __init__(self):
        pass

    def intercept_service(self, continuation, handler_call_details):
        grpc_service_name, grpc_method_name, _ = split_method_call(
            handler_call_details)

        try:
            return continuation(handler_call_details)
        except Exception() as e:
            capture_exception(e)
            raise
