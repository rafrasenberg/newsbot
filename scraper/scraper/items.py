import scrapy

from scrapy_djangoitem import DjangoItem
from articles.models import Article

class ArticleItem(DjangoItem):
    django_model = Article
    