from django.forms import ModelForm, ImageField, FileInput, FileField
from article.models import Comments, Article


class CommentForm(ModelForm):
    class Meta:
        model = Comments
        fields = ['comments_text', ]


class CreateArticleForm(ModelForm):

    class Meta:
        model = Article
        fields = ['article_title', 'article_text', 'article_image', 'article_music', 'article_video', ]

    article_image = ImageField(required=False,error_messages ={'invalid': "Image files only"}, widget=FileInput)
    article_music = FileField(required=False, error_messages={'invalid': "Music files only"}, widget=FileInput)
    article_video = FileField(required=False, error_messages={'invalid': "Video files only"}, widget=FileInput)