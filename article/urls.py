from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static

from . import views

app_name = 'article'
urlpatterns = [
    url(r'^articles/all/$', views.articles, name='articles'),
    url(r'^articles/get/(?P<article_id>\d+)/$', views.article, name='article'),
    url(r'^articles/add_comment/(?P<article_id>\d+)/$', views.add_comment, name='add_comment'),
    url(r'^page/(\d+)/$', views.articles, name='articles'),
    url(r'^', views.articles, name='articles'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)