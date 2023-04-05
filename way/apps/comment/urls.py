from django.urls import path, include
from .views import (CommentsListView, CommentDetailView,)


app_name = 'comment'


urlpatterns = [
    path('comments/', CommentsListView.as_view(), name='comment-list'),
    path('comments/<int:pk>/', CommentDetailView.as_view(), name='comment-detail'),
    
]
