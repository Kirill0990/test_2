from rest_framework import serializers

from review.models import Country, Manufacturer, Car, Comment


class CountrySerializers(serializers.ModelSerializer):

    class Meta():
        model = Country
        fields = ('id', 'name', 'manufacturers')


class ManufacturerSerializers(serializers.ModelSerializer):

    class Meta():
        model = Manufacturer
        fields = ('id', 'name', 'country', 'cars', 'comments')


class CarSerializers(serializers.ModelSerializer):

    class Meta():
        model = Car
        fields = ('id', 'name', 'manufacturer',
                  'start_year', 'end_year', )


class CommentSerializers(serializers.ModelSerializer):

    class Meta():
        model = Comment
        fields = ('id', 'email', 'car', 'creation_date', 'comment',)
