from django.shortcuts import render
from .models import Article

# Create your views here.

def home(request):
    return render(request,"index.html")

def articles_list(request):
    articles=Article.objects.all().order_by('date')
    return render(request, "articles/articles_lists.html",{"articles":articles})

def articles_detail(request,slug):
    article=Article.objects.get(slug=slug)
    return render(request,"articles/articles_detail.html",{"article":article})
