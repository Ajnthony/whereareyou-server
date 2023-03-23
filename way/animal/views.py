from rest_framework.response import Response
from .models import (
    Animal,
    Tag,
)
from rest_framework import (
    permissions,
    viewsets,
    mixins,
    status,
    generics,
)
from .serializers import (
    AnimalSerializer,
    AnimalDetailSerializer,
    TagSerializer,
)
from drf_spectacular.utils import (
    extend_schema_view,
    extend_schema,
    OpenApiParameter,
    OpenApiTypes,
)

class CreateAnimalPermission(permissions.BasePermission):
    message = 'Only the owner of this animal can make changes.'
    
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        
        return request.user == obj.user


@extend_schema_view(
    list=extend_schema(
        parameters=[
            OpenApiParameter(
                'tags',
                OpenApiTypes.STR,
                description='Comma-separated list of tag ids to filter animals'
            )
        ]
    )
)
class AnimalViewset(viewsets.ModelViewSet):
    serializer_class = AnimalDetailSerializer
    queryset = Animal.objects.all()
    permission_classes = [CreateAnimalPermission, permissions.IsAuthenticated]
    
    def _params_to_ints(self, queries):
        return [int(str_id) for str_id in queries.split(',')]
    
    def get_queryset(self):
        tags = self.request.query_params.get('tags')
        queryset = self.queryset
        
        if tags:
            tag_ids = self._params_to_ints(tags)
            queryset = queryset.filter(tags__id__in=tag_ids)
            
        # return queryset.filter(
        #     user=self.request.user
        # ).order_by('-id').distinct()
        return queryset
        
    def get_serializer_class(self):
        if self.action == 'list':
            return AnimalSerializer
        if self.action == 'upload_image':
            # handle image to be added
            print('Image handling is not implemented yet')
            return False
    
        return self.serializer_class
    
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
        
    # not allowing anyone to delete animal obj
    def destroy(self, request, pk=None):
        return Response(
            {'success':True,
             'message': 'Actually no one is allowed to delete anything.'},
            status=status.HTTP_200_OK)
        
# class BaseAnimalAttrViewset(
#     mixins.DestroyModelMixin,
#     mixins.UpdateModelMixin,
#     mixins.ListModelMixin,
#     viewsets.GenericViewSet,
#     ):
    
#     # auth
#     # authentication_classes= []
#     permission_classes = [permissions.IsAuthenticated]
    
#     def get_queryset(self):
#         # assigned_only = bool(
#         #     int(self.request.query_params.get('assigned_only', 0))
#         # )
        
#         # queryset = self.queryset
        
#         # if assigned_only:
#         #     queryset = queryset.filter(animal__isnull=False)
#         # return queryset.filter(
#         #     user=self.request.user
#         # ).order_by('-name').distinct()
#         return Response({'success':True}, status=status.HTTP_200_OK)
        
class TagViewset(viewsets.ModelViewSet):
    serializer_class = TagSerializer
    queryset = Tag.objects.all()
    permission_classes = [permissions.IsAuthenticated]
    
    def get_queryset(self):
        return Tag.objects.all()