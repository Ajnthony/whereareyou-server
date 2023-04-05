from rest_framework import (
    generics,
    status,
)
from rest_framework.response import Response
from rest_framework.permissions import (
    SAFE_METHODS,
    IsAdminUser,
    IsAuthenticated,
    AllowAny,
    BasePermission,
)
from drf_spectacular.utils import (
    extend_schema_view,
    extend_schema,
    OpenApiParameter,
    OpenApiTypes,
)
from .serializers import CommentSerializer
from .models import Comment

@extend_schema_view(
    get=extend_schema(
        parameters=[
            OpenApiParameter(
                'post_id',
                OpenApiTypes.STR,
                description='id of the post to filter comments'
            )
        ]
    )
)
class CommentsListView(generics.ListCreateAPIView):
    serializer_class = CommentSerializer
    queryset = Comment.objects.all()
    
    def get_permissions(self):
        if self.request.method in SAFE_METHODS:
            return [AllowAny(),]
        
        return [IsAuthenticated(),]
    
    def get_queryset(self):
        post_id = int(self.request.query_params.get('post_id'))
        if not post_id:
            raise ValueError('Query \'post_id\' is not provided')
        
        queryset = Comment.objects.filter(post=post_id)
        print(queryset)
        return queryset
    
    
class CommentDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = CommentSerializer
    queryset = Comment.objects.all()
    
    def get_permissions(self):
        if self.request.method == 'DELETE':
            return [IsAdminUser(),]
        
        return [BasePermission(),]