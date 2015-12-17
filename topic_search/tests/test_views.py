from django.test import TestCase


class HomeViewTest(TestCase):

    def test_view_render_correct_template(self):
        response = self.client.get('/')
        self.assertTemplateUsed(response, 'topic_search/home.html')


class AboutViewTest(TestCase):

    def test_view_render_correct_template(self):
        response = self.client.get('/topic_search/about/')
        self.assertTemplateUsed(response, 'topic_search/about.html')
