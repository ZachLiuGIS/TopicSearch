from django.conf.urls import patterns, url
from topic_search import views, api_views


urlpatterns = [
    url(r'^about/$', views.AboutView.as_view(), name='about'),
    url(r'^search_result/$', views.SearchResultView.as_view(), name='search_result'),
    url(r'^api/twitter_trends/$', api_views.TwitterTrendView.as_view(), name='api_twitter_trends'),
    url(r'^api/search_topics/$', api_views.SearchTopicView.as_view(), name='api_search_topics'),
    url(r'^api/search_topic_likes/$', api_views.SearchTopicLikesView.as_view(), name='api_search_topic_likes'),
]
