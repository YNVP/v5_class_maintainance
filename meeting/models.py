from PIL import Image
from django.db import models
from django.urls import reverse
from django.utils import timezone


class Meeting(models.Model):
    meeting_name =models.CharField(max_length=200)
    agenda = models.CharField(max_length=100)
    slug = models.SlugField(max_length=200)
    link = models.CharField(max_length=200)
    time_created=models.DateTimeField(default=timezone.now)
    start_time = models.DateTimeField()

    def __str__(self):
        return f'{self.meeting_name} Meeting'
