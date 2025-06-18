import grpc
from concurrent import futures
import contextlib
import _credentials

# import generated code
import auth_pb2_grpc

# import our modules
from auth.interceptor import AuthInterceptor
from auth.service import AuthService
from patient.service import PatientService
#from data.service import DataService

_LISTEN_ADDRESS_TEMPLATE = "localhost:%d"


@contextlib.contextmanager
def run_server(port):
    # Bind interceptor to server
    server = grpc.server(
        futures.ThreadPoolExecutor(),
        interceptors=(AuthInterceptor(),),
    )
    auth_pb2_grpc.add_AuthServiceServicer_to_server(AuthService(), server)

    # Loading credentials
    server_credentials = grpc.ssl_server_credentials(
        (
            (
                _credentials.SERVER_CERTIFICATE_KEY,
                _credentials.SERVER_CERTIFICATE,
            ),
        )
    )

    # Pass down credentials
    port = server.add_secure_port(
        _LISTEN_ADDRESS_TEMPLATE % port, server_credentials
    )

    server.start()
    try:
        yield server, port
    finally:
        server.stop(0)


def serve():
    print("Starting server...")
    with run_server(50051) as (server, port):
        server.wait_for_termination()



if __name__ == "__main__":
    serve()

