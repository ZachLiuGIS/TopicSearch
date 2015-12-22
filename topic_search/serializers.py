from rest_framework import serializers
from .models import SearchTopic


class SearchTopicSerializer(serializers.ModelSerializer):

    class Meta:
        model = SearchTopic
        fields = ('name', 'likes', 'num_of_search')
        read_only_fields = ('likes', 'num_of_search',)


