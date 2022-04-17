from django.urls import path
from . import views

urlpatterns = [
    path('', views.posts, name="posts"),
    path('<slug:slug>/', views.post, name="single-post"),
    path('create-post/', views.createPost, name="create-post"),
]
