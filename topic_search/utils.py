from TwitterAPI import TwitterAPI
from .app_settings import TWITTER_API_KEYS


class TwitterItem(object):

    def __init__(self, text='', created_at='', user_name='', user_screen_name='', profile_url=''):
        self.text = text
        self.created_at = created_at
        self.user_name = user_name
        self.user_screen_name = user_screen_name
        self.profile_url = profile_url


def search_twitter_by_term(term):
    consumer_key = TWITTER_API_KEYS['consumer_key']
    consumer_secret = TWITTER_API_KEYS['consumer_secret']
    access_token_key = TWITTER_API_KEYS['access_token_key']
    access_token_secret = TWITTER_API_KEYS['access_token_secret']
    api = TwitterAPI(consumer_key, consumer_secret, access_token_key, access_token_secret)

    lang = 'en'
    count = 10

    r = list(api.request('search/tweets', {'q': term, 'lang': lang, 'count': count}))

    items = []

    for item in r:
        if 'text' in item and 'created_at' in item and 'user' in item:
            text = item['text']
            created_at = item['created_at']
            user_name = item['user']['name']
            user_screen_name = item['user']['screen_name']
            profile_url = item['user']['profile_image_url']

            item = TwitterItem(text, created_at, user_name, user_screen_name, profile_url)
            items.append(item)

    print(items)
    return items
