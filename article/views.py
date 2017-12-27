from django.shortcuts import render, redirect, get_object_or_404
from article.models import Article, Comments
from .forms import CommentForm, CreateArticleForm

from django.contrib import auth
from django.core.paginator import Paginator
import datetime


def articles(request, page_number=1):
    all_articles = Article.objects.all()
    current_page = Paginator(all_articles, 3)
    args = {}
    args['articles'] = current_page.page(page_number)
    args['username'] = auth.get_user(request).username
    return render(request, 'articles.html', args)


def article(request, article_id=1):
    comment_form = CommentForm
    args = {}
    args['article'] = Article.objects.get(id=article_id)
    args['comments'] = Comments.objects.filter(comments_article_id = article_id)
    args['form'] = comment_form
    args['username'] = auth.get_user(request).username
    return render(request, 'article.html', args)


def add_comment(request, article_id):
    if request.POST and ('pause' not in request.session):
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.comments_article = Article.objects.get(id=article_id)
            comment.comments_date = datetime.datetime.now()
            comment.comments_from = request.user
            form.save()
            request.session.set_expiry(60)
            request.session['pause'] = True
    return redirect('/articles/get/%s/' % article_id)


def my_articles(request):
    args = {}
    args['articles'] = Article.objects.filter(article_author_id=request.user.id)
    args['username'] = auth.get_user(request).username
    return render(request, 'my_articles.html', args)


def create_article(request):
    article_form = CreateArticleForm
    args = {}
    args['form'] = article_form
    args['username'] = auth.get_user(request).username
    return render(request, 'create_article.html', args)


def save_new_article(request):
    if request.POST:
        form = CreateArticleForm(request.POST, request.FILES)
        if form.is_valid():
            article = form.save(commit=False)
            article.article_date = datetime.datetime.now()
            article.article_author = request.user
            article.article_image = form.cleaned_data['article_image']
            form.save()
    return redirect('/articles/my_articles/')


def edit_article(request, article_id):
    article = get_object_or_404(Article, pk=article_id)
    author = article.article_author
    if author == request.user:
        if request.POST:
            form = CreateArticleForm(request.POST, request.FILES, instance=article)
            if form.is_valid():
                cur_article = Article.objects.get(id=article_id)
                article = form.save(commit=False)
                article.article_author = request.user
                article.article_date = cur_article.article_date
                article.article_image = form.cleaned_data['article_image']
                article.save()
                return redirect('my_articles.html')
        else:
            form = CreateArticleForm(instance=article)
        return render(request, 'create_article.html', {'form': form})
    else:
        return render(request, 'articles.html')




















