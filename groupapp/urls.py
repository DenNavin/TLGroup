from django.urls import path

from .views import PostListView, CustomUserView, CustomUserIDView


urlpatterns = [
    path('', PostListView, name='home'),
    path('users', CustomUserView.as_view()),
    path('users/<int:pk>', CustomUserIDView.as_view())
]
