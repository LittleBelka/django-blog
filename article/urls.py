from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static

from . import views

app_name = 'article'
urlpatterns = [
    url(r'^articles/all/$', views.articles, name='articles'),
    url(r'^articles/get/(?P<article_id>\d+)/$', views.article, name='article'),
    url(r'^articles/add_comment/(?P<article_id>\d+)/$', views.add_comment, name='add_comment'),
    url(r'^articles/my_articles/$', views.my_articles, name='my_articles'),
    url(r'^articles/create_article/$', views.create_article, name='create_article'),
    url(r'^articles/edit_article/(?P<article_id>\d+)/$', views.edit_article, name='edit_article'),
    url(r'^page/(\d+)/$', views.articles, name='articles'),


] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)