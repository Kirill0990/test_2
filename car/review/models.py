from django.db import models


class Country(models.Model):
    name = models.CharField(max_length=100)


class Manufacturer(models.Model):
    name = models.CharField(max_length=100)
    country = models.ForeignKey(
        Country, on_delete=models.SET_NULL,
        related_name='manufacturers', blank=True, null=True
    )


class Car(models.Model):
    name = models.CharField(max_length=100)
    manufacturer = models.ForeignKey(
        Manufacturer, on_delete=models.SET_NULL,
        related_name='cars', blank=True, null=True
    )
    start_year = models.IntegerField()
    end_year = models.IntegerField()


class Comment(models.Model):
    email = models.EmailField(max_length=80, unique=True)
    car = models.ForeignKey(
        Car, on_delete=models.SET_NULL,
        related_name='comments', blank=True, null=True
    )
    creation_date = models.DateTimeField()
    comment = models.TextField(max_length=250)
