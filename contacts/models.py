from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse


class Contact(models.Model):
    name = models.CharField(max_length=100)
    subject = models.CharField(max_length=100)
    number=models.CharField(max_length=100)
    SECTION = [("B01", "B01"), ("B02", "B02"), ("B03", "B03"), ("B04", "B04"), ("B05", "B05"), ("B06", "B06"), ("B07", "B07"), ("B08", "B08"), ("B09", "B09"),
               ("B10", "B10"), ("B11", "B11"), ("B12", "B12"), ("B13", "B13"), ("B14", "B14"), ("B15", "B15"), ("B16", "B16"), ("B17", "B17"), ("B18", "B18"), ("B19", "B19")]
    section = models.CharField(max_length=4, choices=SECTION)
    date_posted = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('home')
