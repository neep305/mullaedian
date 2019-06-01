import datetime

from django.db import models
from django.utils import timezone

# Create your models here.
class Place(models.Model):
    restaurant = models.CharField(max_length=150)
    latitude = models.FloatField()
    longitude = models.FloatField()
    reg_date = models.DateTimeField('date registered')

    def __str__(self):
        return self.restaurant

    def was_registered_recently(self):
        return self.reg_date >= timezone.now() - datetime.timedelta(days=1)
