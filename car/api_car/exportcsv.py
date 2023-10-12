from django.http import HttpResponse
import csv

from review.models import Country, Manufacturer, Car, Comment


def export_country_csv(request):
    data = Country.objects.all()

    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="country.csv"'

    writer = csv.writer(response)
    writer.writerow([
        'id',
        'name',
        ])

    for country in data:
        writer.writerow([country.pk,
                         country.name,])

    return response

def export_manufacturer_csv(request):
    data = Manufacturer.objects.all()

    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="manufacturer.csv"'

    writer = csv.writer(response)
    writer.writerow([
        'id',
        'name',
        'country',
        ])

    for manufacturer in data:
        writer.writerow([manufacturer.pk,
                         manufacturer.name,
                         manufacturer.country,])

    return response

def export_car_csv(request):
    data = Car.objects.all()

    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="car.csv"'

    writer = csv.writer(response)
    writer.writerow([
        'id',
        'name',
        'manufacturer',
        'start_year',
        'end_year',
        ])

    for car in data:
        writer.writerow([car.pk,
                         car.name,
                         car.manufacturer,
                         car.start_year,
                         car.end_year,])

    return response

def export_comment_csv(request):
    data = Comment.objects.all()

    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="post.csv"'

    writer = csv.writer(response)
    writer.writerow([
        'id',
        'email',
        'car',
        'creation_date',
        'comment',
        ])

    for comment in data:
        writer.writerow([comment.pk,
                         comment.email,
                         comment.car,
                         comment.creation_date,
                         comment.comment,])

    return response
