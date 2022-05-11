from django.shortcuts import render
from django.views.generic import ListView, DetailView

from .models import Article


class ArticleListView(ListView):
    context_object_name = "articles"
    paginate_by = 5
    template_name = "article_app/article_list.html"

    def get_queryset(self):
        """ only make published articles display """
        return Article.objects.filter(is_online=True)


class ArticleDetailView(DetailView):
    # if the article is not published will not be accessed
    queryset = Article.objects.filter(is_online=True)
    context_object_name = "article"
    query_pk_and_slug = True
    template_name = "article_app/article_detail.html"
