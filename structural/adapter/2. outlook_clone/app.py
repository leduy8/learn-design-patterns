from email_client import EmailClient
from gmail_adapter import GmailAdapter

client = EmailClient()
client.add_provider(GmailAdapter())
client.download_email()