from twitter_service import TwitterService

service = TwitterService()
service.connect_to_api("1234")
tweets = service.get_tweets()
print(tweets)