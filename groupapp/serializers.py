from rest_framework import serializers

from .models import CustomUser, Company


class CompanySerializer(serializers.Serializer):
    name = serializers.CharField(max_length=150)
    catchPhrase = serializers.CharField(max_length=500)
    bs = serializers.CharField(max_length=500)


class CustomUserSerializer(serializers.Serializer):
    username = serializers.CharField(max_length=100)
    phone = serializers.CharField(max_length=30)
    website = serializers.CharField(max_length=300)
    company = CompanySerializer(read_only=True)

    def create(self, validated_data):
        return CustomUser.objects.create(**validated_data)

    def update(self, customuser, validated_data):
        customuser.username = validated_data.get('username', customuser.username)
        customuser.phone = validated_data.get('phone', customuser.phone)
        customuser.website = validated_data.get('website', customuser.website)
        # customuser.company = validated_data.get('company', customuser.company)