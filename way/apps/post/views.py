from rest_framework import (
    generics,
    viewsets,
    status,
)
from rest_framework.permissions import (
    SAFE_METHODS,
    IsAdminUser,
    IsAuthenticated,
    AllowAny,
    BasePermission,
)
from rest_framework.response import Response
from .serializers import (PostSerializer, CategorySerializer,)
from .models import (Post, Category,)
from django.shortcuts import get_object_or_404

class PostWritePermission(BasePermission):
    message = 'You do not have access to this post.'

    def has_object_permission(self, request, view, obj):
        if request.method in SAFE_METHODS:
            return True

        return request.user == obj.user

class PostsListView(generics.ListCreateAPIView):
    serializer_class = PostSerializer
    queryset = Post.objects.all()
    
    def get_permissions(self):
        if self.request.method in SAFE_METHODS:
            return [AllowAny(),]
        
        return [IsAuthenticated(),]
    
    def get_queryset(self):
        queryset = Post.objects.all()
        return queryset

class PostDetailView(generics.RetrieveUpdateAPIView):
    serializer_class = PostSerializer
    queryset = Post.objects.all()
    permission_classes = [IsAdminUser, PostWritePermission]

    def get_object(self, queryset=None, **kwargs):
        item = self.kwargs.get('pk')
        
        # get post by slug
        return get_object_or_404(Post, slug=item)

class CategoryViewset(viewsets.ModelViewSet):
    serializer_class = CategorySerializer
    queryset = Category.objects.filter(is_active=True)

    # only admin (staff) users can create/update/delete category
    def get_permissions(self):
        if self.request.method not in SAFE_METHODS:
            return [IsAdminUser(),]

        return [IsAuthenticated(),]