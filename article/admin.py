from django.contrib import admin
from article.models import Article, Comments, Tags


class ArticleInline(admin.StackedInline):
    model = Comments
    extra = 2


class ArticleAdmin(admin.ModelAdmin):
    fields = ['article_title', 'article_text', 'article_date', 'tags', 'article_image', 'article_music',
              'article_video', 'article_author']
    inlines = [ArticleInline]
    list_display = ('article_title', 'article_date')
    list_filter = ['article_date']


class TagsAdmin(admin.ModelAdmin):
    fields = ['name']
    list_display = ('name',)


admin.site.register(Article, ArticleAdmin)
admin.site.register(Tags, TagsAdmin)

