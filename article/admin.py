from django.contrib import admin
from article.models import Article, Comments


class ArticleInline(admin.StackedInline):
    model = Comments
    extra = 2


class ArticleAdmin(admin.ModelAdmin):
    fields = ['article_title', 'article_text', 'article_date', 'article_image', 'article_music',
              'article_video', 'article_author']
    inlines = [ArticleInline]
    list_display = ('article_title', 'article_date')
    list_filter = ['article_date']

admin.site.register(Article, ArticleAdmin)

