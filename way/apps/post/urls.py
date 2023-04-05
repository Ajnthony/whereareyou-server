from django.urls import path, include
from .views import (CategoryViewset, PostsListView, PostDetailView,)
from rest_framework.routers import DefaultRouter

app_name = 'post'

router = DefaultRouter()
router.register('categories', CategoryViewset, basename='category')


urlpatterns = [
    path('posts/', PostsListView.as_view(), name='posts-list'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-item'),
    path('', include(router.urls), name='category'),
]
