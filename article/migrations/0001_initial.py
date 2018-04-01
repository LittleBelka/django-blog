# Generated by Django 2.0.3 on 2018-03-31 20:44

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('article_title', models.CharField(max_length=200, verbose_name='Заголовок')),
                ('article_text', models.TextField(verbose_name='Текст')),
                ('article_date', models.DateTimeField(verbose_name='Дата публикации')),
                ('article_image', models.ImageField(blank=True, null=True, upload_to='post_image', verbose_name='Картинка')),
                ('article_music', models.FileField(blank=True, null=True, upload_to='post_music', verbose_name='Музыка')),
                ('article_video', models.FileField(blank=True, null=True, upload_to='post_video', verbose_name='Видео')),
                ('article_author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'article',
                'verbose_name': 'Пост',
                'verbose_name_plural': 'Посты',
            },
        ),
        migrations.CreateModel(
            name='Comments',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comments_text', models.TextField(verbose_name='Текст')),
                ('comments_date', models.DateTimeField(verbose_name='Дата комментария')),
                ('comments_article', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='article.Article')),
                ('comments_from', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'comments',
                'verbose_name': 'Комментарий',
                'verbose_name_plural': 'Комментарии',
            },
        ),
        migrations.CreateModel(
            name='Tags',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, unique=True, verbose_name='Теги')),
            ],
            options={
                'db_table': 'tags',
            },
        ),
        migrations.AddField(
            model_name='article',
            name='tags',
            field=models.ManyToManyField(related_name='tags', related_query_name='tag', to='article.Tags', verbose_name='Теги'),
        ),
    ]
