from django.test import TestCase
from unittest.mock import patch
from topic_search.utils import search_twitter_by_term, search_wiki_by_term, format_date, \
    convert_hash_tags, convert_links, convert_users


class TwitterSearchTest(TestCase):

    def test_search(self):
        term = 'python'
        results = search_twitter_by_term(term)
        self.assertTrue(len(results) > 0)


class WikiSearchTest(TestCase):

    def test_search(self):
        term = 'python'
        results = search_wiki_by_term(term)
        self.assertTrue(len(results) > 0)


class UtilsTest(TestCase):

    def test_format_date(self):
        date_str = 'Fri Dec 18 07:16:37 +0000 2015'
        self.assertEqual(format_date(date_str), 'Fri Dec 18 07:16:37 2015')

    def test_convert_users(self):
        str_ = r"RT @chrislpenner: We've got solutions in Perl, C, Erlang, Python,Haskell, Ruby,Clojure, Rust, Scala, and Awk! https://t.co/4wtPiD7KVd"
        str_ = convert_users(str_)
        self.assertIn(r'<a href="https://twitter.com/chrislpenner" target="_blank">@chrislpenner:</a>', str_)

    def test_convert_hash_tags(self):
        str_ = r"Selenium First Steps After Only 2 Weeks Training https://t.co/o5skWlVGec #selenium #java #C #python"
        str_ = convert_hash_tags(str_)
        self.assertIn(r'<a href="https://twitter.com/hashtag/python?src=hash" target="_blank">#python</a>', str_)
        self.assertIn(r'<a href="https://twitter.com/hashtag/C?src=hash" target="_blank">#C</a>', str_)
        self.assertIn(r'<a href="https://twitter.com/hashtag/java?src=hash" target="_blank">#java</a>', str_)
        self.assertIn(r'<a href="https://twitter.com/hashtag/selenium?src=hash" target="_blank">#selenium</a>', str_)

    def test_convert_links(self):
        str_ = r"Selenium First Steps After Only 2 Weeks Training https://t.co/o5skWlVGec #selenium #java #C #python"
        str_ = convert_links(str_)
        self.assertIn(r'<a href="https://t.co/o5skWlVGec" target="_blank">https://t.co/o5skWlVGec</a>', str_)

