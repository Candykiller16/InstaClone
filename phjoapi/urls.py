from django.urls import path
from phjoapi import views

urlpatterns = [
    path('', views.get_routes),
    path('posts/', views.get_posts),
    path('posts/<int:pk>', views.get_post),
]