from django.urls import path

from .views import (PostListView,
                    CustomUserView,
                    CustomUserIDView,
                    index,
                    room,
                    )


urlpatterns = [
    #path('', PostListView, name='home'),
    #path('users', CustomUserView.as_view()),
    #path('users/<int:pk>', CustomUserIDView.as_view()),
    path('', index, name='index'),
    path('<str:room_name>/', room, name='room'),
]
