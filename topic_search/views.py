from django.views.generic.base import TemplateView
from .utils import search_twitter_by_term


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
        term = self.request.GET["term"]
        twitter_results = search_twitter_by_term(term)
        context['term'] = term
        context['tweets'] = twitter_results
        return context
