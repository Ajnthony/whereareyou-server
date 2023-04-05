from django.contrib import admin
from django.urls import path, include
from drf_spectacular.views import (
    SpectacularAPIView,
    SpectacularRedocView,
    SpectacularSwaggerView,
)

urlpatterns = [
    path('admin/', admin.site.urls),
    
    path('api/', include([
        path('schema/', SpectacularAPIView.as_view(), name='schema'),
        path('swagger-ui/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
        path('redoc-ui/', SpectacularRedocView.as_view(url_name='schema'), name='redoc-ui'),
        path('users/', include('apps.user.urls', namespace='user')),
        
        # already using 'animals/' and 'tags/'
        path('', include('apps.animal.urls', namespace='animal')),
        path('', include('apps.post.urls', namespace='post')),
        path('', include('apps.comment.urls', namespace='comment')),
    ])),
]
