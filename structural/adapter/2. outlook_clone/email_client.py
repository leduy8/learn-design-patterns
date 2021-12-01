class EmailClient:
    def __init__(self) -> None:
        self.providers = []

    def add_provider(self, provider):
        self.providers.append(provider)

    def download_email(self):
        for provider in self.providers:
            provider.download_email()