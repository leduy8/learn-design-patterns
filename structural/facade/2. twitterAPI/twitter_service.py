from twitter_token import RequestToken, AccessToken


class TwitterService:
    def __init__(self) -> None:
        self.access_token = None
        self.request = RequestToken()
        self.access = AccessToken()

    def connect_to_api(self, request_key):
        if self.request.check(request_key):
            self.access_token = self.request.get_access_token()            

    def _check_access(self):
        if not self.access.check(self.access_token):
            print("User hasn't have rights to use this service.")
            return False
        
        return True

    def get_tweets(self):
        if not self._check_access():
            return

        return ['tweet1', 'tweet2', 'tweet3', 'tweet4']