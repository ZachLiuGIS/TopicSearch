from django.test import TestCase


class HomeViewTest(TestCase):

    def test_view_render_correct_template(self):
        response = self.client.get('/')
        self.assertTemplateUsed(response, 'topic_search/home.html')


class AboutViewTest(TestCase):

    def test_view_render_correct_template(self):
        response = self.client.get('/topic_search/about/')
        self.assertTemplateUsed(response, 'topic_search/about.html')


class SearchResultViewTest(TestCase):

    def test_view_render_correct_template(self):
        response = self.client.get('/topic_search/search-result/?term=text')
        self.assertTemplateUsed(response, 'topic_search/search_result.html')

    def test_can_display_twitter_result(self):
        response = self.client.get('/topic_search/search-result/?term=python')
        self.assertContains(response, "Twitter Search Result")
        self.assertContains(response, "id_twitter_result_list")
