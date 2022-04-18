from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.login_user, name="login"),
    path('logout/', views.logout_user, name="logout"),
    path('register/', views.register_user, name="register"),


    path('', views.posts, name="posts"),
    path('create-post/', views.create_post, name="create-post"),
    path('update-project/<slug:slug>', views.update_post, name='update-post'),
    path('delete-project/<slug:slug>', views.delete_post, name='delete-post'),
    path('<slug:slug>/', views.post, name="single-post"),
]
