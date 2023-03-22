# from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    AnimalViewset,
    TagViewset,
)

app_name = 'animal'

router = DefaultRouter()
router.register('animals', AnimalViewset, basename='animal')
router.register('tags', TagViewset, basename='tags')


urlpatterns = router.urls
