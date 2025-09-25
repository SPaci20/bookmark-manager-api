from rest_framework import status, generics, permissions
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from .models import Collection, Bookmark
from .serializers import UserSerializer, UserRegistrationSerializer, CollectionSerializer, BookmarkSerializer
from .permissions import IsOwner

@api_view(['POST'])
@permission_classes([permissions.AllowAny])
def register(request):
    serializer = UserRegistrationSerializer(data=request.data)
    if serializer.is_valid():
        user = serializer.save()
        refresh = RefreshToken.for_user(user)
        return Response({
            'user': UserSerializer(user).data,
            'refresh': str(refresh),
            'access': str(refresh.access_token),
        }, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
@permission_classes([permissions.AllowAny])
def login(request):
    username = request.data.get('username')
    password = request.data.get('password')
    
    user = authenticate(username=username, password=password)
    if user:
        refresh = RefreshToken.for_user(user)
        return Response({
            'user': UserSerializer(user).data,
            'refresh': str(refresh),
            'access': str(refresh.access_token),
        })
    return Response({'error': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)

@api_view(['GET'])
def profile(request):
    serializer = UserSerializer(request.user)
    return Response(serializer.data)

# Collection Views
class CollectionListCreateView(generics.ListCreateAPIView):
    serializer_class = CollectionSerializer
    permission_classes = [permissions.IsAuthenticated]
    
    def get_queryset(self):
        return Collection.objects.filter(user=self.request.user)
    
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class CollectionDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = CollectionSerializer
    permission_classes = [permissions.IsAuthenticated, IsOwner]
    
    def get_queryset(self):
        return Collection.objects.filter(user=self.request.user)

# Bookmark Views
class BookmarkListCreateView(generics.ListCreateAPIView):
    serializer_class = BookmarkSerializer
    permission_classes = [permissions.IsAuthenticated]
    
    def get_queryset(self):
        collection_id = self.request.query_params.get('collection_id')
        if collection_id:
            return Bookmark.objects.filter(user=self.request.user, collection_id=collection_id)
        return Bookmark.objects.filter(user=self.request.user)
    
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class BookmarkDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = BookmarkSerializer
    permission_classes = [permissions.IsAuthenticated, IsOwner]
    
    def get_queryset(self):
        return Bookmark.objects.filter(user=self.request.user)

@api_view(['GET'])
def bookmarks_by_tag(request, tag):
    bookmarks = Bookmark.objects.filter(
        user=request.user, 
        tags__icontains=tag
    )
    serializer = BookmarkSerializer(bookmarks, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def api_root(request):
    return Response({
        'message': 'Bookmark Manager API is running!',
        'endpoints': {
            'auth_register': '/api/auth/register/',
            'auth_login': '/api/auth/login/',
            'collections': '/api/collections/',
            'bookmarks': '/api/bookmarks/'
        }
    })