from django.shortcuts import render
#from rest_framework import request
from .models import Post


def PostListView(request):
    posts = Post.objects.all()
    return render(request, 'home.html', {'posts': posts})




