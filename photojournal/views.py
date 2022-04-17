from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Post
from .forms import PostForm


def posts(requset):
    posts = Post.objects.all()
    context = {'posts': posts}
    return render(requset, 'photojournal/posts.html', context)


def post(request, slug):
    post = Post.objects.get(slug=slug)
    context = {'post': post}
    return render(request, 'photojournal/single-post.html', context)


def createPost(request):
    form = PostForm()
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            return redirect('posts')
    context = {'form': form}
    return render(request, 'photojournal/post_form.html', context)
