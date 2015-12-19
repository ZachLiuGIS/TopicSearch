from django.views.generic.base import TemplateView
from .utils import search_twitter_by_term, search_wiki_by_term, TwitterAPIQueryError
from geopy.geocoders import Nominatim


class HomeView(TemplateView):

    template_name = 'topic_search/home.html'

    def get_context_data(self, **kwargs):
        context = super(HomeView, self).get_context_data(**kwargs)
        return context


class AboutView(TemplateView):

    template_name = 'topic_search/about.html'

    def get_context_data(self, **kwargs):
        context = super(AboutView, self).get_context_data(**kwargs)
        return context


class SearchResultView(TemplateView):

    template_name = 'topic_search/search_result.html'

    def get_context_data(self, **kwargs):
        context = super(SearchResultView, self).get_context_data(**kwargs)
        context['errors'] = []

        term = self.request.GET["term"]
        geo_search = True if "geo-search" in self.request.GET else False

        if geo_search:
            lat = self.request.GET["lat"]
            lng = self.request.GET["lng"]
            context['coordinates'] = dict(lat=lat, lng=lng)
            geolocator = Nominatim()
            location = geolocator.reverse(lat + ', ' + lng)
            if location:
                context['location'] = location

        try:
            if geo_search:
                twitter_results = search_twitter_by_term(term, geo_search, lat, lng)
            else:
                twitter_results = search_twitter_by_term(term, geo_search)
            context['tweets'] = twitter_results
        except TwitterAPIQueryError:
            context['errors'].append('Twitter')

        context['term'] = term

        try:
            if geo_search:
                wiki_results = search_wiki_by_term(term, geo_search, lat, lng)
            else:
                wiki_results = search_wiki_by_term(term, geo_search)
            context['wikis'] = wiki_results
        except:
            context['errors'].append('Wiki')

        return context
