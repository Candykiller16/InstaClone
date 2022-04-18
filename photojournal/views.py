from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect, get_object_or_404
from .models import Post, User
from .forms import PostForm, CustomUserCreationForm


def login_user(request):
    page = 'login'
    if request.user.is_authenticated:
        return redirect('posts')

    if request.method == 'POST':
        username = request.POST['username'].lower()
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect(request.GET['next'] if 'next' in request.GET else 'posts')
        else:
            messages.error(request, 'Username or password incorrect')

    return render(request, 'photojournal/login_register.html')


#
#
def logout_user(request):
    logout(request)
    messages.info(request, 'User was successfully logged out')
    return redirect('login')


def register_user(request):
    page = 'register'
    form = CustomUserCreationForm()

    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()

            messages.success(request, 'User account was successfully registered')

            login(request, user)
            return redirect('posts')

        else:
            messages.error(request, 'User has occured an error during creating profile')

    context = {'page': page, 'form': form}
    return render(request, 'photojournal/login_register.html', context)


def posts(requset):
    posts = Post.objects.all()
    context = {'posts': posts}
    return render(requset, 'photojournal/posts.html', context)


def post(request, slug):
    post = get_object_or_404(Post, slug=slug)
    context = {'post': post}
    return render(request, 'photojournal/single-post.html', context)


def create_post(request):
    form = PostForm()
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            return redirect('posts')

    context = {'form': form}
    return render(request, 'photojournal/post_form.html', context)


def update_post(request, slug):
    post = Post.objects.get(slug=slug)
    form = PostForm(instance=post)
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            form.save()
            return redirect('posts')

    context = {'form': form}
    return render(request, 'photojournal/post_form.html', context)


def delete_post(request, slug):
    post = Post.objects.get(slug=slug)
    if request.method == 'POST':
        post.delete()
        return redirect('posts')
    context = {'object': post}
    return render(request, 'delete_template.html', context)
