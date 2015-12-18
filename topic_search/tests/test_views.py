from django.test import TestCase
from unittest.mock import patch
from datetime import datetime
from topic_search.utils import TwitterItem, WikiItem, TwitterAPIQueryError, WikiAPIQueryError


class HomeViewTest(TestCase):

    def test_view_render_correct_template(self):
        response = self.client.get('/')
        self.assertTemplateUsed(response, 'topic_search/home.html')


class AboutViewTest(TestCase):

    def test_view_render_correct_template(self):
        response = self.client.get('/topic_search/about/')
        self.assertTemplateUsed(response, 'topic_search/about.html')


class SearchResultViewTest(TestCase):

    @patch('topic_search.views.search_twitter_by_term')
    @patch('topic_search.views.search_wiki_by_term')
    def test_view_render_correct_template(self, mock_search_wiki_by_term, mock_search_twitter_by_term):
        items = []
        mock_search_twitter_by_term.return_value = items

        wikis = []
        mock_search_wiki_by_term.return_value = wikis

        response = self.client.get('/topic_search/search_result/?term=text')
        self.assertTemplateUsed(response, 'topic_search/search_result.html')

    @patch('topic_search.views.search_twitter_by_term')
    @patch('topic_search.views.search_wiki_by_term')
    def test_can_display_twitter_result(self, mock_search_wiki_by_term, mock_search_twitter_by_term):

        items = []
        for i in range(1, 11):
            items.append(TwitterItem(
                text='python ' + str(i),
                created_at=datetime.now(),
                user_name='user_' + str(i),
                user_screen_name='screenname_' + str(i),
                profile_url='url_' + str(i)
            ))
        mock_search_twitter_by_term.return_value = items

        wikis = []
        mock_search_wiki_by_term.return_value = wikis

        response = self.client.get('/topic_search/search_result/?term=python')
        self.assertContains(response, "Twitter Search Result")
        self.assertContains(response, "id_twitter_result_list")
        self.assertContains(response, "user_10")

    @patch('topic_search.views.search_twitter_by_term')
    @patch('topic_search.views.search_wiki_by_term')
    def test_can_display_twitter_result_return_empty_results(self, mock_search_wiki_by_term, mock_search_twitter_by_term):

        items = []
        mock_search_twitter_by_term.return_value = items

        wikis = []
        mock_search_wiki_by_term.return_value = wikis

        response = self.client.get('/topic_search/search_result/?term=python')
        self.assertContains(response, "Twitter Search Result")
        self.assertNotContains(response, "id_twitter_result_list")
        self.assertContains(response, "Sorry, no tweets are found for this topic.")

    @patch('topic_search.views.search_twitter_by_term')
    @patch('topic_search.views.search_wiki_by_term')
    def test_can_display_twitter_handles_error(self, mock_search_wiki_by_term, mock_search_twitter_by_term):

        e = TwitterAPIQueryError()
        mock_search_twitter_by_term.side_effect = e

        wikis = []
        mock_search_wiki_by_term.return_value = wikis

        response = self.client.get('/topic_search/search_result/?term=python')
        self.assertContains(response, "Twitter Search Result")
        self.assertNotContains(response, "id_twitter_result_list")
        self.assertContains(response, "Sorry, something is wrong with twitter search")

    @patch('topic_search.views.search_twitter_by_term')
    @patch('topic_search.views.search_wiki_by_term')
    def test_can_display_wiki_result(self, mock_search_wiki_by_term, mock_search_twitter_by_term):

        wikis = []
        for i in range(1, 6):
            wikis.append(WikiItem(
                title='title_' + str(i),
                categories='categories_' + str(i),
                summary='summary_' + str(i),
                revision_id='revision_id_' + str(i)
            ))

        mock_search_wiki_by_term.return_value = wikis

        items = []
        mock_search_twitter_by_term.return_value = items

        response = self.client.get('/topic_search/search_result/?term=python')
        self.assertContains(response, "Wiki Search Result")
        self.assertContains(response, "id_wiki_result_list")
        self.assertContains(response, "title_4")

