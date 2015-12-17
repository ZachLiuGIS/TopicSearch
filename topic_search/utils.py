from TwitterAPI import TwitterAPI
from .app_settings import TWITTER_API_KEYS


def search_twitter_by_term(term):
    consumer_key = TWITTER_API_KEYS['consumer_key']
    consumer_secret = TWITTER_API_KEYS['consumer_secret']
    access_token_key = TWITTER_API_KEYS['access_token_key']
    access_token_secret = TWITTER_API_KEYS['access_token_secret']
    api = TwitterAPI(consumer_key, consumer_secret, access_token_key, access_token_secret)

    r = list(api.request('search/tweets', {'q': term}))

    for item in r:
        print(item['text'] if 'text' in item else item)
        print()
        print()
