from rest_framework import generics
from rest_framework.permissions import (
    SAFE_METHODS,
    BasePermission,
    IsAuthenticated,
)
from .serializers import UserSerializer

class UserUpdatePermission(BasePermission):
    message = 'You do not have access to other user\'s accounts but yours.'
    
    def has_object_permission(self, request, view, obj):
        if request.method in SAFE_METHODS:
            return True
        
        return request.user == obj['id']
    
class CreateUserView(generics.CreateAPIView):
    serializer_class = UserSerializer
    
class UpdateUserView(generics.RetrieveUpdateAPIView):
    serializer_class = UserSerializer
    permission_classes = [UserUpdatePermission, IsAuthenticated]
    