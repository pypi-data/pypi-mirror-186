import os

from grpc_tools import protoc

def genrate_proto_files(proto_filename):
    PROTO_NAME = proto_filename.split("/")[-1]
    SERVER_DIR = os.getcwd()

    protoc.main(
        (
            "",
            "--proto_path={}".format(os.path.join(SERVER_DIR, "protos", "")),
            "--python_out={}".format(os.path.join(SERVER_DIR, "protos", "")),
            "--grpc_python_out={}".format(os.path.join(SERVER_DIR, "protos", "")),
            "{}".format(PROTO_NAME),
        )
    )

    proto_ltr = PROTO_NAME.split(".proto")[0].lower()

    service_pb2 = proto_ltr + "_pb2"
    service_pb2_grpc = proto_ltr + "_pb2_grpc.py"
    file_path = SERVER_DIR + "/protos/" + service_pb2_grpc

    with open(file_path, "r") as _file:
        data = _file.read()

    data = data.replace("import " + service_pb2, "import protos." + service_pb2)

    with open(file_path, "w") as _file:
        _file.write(data)
