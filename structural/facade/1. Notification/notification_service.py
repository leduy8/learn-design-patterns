from notification_server import NotificationServer
from message import Message


class NotificationService:
    def send(self, message, target):
        server = NotificationServer()
        connection = server.connect("127.0.0.1")
        auth_token = server.authenticate("app id", "key")
        server.send(auth_token, Message(message), target)
        connection.disconnect()