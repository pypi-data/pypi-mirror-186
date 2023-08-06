
def split_method_call(handler_call_details):
    """
    Infers the grpc service and method name from the handler_call_details.
    """

    # e.g. /package.ServiceName/MethodName
    parts = handler_call_details.method.split("/")
    if len(parts) < 3:
        return "", "", False

    grpc_service_name, grpc_method_name = parts[1:3]
    return grpc_service_name, grpc_method_name, True