from django.urls import path, include
from rest_framework import routers
from . import export

from .views import (CountryViewSet,  ManufacturerViewSet,
                    CarViewSet, CommentViewSet)

router = routers.DefaultRouter()
router.register('country', CountryViewSet, basename='country')
router.register('manufacturer', ManufacturerViewSet, basename='manufacturer')
router.register('car', CarViewSet, basename='car')
router.register('comment', CommentViewSet, basename='comment')

urlpatterns = [
    path('', include(router.urls)),
    path('auth/', include('djoser.urls')),
    path('api/export/country', export.export_country_to_xlsx),
    path('api/export/manufacturer', export.export_manufactures_to_xlsx),
    path('api/export/car', export.export_car_to_xlsx),
    path('api/export/comment', export.export_comment_to_xlsx),
]
