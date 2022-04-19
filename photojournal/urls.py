from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.login_user, name="login"),
    path('logout/', views.logout_user, name="logout"),
    path('register/', views.register_user, name="register"),

    # path('', views.profiles, name='profiles'),
    path('profile/<int:pk>', views.user_profile, name='user-profile'),
    path('account/', views.user_account, name='account'),
    path('edit-account/', views.edit_account, name='edit-account'),

    path('', views.posts, name="posts"),
    path('create-post/', views.create_post, name="create-post"),
    path('update-post/<slug:slug>', views.update_post, name='update-post'),
    path('delete-post/<slug:slug>', views.delete_post, name='delete-post'),
    path('post-like/<slug:slug>', views.like_post, name='post-like'),
    path('<slug:slug>/', views.post, name="single-post"),
]
