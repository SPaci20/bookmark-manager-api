from django.urls import path, include
from rest_framework_simplejwt.views import TokenRefreshView
from . import views

urlpatterns = [
    # Authentication
    path('auth/register/', views.register, name='register'),
    path('auth/login/', views.login, name='login'),
    path('auth/profile/', views.profile, name='profile'),
    path('auth/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    
    # Collections
    path('collections/', views.CollectionListCreateView.as_view(), name='collection-list'),
    path('collections/<int:pk>/', views.CollectionDetailView.as_view(), name='collection-detail'),
    
    # Bookmarks
    path('bookmarks/', views.BookmarkListCreateView.as_view(), name='bookmark-list'),
    path('bookmarks/<int:pk>/', views.BookmarkDetailView.as_view(), name='bookmark-detail'),
    path('bookmarks/tag/<str:tag>/', views.bookmarks_by_tag, name='bookmarks-by-tag'),
   
    #testing API root
    path('', views.api_root, name='api-root'),
]