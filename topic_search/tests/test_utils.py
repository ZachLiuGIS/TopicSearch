from django.test import TestCase
from ..utils import search_twitter_by_term, search_wiki_by_term


class TwitterSearchTest(TestCase):

    def test_search(self):
        term = 'python'
        search_twitter_by_term(term)


class WikiSearchTest(TestCase):

    def test_search(self):
        term = 'python'
        search_wiki_by_term(term)
