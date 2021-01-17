from django.urls import path

from .views import PostListView


urlpatterns = [
    path('', PostListView, name='home'),
]
