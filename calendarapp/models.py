from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User


class Event(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=200, unique=True)
    description = models.TextField()
    next_level = models.CharField(max_length=50)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    created_date = models.DateTimeField(auto_now_add=True)
    cgpa = models.DecimalField(max_digits=4,decimal_places=2,default=0.0)
    tenth = models.DecimalField(max_digits=4,decimal_places=2,default=0.0)
    inter = models.DecimalField(max_digits=4,decimal_places=2,default=0.0)
    is_completed = models.BooleanField(default=False)
    disable_add = models.BooleanField(default=False)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('calendarapp:event-detail', args=(self.id,))

    @property
    def get_html_url(self):
        url = reverse('calendarapp:event-detail', args=(self.id,))
        return f'<a href="{url}" data-toggle="tooltip" data-placement="top" title="{self.title} Level: {self.next_level}" style="text-decoration:none;color:white;font-size:1.75vh;"> {self.title} </a>'


class EventMembers(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    students = models.ManyToManyField(User)


class AddManualMembers(models.Model):
    get_class = models.IntegerField()
    get_rolls = models.TextField()

class AddLatestNews(models.Model):
    created_time = models.DateTimeField(auto_now_add=True)
    end_time = models.DateTimeField()
    post_data = models.TextField()

    def get_absolute_url(self):
        return reverse('home')

