from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from articles.views import ArticleDetailView, ArticleListView

urlpatterns = [
    
    path('', ArticleListView.as_view(), name="article-list"),
    path('admin/', admin.site.urls),
    path('article/<int:pk>', ArticleDetailView.as_view(), name="article-detail"),
]
