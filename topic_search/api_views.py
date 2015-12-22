from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response

from topic_search.utils import get_twitter_trend_topics, TwitterAPIQueryError
from .models import SearchTopic
from .serializers import SearchTopicSerializer


class TwitterTrendView(APIView):

    def get(self, request, format=None):

        try:
            trends = get_twitter_trend_topics()

        except TwitterAPIQueryError:
            return Response('API Search Error')

        return Response(trends, content_type='application/json')


class SearchTopicView(APIView):

    def get(self, request, format=None):

        topics = SearchTopic.objects.all().order_by('-num_of_search')[:10]
        serializer = SearchTopicSerializer(topics, many=True)
        return Response(serializer.data)

    def post(self, request):

        serializer = SearchTopicSerializer(data=request.data)
        if serializer.is_valid():
            name = serializer.validated_data['name']
            topic, created = SearchTopic.objects.get_or_create(name=name)
            topic.num_of_search += 1
            topic.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class SearchTopicLikesView(APIView):

    def get(self, request, format=None):

        topics = SearchTopic.objects.all().order_by('-likes')[:10]
        serializer = SearchTopicSerializer(topics, many=True)
        return Response(serializer.data)

    def post(self, request):

        serializer = SearchTopicSerializer(data=request.data)
        if serializer.is_valid():
            name = serializer.validated_data['name']
            topic, created = SearchTopic.objects.get_or_create(name=name)

            # handles if name is not searched before
            if created is True:
                topic.num_of_search += 1
            topic.likes += 1
            topic.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


