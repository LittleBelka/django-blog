from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Article(models.Model):

    class Meta():
        db_table = "article"
        verbose_name = "Пост"
        verbose_name_plural = "Посты"

    article_title = models.CharField(max_length=200, verbose_name=u"Заголовок")
    article_text = models.TextField(verbose_name=u"Текст")
    article_date = models.DateTimeField(verbose_name=u"Дата публикации")
    article_image = models.ImageField(upload_to='post_image', blank=True, null=True, verbose_name=u"Картинка")
    article_author = models.ForeignKey(User)


class Comments(models.Model):

    class Meta():
        db_table = "comments"
        verbose_name = "Комментарий"
        verbose_name_plural = "Комментарии"

    comments_text = models.TextField(verbose_name=u"Текст")
    comments_date = models.DateTimeField(verbose_name=u"Дата комментария")
    comments_article = models.ForeignKey(Article)
    comments_from = models.ForeignKey(User)