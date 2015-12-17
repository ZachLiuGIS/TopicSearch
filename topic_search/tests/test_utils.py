from django.test import TestCase
from ..utils import search_twitter_by_term


class TwitterSearchTest(TestCase):
    term = 'python'
    search_twitter_by_term(term)
