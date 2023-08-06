"""Handyman

Usage:
  handyman proto_gen <proto_filename>
  handyman run_server <server_type>
  handyman run_tests [--debug]
  handyman --version

Options:
  -h --help     Show this screen.
  --version     Show version.
"""


if __name__ == "__main__":
    import os
    from docopt import docopt

    from handyman.cli import proto_gen

    args = docopt(__doc__)

    if args["proto_gen"]:
        proto_filename = args["<proto_filename>"]
        if proto_filename:
            proto_gen.genrate_proto_files(proto_filename)
        else:
            print("Proto filename not provided")

    elif args["run_server"]:
        os.system("python setup.py install")
        server_type = args["<server_type>"]
        if server_type == "grpc":
            os.system("python grpc_server/server.py")
        else:
            os.system("python http_server/server.py")

    elif args["run_tests"]:
        if args["--debug"]:
            os.system("py.test --capture=no")
        else:
            os.system("py.test")
