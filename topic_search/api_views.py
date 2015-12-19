
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response

from topic_search.utils import get_twitter_trend_topics, TwitterAPIQueryError


class TwitterTrendView(APIView):

    def get(self, request, format=None):

        try:
            trends = get_twitter_trend_topics()

        except TwitterAPIQueryError:
            return Response('API Search Error')

        return Response(trends, content_type='application/json')
