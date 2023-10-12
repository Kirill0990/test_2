from rest_framework import serializers

from review.models import Country, Manufacturer, Car, Comment


class CountrySerializers(serializers.ModelSerializer):
    class Meta():
        model = Country
        fields = ('id', 'name', 'manufacturer')


class CarSerializers(serializers.ModelSerializer):
    count_comments = serializers.SerializerMethodField()

    class Meta():
        model = Car
        fields = ('id', 'name', 'manufacturer',
                  'start_year', 'end_year', 'comments', 'count_comments')

    def get_count_comments(self, obj):
        return obj.comments.count()


class ManufacturerSerializers(serializers.ModelSerializer):
    cars = CarSerializers(many=True)

    class Meta():
        model = Manufacturer
        fields = ('id', 'name', 'country', 'cars',)


class CommentSerializers(serializers.ModelSerializer):
    class Meta():
        model = Comment
        fields = ('id', 'email', 'car', 'creation_date', 'comment',)
