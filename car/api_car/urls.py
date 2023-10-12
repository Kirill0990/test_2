from django.urls import path, include
from rest_framework import routers
from . import exportxlsx
from . import exportcsv
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
    path('exportxlsx/country/', exportxlsx.export_country_to_xlsx),
    path('exportxlsx/manufacturer/', exportxlsx.export_manufactures_to_xlsx),
    path('exportxlsx/car/', exportxlsx.export_car_to_xlsx),
    path('exportxlsx/comment/', exportxlsx.export_comment_to_xlsx),
    path('exportcsv/country/', exportcsv.export_country_csv),
    path('exportcsv/manufacturer/', exportcsv.export_manufacturer_csv),
    path('exportcsv/car/', exportcsv.export_car_csv),
    path('exportcsv/comment/', exportcsv.export_comment_csv),
]
