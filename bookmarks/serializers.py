from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Collection, Bookmark

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email']

class UserRegistrationSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    
    class Meta:
        model = User
        fields = ['username', 'email', 'password']
    
    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data['username'],
            email=validated_data['email'],
            password=validated_data['password']
        )
        return user

class CollectionSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='user.username')
    
    class Meta:
        model = Collection
        fields = ['id', 'name', 'description', 'user', 'created_at', 'updated_at']

class BookmarkSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='user.username')
    collection_name = serializers.ReadOnlyField(source='collection.name')
    
    class Meta:
        model = Bookmark
        fields = ['id', 'title', 'url', 'description', 'tags', 'collection', 'collection_name', 'user', 'created_at', 'updated_at']