import re
from TwitterAPI import TwitterAPI
from .app_settings import TWITTER_API_KEYS
import wikipedia


class TwitterAPIQueryError(Exception):
        pass


class WikiAPIQueryError(Exception):
        pass


def format_date(date_):
    lst = date_.split(' ')
    lst.pop(-2)
    return " ".join(lst)


def convert_links(text):
    pat_link = re.compile('(https?:\/\/.*?)(\s|$)')
    text = re.sub(pat_link, r' <a href="\1" target="_blank">\1</a> ', text)
    return text


def convert_hash_tags(text):
    pat_hash = re.compile('#(.*?)(\s|$|#)')
    text = re.sub(pat_hash, r' <a href="https://twitter.com/hashtag/\1?src=hash" target="_blank">#\1</a> ', text)
    return text


def convert_users(text):
    pat_hash = re.compile('@(.*?)(:|\s|$)')
    text = re.sub(pat_hash, r' <a href="https://twitter.com/\1" target="_blank">@\1\2</a> ', text)
    return text


def process_twitter_text(text):
    text = convert_links(text)
    text = convert_hash_tags(text)
    text = convert_users(text)
    return text


class TwitterItem(object):

    def __init__(self, text='', created_at='', user_name='', user_screen_name='', profile_url=''):
        self.text = text
        self.created_at = created_at
        self.user_name = user_name
        self.user_screen_name = user_screen_name
        self.profile_url = profile_url


class WikiItem(object):

    def __init__(self, title='', categories='', summary='', revision_id=''):
        self.title = title
        self.categories = categories
        self.summary = summary
        self.revision_id = revision_id


def search_twitter_by_term(term, geo_search=False, lat="", lng=""):
    consumer_key = TWITTER_API_KEYS['consumer_key']
    consumer_secret = TWITTER_API_KEYS['consumer_secret']
    access_token_key = TWITTER_API_KEYS['access_token_key']
    access_token_secret = TWITTER_API_KEYS['access_token_secret']
    api = TwitterAPI(consumer_key, consumer_secret, access_token_key, access_token_secret)

    lang = 'en'
    count = 10

    try:
        items = []
        options = {'q': term, 'lang': lang, 'count': count}
        if geo_search and lat and lng:
            options['geocode'] = lat + ',' + lng + ',100mi'

        r = list(api.request('search/tweets', options))

        for item in r:
            if 'text' in item and 'created_at' in item and 'user' in item:
                text = process_twitter_text(item['text'])
                created_at = format_date(item['created_at'])
                user_name = item['user']['name']
                user_screen_name = item['user']['screen_name']
                profile_url = item['user']['profile_image_url']

                item = TwitterItem(text, created_at, user_name, user_screen_name, profile_url)
                items.append(item)
    except:
        raise TwitterAPIQueryError

    return items


def search_wiki_by_term(term, geo_search=False, lat="", lng=""):
    lang = 'en'
    count = 5
    radius = 10000
    wikipedia.set_lang(lang)

    items = []
    try:
        if geo_search:
            names = wikipedia.geosearch(float(lat), float(lng), title=term, results=count, radius=radius)
        else:
            names = wikipedia.search(term, results=count)
        for name in names:
            try:
                page = wikipedia.page(name)
                wiki = WikiItem(page.title, page.categories, page.summary, page.revision_id)
                items.append(wiki)
            except wikipedia.exceptions.DisambiguationError:
                continue
        return items
    except wikipedia.exceptions.WikipediaException:
        raise WikiAPIQueryError

