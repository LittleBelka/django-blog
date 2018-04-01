from django.shortcuts import render, redirect, get_object_or_404
from article.models import Article, Comments, Tags
from .forms import CommentForm, CreateArticleForm

from django.contrib import auth
from django.core.paginator import Paginator
from django.http import JsonResponse
import datetime


def articles(request, page_number=1):
    all_articles = Article.objects.all().order_by('-article_date')
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


def calendar_info(request):
    articles = Article.objects.all().values('article_date', 'article_title', 'id')
    articles_list = list(articles)
    data = []
    for article in articles_list:
        data.append([
            '{dt.day}/{dt.month}/{dt.year}'.format(dt=article['article_date']),
            article['article_title'],
            '/articles/article/' + str(article['id']),
            '#0BA1BF'
        ])
    return JsonResponse(data, safe=False)


def one_article(request, pk):
    one_date = get_object_or_404(Article, pk=pk).article_date
    args = {}
    args['username'] = auth.get_user(request).username
    args['articles'] = Article.objects.filter(article_date=one_date)
    args['tags'] = Tags.objects.all()
    print("in one article")
    return render(request, 'my_articles.html', args)


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
    args['articles'] = Article.objects.filter(article_author_id=request.user.id).order_by('-article_date')
    args['username'] = auth.get_user(request).username
    args['tags'] = Tags.objects.all()
    return render(request, 'my_articles.html', args)


def tags(request, pk):
    args = {}
    args['tags'] = Tags.objects.all()
    args['articles'] = Article.objects.filter(tags=pk).order_by('-article_date')
    args['username'] = auth.get_user(request).username
    return render(request, 'my_articles.html', args)


def create_article(request):
    args = {}
    args['username'] = auth.get_user(request).username
    if request.POST:
        form = CreateArticleForm(request.POST, request.FILES)
        if form.is_valid():
            # tag = Tags.objects.filter(name=form.data['tags']).first()
            # print("in create_article tag: ", tag)
            article = form.save(commit=False)
            # article.tags.set(tag)
            article.article_date = datetime.datetime.now()
            article.article_author = request.user
            article.article_image = form.cleaned_data['article_image']
            article.article_music = form.cleaned_data['article_music']
            article.article_video = form.cleaned_data['article_video']
            form.save()
            return redirect('/articles/my_articles/')
        else:
            print("form is not valid")
    else:
        form = CreateArticleForm()
        args['form'] = form
        args['tags'] = Tags.objects.all().values_list('name', flat=True)
        print("Tags: ", args['tags'].values_list('name', flat=True))
    return render(request, 'create_article.html', args)


def edit_article(request, article_id):
    article = get_object_or_404(Article, pk=article_id)
    author = article.article_author
    if author == request.user:
        args = {}
        if request.POST:
            form = CreateArticleForm(request.POST, request.FILES, instance=article)
            if form.is_valid():
                print(" form article.tags: ", form.cleaned_data['tags'])
                cur_article = Article.objects.get(id=article_id)
                article = form.save(commit=False)
                article.tags.set(form.cleaned_data['tags'])
                article.article_author = request.user
                article.article_date = cur_article.article_date
                article.article_image = form.cleaned_data['article_image']
                article.article_music = form.cleaned_data['article_music']
                article.article_video = form.cleaned_data['article_video']
                article.save()
                return redirect('/articles/my_articles/')
        else:
            form = CreateArticleForm(instance=article)
            args = {'form': form, 'username': auth.get_user(request).username,'tags': Tags.objects.all()}
        return render(request, 'create_article.html', args)
    else:
        return render(request, 'articles.html')




















