from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


posts = [
    {
        'title': "Blog 1",
        'author': "Ben cafer",
        'date_posted': " 2021-09-06",
        'content': "i love blog",
    }
]


def home(request):
    return render(request, 'blog/home.html', context={'posts': posts})


def about(request):
    return render(request, 'blog/about.html')