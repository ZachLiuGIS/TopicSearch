from django.views.generic.base import TemplateView
from .utils import search_twitter_by_term, search_wiki_by_term, TwitterAPIQueryError
from geopy.geocoders import Nominatim
from .models import SearchTopic


class HomeView(TemplateView):

    template_name = 'topic_search/home.html'

    def get_context_data(self, **kwargs):
        context = super(HomeView, self).get_context_data(**kwargs)
        search_topics = SearchTopic.objects.all().order_by('-num_of_search')[:10]
        context['top_searches'] = search_topics
        liked_topics = SearchTopic.objects.all().order_by('-likes')[:10]
        context['top_likes'] = liked_topics
        return context


class AboutView(TemplateView):

    template_name = 'topic_search/about.html'

    def get_context_data(self, **kwargs):
        context = super(AboutView, self).get_context_data(**kwargs)
        return context


class SearchResultView(TemplateView):

    template_name = 'topic_search/search_result.html'

    def dispatch(self, request, *args, **kwargs):
        term = self.request.GET["term"]
        if term:
            topic, created = SearchTopic.objects.get_or_create(name=term)
            topic.num_of_search += 1
            topic.save()
        return super(SearchResultView, self).dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super(SearchResultView, self).get_context_data(**kwargs)
        context['errors'] = []

        term = self.request.GET["term"]
        geo_search = True if "geo-search" in self.request.GET else False

        context['term'] = term

        # get geo context data
        if geo_search:
            lat = self.request.GET["lat"]
            lng = self.request.GET["lng"]
            context['coordinates'] = dict(lat=lat, lng=lng)
            geolocator = Nominatim()
            location = geolocator.reverse(lat + ', ' + lng)
            if location:
                context['location'] = location

        # twitter search
        try:
            if geo_search:
                twitter_results = search_twitter_by_term(term, geo_search, lat, lng)
            else:
                twitter_results = search_twitter_by_term(term, geo_search)
            context['tweets'] = twitter_results
        except TwitterAPIQueryError:
            context['errors'].append('Twitter')

        # wiki search
        try:
            if geo_search:
                wiki_results = search_wiki_by_term(term, geo_search, lat, lng)
            else:
                wiki_results = search_wiki_by_term(term, geo_search)
            context['wikis'] = wiki_results
        except:
            context['errors'].append('Wiki')

        return context
