from django.db import models
from django.contrib.auth.models import User


class Tags(models.Model):

    class Meta():
        db_table = "tags"
        verbose_name = "Тег"
        verbose_name_plural = "Теги"

    name = models.CharField(max_length=50, unique=True, verbose_name=u"Теги")

    def __str__(self):
        return self.name


class Article(models.Model):

    class Meta():
        db_table = "article"
        verbose_name = "Пост"
        verbose_name_plural = "Посты"

    article_title = models.CharField(max_length=200, verbose_name=u"Заголовок")
    article_text = models.TextField(verbose_name=u"Текст")
    article_date = models.DateTimeField(verbose_name=u"Дата публикации")
    article_image = models.ImageField(upload_to='post_image', blank=True, null=True, verbose_name=u"Картинка")
    article_music = models.FileField(upload_to='post_music', blank=True, null=True, verbose_name=u"Музыка")
    article_video = models.FileField(upload_to='post_video', blank=True, null=True, verbose_name=u"Видео")
    tags = models.ManyToManyField(Tags, verbose_name=u'Теги')
    article_author = models.ForeignKey(User, on_delete=models.CASCADE)


class Comments(models.Model):

    class Meta():
        db_table = "comments"
        verbose_name = "Комментарий"
        verbose_name_plural = "Комментарии"

    comments_text = models.TextField(verbose_name=u"Текст")
    comments_date = models.DateTimeField(verbose_name=u"Дата комментария")
    comments_article = models.ForeignKey(Article, on_delete=models.CASCADE)
    comments_from = models.ForeignKey(User, on_delete=models.CASCADE)