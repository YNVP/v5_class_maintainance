from django.contrib.auth.models import User
from PIL import Image
from django.db import models
from django.urls import reverse
from calendarapp.models import Event

class AttendanceRequest(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    company = models.CharField(max_length=40)
    TYPE = [("Training", "Training"), ("Assessment", "Assessment")]
    request_type = models.CharField(max_length=20, choices=TYPE, blank=True, null=True)
    image = models.ImageField(default='user.png', upload_to='request_pics', null=True, blank=True)
    start_time = models.DateTimeField()
    granted = models.BooleanField(default=False)
    rejected = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.user.username} Request'

    def get_absolute_url(self):
        return reverse("profile_detail", args=[str(self.user.username)])

    def save(self, *args, **kwargs):
        super().save()
        img = Image.open(self.image.path)
        img.save(self.image.path)