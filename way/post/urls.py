from django.urls import path, include
from .views import (CategoryViewset, PostsListView, PostDetailView,)
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('', CategoryViewset, basename='categories')

app_name = 'post'

urlpatterns = [
    path('', PostsListView.as_view(), name='posts-list'),
    path('', PostDetailView.as_view(), name='post-item'),
    path('', include(router.urls)),
]
