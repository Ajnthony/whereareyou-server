from rest_framework.response import Response
from rest_framework import permissions
from animal.models import (
    Animal,
    Tag,
)
from rest_framework import (
    viewsets,
    mixins,
    status,
    )
from animal_api.serializers import (
    AnimalSerializer,
    AnimalDetailSerializer,
    TagSerializer,
)

class CreateAnimalPermission(permissions.BasePermission):
    message = 'Only the owner of this animal can make changes.'
    
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        
        return request.user == obj.owner

class AnimalViewset(viewsets.ModelViewSet):
    serializer_class = AnimalDetailSerializer
    queryset = Animal.objects.all()
    
    # authentication
    # authentication_classes = []
    permission_classes = [
                        # permissions.IsAuthenticatedOrReadOnly,
                        #   permissions.DjangoModelPermissionsOrAnonReadOnly,
                          CreateAnimalPermission
                          ]
    
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
        
class BaseAnimalAttrViewset(
    mixins.DestroyModelMixin,
    mixins.UpdateModelMixin,
    mixins.ListModelMixin,
    viewsets.GenericViewSet,
    ):
    
    # auth
    # authentication_classes= []
    # permission_classes = []
    
    def get_queryset(self):
        assigned_only = bool(
            int(self.request.query_params.get('assigned_only', 0))
        )
        
        queryset = self.queryset
        
        if assigned_only:
            queryset = queryset.filter(animal__isnull=False)
        return queryset.filter(
            user=self.request.user
        ).order_by('-name').distinct()
        
class TagViewset(BaseAnimalAttrViewset):
    serializer_class = TagSerializer
    queryset = Tag.objects.all()