from django.shortcuts import render
from django.views import generic
from articles.models import Article

class ArticleDetailView(generic.DetailView):
    model = Article
    context_object_name = 'article'
    template_name = 'pages/detail.html'

class ArticleListView(generic.ListView):
    model = Article
    context_object_name = 'articles'
    template_name = 'pages/home.html'