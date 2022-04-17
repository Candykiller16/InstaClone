from django.urls import path
from . import views

urlpatterns = [
    path('', views.posts, name="posts"),
    path('create-post/', views.create_post, name="create-post"),
    path('<slug:slug>/', views.post, name="single-post"),
]
