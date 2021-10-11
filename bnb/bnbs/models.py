from django.db import models
from django.contrib.auth.models import User

class Accommodation(models.Model):
        
    room_id = models.IntegerField(default=0, null=True)
    name = models.CharField(max_length=128, null=True)
    review = models.DecimalField(max_digits=3, decimal_places=2, null=True)
    neighbourhood = models.CharField(max_length=40, null=True)
    description = models.TextField(null=True)
    latitude = models.FloatField(null=True)
    longitude = models.FloatField(null=True)
    property_long = models.CharField(max_length=36, null=True)
    property = models.CharField(max_length=20, null=True)
    room_type = models.CharField(max_length=13, null=True)
    accommodates = models.IntegerField(null=True)
    bedrooms = models.IntegerField(null=True)
    beds = models.IntegerField(null=True)
    number_of_baths = models.DecimalField(max_digits=5, decimal_places=1, null=True)
    bathroom_shared = models.BooleanField(default = True, null=True)
    amenities = models.TextField(null=True)
    price_eu = models.IntegerField(default=0, null=True)
    price_us = models.IntegerField(default=0, null=True)
    listing_url = models.URLField(max_length=80, null=True)
    picture_url = models.URLField(max_length=200, null=True)
    # price_rater = models.IntegerField(default=0, null=True)

    def __str__(self):
        return (str(self.room_id) + str(self.name))

class Restaurant(models.Model):
    name = models.CharField(max_length=50, null=True)
    latitude = models.FloatField(null=True)
    longitude = models.FloatField(null=True) 
    description = models.TextField(null=True)
    name_en = models.TextField(null=True)
    description_en = models.TextField(null=True) 
    address = models.CharField(max_length=50, null=True)
    url = models.URLField(max_length=200, null=True)
    media = models.URLField(max_length=200, null=True)
    thumbnail = models.URLField(max_length=200, null=True)

    def __str__(self):
        return str(self.name)

class Art(models.Model):
    trcid = models.CharField(max_length=50, null=True)
    name = models.CharField(max_length=80, null=True)
    name_en = models.CharField(max_length=85, null=True)
    latitude = models.FloatField(null=True)
    longitude = models.FloatField(null=True) 
    description = models.TextField(null=True)
    description_en = models.TextField(null=True) 
    address = models.CharField(max_length=50, null=True)
    url = models.URLField(max_length=200, null=True)
    media = models.URLField(max_length=200, null=True)
    thumbnail = models.URLField(max_length=200, null=True)

    def __str__(self):
        return str(self.name)

class ShoppingArea(models.Model):
    name = models.CharField(max_length=45, null=True)
    latitude = models.FloatField(null=True)
    longitude = models.FloatField(null=True) 

    def __str__(self):
        return str(self.name)