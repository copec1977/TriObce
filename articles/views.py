from django.shortcuts import render, get_object_or_404, redirect
from .models import Article
from .forms import ArticleForm, ActivityForm


def index(request):
    articles = Article.objects.all()
    return render(request, 'index.html', {'articles': articles})


def article_detail(request, pk):
    article = get_object_or_404(Article, pk=pk)
    if request.method == 'POST':
        form = ActivityForm(request.POST, request.FILES)
        if form.is_valid():
            activity = form.save(commit=False)
            activity.article = article
            activity.save()
            return redirect('article_detail', pk=pk)
    else:
        form = ActivityForm()
    return render(request, 'article_detail.html', {'article': article, 'form': form})


def add_article(request):
    if request.method == 'POST':
        form = ArticleForm(request.POST)
        if form.is_valid():
            article = form.save()
            return redirect('article_detail', pk=article.pk)
    else:
        form = ArticleForm()
    return render(request, 'add_article.html', {'form': form})
