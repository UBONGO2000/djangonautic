from django.shortcuts import render
# Create your views here.

def home(request):
    return render(request,"index.html")


def articles_list(request):
    return render(request, "articles/articles_lists.html")