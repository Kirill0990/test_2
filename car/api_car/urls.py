from django.urls import path, include
from rest_framework import routers

from .views import (CountryViewSet,  ManufacturerViewSet,
                    CarViewSet, CommentViewSet)

router = routers.DefaultRouter()
router.register('country', CountryViewSet, basename='country')
router.register('manufacturer', ManufacturerViewSet, basename='manufacturer')
router.register('car', CarViewSet, basename='car')
router.register('comment', CommentViewSet, basename='comment')

urlpatterns = [
    path('', include(router.urls))
]
