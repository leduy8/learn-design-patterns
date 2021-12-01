from gmail.gmail_client import GmailClient
from email_provider import EmailProvider


class GmailAdapter(EmailProvider):
    def __init__(self) -> None:
        super().__init__()
        self.gmail_client = GmailClient()

    def download_email(self):
        self.gmail_client.connect()
        self.gmail_client.get_emails()
        self.gmail_client.disconnect()