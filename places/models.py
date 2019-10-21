import datetime

from django.db import models
from django.utils import timezone


# Create your models here.
class Place(models.Model):

    name = models.CharField(max_length=50)
    address = models.CharField(max_length=250)
    # restaurant = models.CharField(max_length=150)
    # latitude = models.FloatField()
    # longitude = models.FloatField()
    reg_date = models.DateTimeField('date registered')

    def __str__(self):
        # return self.restaurant
        return self.name

    def was_registered_recently(self):
        return self.reg_date >= timezone.now() - datetime.timedelta(days=1)


class Restaurant(models.Model):

    place = models.OneToOneField(Place, on_delete=models.CASCADE, primary_key=True, )

    latitude = models.FloatField()
    longitude = models.FloatField()

    def __str__(self):
        return self.place.name
