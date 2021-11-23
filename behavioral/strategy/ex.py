from abc import ABC, abstractmethod


class Encryption(ABC):
    @abstractmethod
    def encrypt(self, message):
        pass


class DesEncryption(Encryption):
    def encrypt(self, message):
        return f'[DES Encrypted] aaaaaaa{message}zzzzzzz'


class AesEncryption(Encryption):
    def encrypt(self, message):
        return f'[AES Encrypted] bbbbbbb{message}yyyyyyy'


class ChatClient:
    def send_message(self, message, encryption_algo):
        message = encryption_algo.encrypt(message)
        print(message)


client = ChatClient()
client.send_message('Hello', DesEncryption())
client.send_message('World', AesEncryption())