import grpc
from . import _credentials

class GRPCConnectionManager:
    _instance = None
    HOST = "localhost:50051"

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(GRPCConnectionManager, cls).__new__(cls)
            cls._instance.token = "unauthorised"
            cls._instance.channel = None
            cls._instance._update_channel()
        return cls._instance

    def _update_channel(self):
        """Update the channel with current token"""
        if self.channel:
            self.channel.close()  # Close existing channel
        
        call_credentials = grpc.access_token_call_credentials(self.token)
        channel_credentials = grpc.ssl_channel_credentials(_credentials.ROOT_CERTIFICATE)
        composite_credentials = grpc.composite_channel_credentials(channel_credentials, call_credentials)
        self.channel = grpc.secure_channel(self.HOST, composite_credentials)

    def set_token(self, token: str):
        """Set authentication token and update all connections"""
        self.token = token
        self._update_channel()

    def get_channel(self):
        return self.channel

    def get_stub(self, stub_class):
        return stub_class(self.get_channel())

    def close(self):
        """Clean up the channel"""
        if self.channel:
            self.channel.close()
