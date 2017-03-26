from django.db import models
from django.utils import timezone

RATING_OPTIONS = (
    (1, 'Not Good'),
    (2, 'OK'),
    (3, 'Good'),
    (4, 'Very Good'),
    (5, 'Excellent'),
)

class Ratings(models.Model):
    rating = models.CharField(
        max_length=30,
        choices=RATING_OPTIONS,
        default=5)

    class Meta:
        abstract = True


class Atmosphere(Ratings):
    pass


class Coffee(Ratings):
    pass


class Wifi(Ratings):
    pass


class Cafe(models.Model):
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=200)
    address1 = models.CharField(max_length=200)
    address2 = models.CharField(max_length=200)
    address3 = models.CharField(max_length=200)
    city = models.CharField(max_length=200)
    post_code = models.CharField(max_length=30)
    atmosphere_rating = models.ForeignKey(Atmosphere)
    coffee_rating = models.ForeignKey(Coffee)
    wifi_rating = models.ForeignKey(Wifi)
