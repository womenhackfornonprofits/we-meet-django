from django.db import models
from django.utils import timezone

RATING_OPTIONS = (
    (1, 'Not Good'),
    (2, 'OK'),
    (3, 'Good'),
    (4, 'Very Good'),
    (5, 'Excellent'),
)


class Address(models.Model):
    street = models.TextField()
    postcode = models.TextField()
    city = models.TextField()

    class Meta:
        verbose_name_plural = 'addresses'


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
    address = models.ForeignKey(Address)
    atmosphere_rating = models.ForeignKey(Atmosphere)
    coffee_rating = models.ForeignKey(Coffee)
    wifi_rating = models.ForeignKey(Wifi)
