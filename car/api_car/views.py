from rest_framework import viewsets
from rest_framework import permissions

from .serializers import (CountrySerializers, CarSerializers,
                          ManufacturerSerializers, CommentSerializers)
from review.models import Country, Manufacturer, Car, Comment


class CountryViewSet(viewsets.ModelViewSet):
    queryset = Country.objects.all()
    serializer_class = CountrySerializers
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class ManufacturerViewSet(viewsets.ModelViewSet):
    queryset = Manufacturer.objects.all()
    serializer_class = ManufacturerSerializers
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class CarViewSet(viewsets.ModelViewSet):
    queryset = Car.objects.all()
    serializer_class = CarSerializers
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializers
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
