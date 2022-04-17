from django.shortcuts import render
from django.http import HttpResponse
from .models import Post


def posts(requset):
    posts = Post.objects.all()
    context = {'posts': posts}
    return render(requset, 'photojournal/posts.html', context)


def post(request, slug_field):
    post = Post.objects.get(slug=slug_field)
    context = {'post': post}
    return render(request, 'photojournal/single-post.html', context)
