from django.test import TestCase
from topic_search.models import SearchTopic


class SearchTopicModelTest(TestCase):

    def test_string(self):

        topic = SearchTopic.objects.create(name='topic')
        self.assertEqual(str(topic), 'topic')
