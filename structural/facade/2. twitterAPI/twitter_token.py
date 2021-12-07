class RequestToken:
    def check(self, token):
        return True if token == "1234" else False

    def get_access_token(self):
        return AccessToken().get()

class AccessToken:
    def get(self):
        return "4321"

    def check(self, token):
        return True if token == "4321" else False