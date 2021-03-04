from django.shortcuts import render
from rest_framework import request
from rest_framework.generics import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response

from .models import Post, CustomUser
from .serializers import CustomUserSerializer, CompanySerializer


class CustomUserView(APIView):

    def get(self, request):
        customuser = CustomUser.objects.all()
        serializer = CustomUserSerializer(customuser, many=True)

        return Response({'Users': serializer.data})

    def post(self, request):
        customuser = request.data.get('customuser')
        serializer = CustomUserSerializer(data=customuser)
        if serializer.is_valid(raise_exception=True):
            customuser_saved = serializer.save()

            return Response({'success': f"customuser '{customuser_saved.username}' created successfully"})


class CustomUserIDView(APIView):
    def get_object(self, pk):
        try:
            return CustomUser.objects.get(pk=pk)
        except CustomUser.DoesNotExist:
            raise CustomUser

    def get(self, request, pk, format=None):
        user = get_object_or_404(CustomUser.objects.all(), pk=pk)
        serializer = CustomUserSerializer(user)
        return Response(serializer.data)

    def put(self, request, pk):
        customuser = get_object_or_404(CustomUser.objects.all(), pk=pk)
        data = request.data.get('customuser')
        serializer = CustomUserSerializer(instance=customuser, data=data, partial=True)
        if serializer.is_valid(raise_exception=True):
            customuser_saved = serializer.save()

            return Response({'success': f"customuser '{customuser_saved.theme}' updated successfully"})

    def delete(self, request, pk):
        customuser = get_object_or_404(CustomUser.objects.all(), pk)
        customuser.delete()

        return Response()


class Company(APIView):
    def get(self, request):
        company = Company.objects.all()
        serializer = CompanySerializer(company, many=True)

        return Response({'Company': serializer.data})


def PostListView(request):
    posts = Post.objects.all()
    return render(request, 'home.html', {'posts': posts})



