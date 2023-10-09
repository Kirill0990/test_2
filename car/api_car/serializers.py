from rest_framework import serializers

from review.models import Country, Manufacturer, Car, Comment


class CountrySerializers(serializers.Serializer):

    class Meta():
        model = Country
        field = ('id', 'name',)


class ManufacturerSerializers(serializers.Serializer):

    class Meta():
        model = Manufacturer
        field = ('id', 'name', 'slug', 'country',)


class CarSerializers(serializers.Serializer):

    class Meta():
        model = Car
        field = ('id', 'name', 'manufacture', 'start_year', 'end_year',)


class CommentSerializers(serializers.Serializer):

    class Meta():
        model = Comment
        field = ('id', 'email', 'car', 'creation_date', 'comment',)
