from django.urls import path
from phjoapi import views

from rest_framework_simplejwt.views import (
    TokenVerifyView,
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    path('', views.get_routes),
    path('posts/', views.get_posts),
    path('posts/<int:pk>', views.get_post),

    path('users/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('users/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('users/token/verify/', TokenVerifyView.as_view(), name='token_verify'),
]