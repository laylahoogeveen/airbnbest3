from django.db import models
from django.contrib.auth.models import User

class Accommodation(models.Model):

    ENTIRE_HOME = 'ENT'
    PRIVATE_ROOM = 'PRR'
    HOTEL_ROOM = 'HTR'
    SHARED_ROOM = 'SHR'
    ROOM_CHOICES = [
        (ENTIRE_HOME, 'ENT'),
        (PRIVATE_ROOM, 'PRR'),
        (HOTEL_ROOM, 'HTR'),
        (SHARED_ROOM, 'SHR')
        ]

    room_id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=128)
    review = models.DecimalField(max_digits=3, decimal_places=2)
    description = models.TextField()
    latitude = models.FloatField()
    longitude = models.FloatField()
    property_long = models.CharField(max_length=36)
    property = models.CharField(max_length=20)
    room_type = models.CharField(
        max_length=36,
        choices=ROOM_CHOICES,
    )
    accomodates = models.IntegerField(default = 0)
    bedrooms = models.IntegerField(default = 0.0)
    beds = models.IntegerField(default = 0)
    number_of_baths = models.DecimalField(max_digits=5, decimal_places=1)
    bathroom_shared = models.BooleanField(default = True)
    amenities = models.TextField()
    price_eu = models.IntegerField(default = 0)
    price_us = models.IntegerField(default = 0)
    listing_url = models.URLField(max_length=80)
    picture_url = models.URLField(max_length=200)

# # class Restaurant(models.Model):

# class Art(models.Model):
#     MUSEUM = 'MUS'
#     GALLERY = 'GAL'
#     ART_CHOICES = [
#         (MUSEUM, 'Museum'),
#         (GALLERY, 'Gallery'),
#     ]
#     type = models.CharField(
#         max_length=2,
#         choices=ART_CHOICES,
#         default=MUSEUM, 
#     )
