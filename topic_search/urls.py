from django.conf.urls import patterns, url
from topic_search import views


urlpatterns = [
    url(r'^about/$', views.AboutView.as_view(), name='about'),
    url(r'^search-result/$', views.SearchResultView.as_view(), name='search_result'),
]
