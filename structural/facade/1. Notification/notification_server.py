from connection import Connection
from auth_token import AuthToken

class NotificationServer:
    def connect(self, ip_address):
        return Connection()

    def authenticate(self, app_id, key):
        return AuthToken()

    def send(self, auth_token, message, target):
        print("Sending a message.")