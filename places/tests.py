import datetime

from django.test import TestCase
from django.utils import timezone

from django.urls import reverse

from .models import Place


# Create your tests here.
class PlaceModelTests(TestCase):

    def test_was_registered_recently_with_future_question(self):
        """
        was_registered_recently() returns False for places
        :return:
        """
        time = timezone.now() + datetime.timedelta(days=30)
        future_place = Place(reg_date=time)
        self.assertIs(future_place.was_registered_recently(), True)
