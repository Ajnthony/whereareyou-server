from django.contrib import admin
from django.urls import path
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from rest_framework.schemas import get_schema_view
from rest_framework.documentation import include_docs_urls

urlpatterns = [
    path('api/token/', TokenObtainPairView.as_view(), name='token'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('admin/', admin.site.urls),
    
    # api docs
    path('docs-ui/', include_docs_urls(title='WAY - Where Are You')),
    path('schema/', get_schema_view(
        title='WAY - Where Are You',
        description='WAY API',
        version='v1',
    ), name='openapi-schema')
]
