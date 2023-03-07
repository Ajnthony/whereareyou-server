from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    AnimalViewset,
    TagViewset,
)

router = DefaultRouter()

router.register('animals',AnimalViewset)
router.register('tags',TagViewset)

app_name = 'animal'

urlpatterns = [
    path('', include(router.urls))
]