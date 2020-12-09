from django.contrib.auth.models import User
from PIL import Image
from django.db import models
from django.urls import reverse
from meeting.models import Meeting
from todo.models import TaskList

class Team(models.Model):
    team_name =models.CharField(max_length=200)
    team_instructor = models.CharField(max_length=50)
    subject = models.CharField(max_length=50)
    team_members = models.ManyToManyField(User)
    image = models.ImageField(default='user.png', upload_to='team_pics', null=True, blank=True)
    slug = models.SlugField(max_length=200)
    project_name=models.CharField(max_length=200)
    project_field = models.CharField(max_length=200)
    LEVELS=[('Definition','Definition'),('Initiation','Initiation'),('Planning','Planning'),('Execution','Execution'),('Monitoring & Control','Monitoring & Control'),('Closure','Closure')]
    project_level = models.CharField(max_length=100, choices=LEVELS)
    team_leader = models.CharField(max_length=200)
    meetings = models.ManyToManyField(Meeting)
    task_list = models.ForeignKey(TaskList, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.team_name} Team'

    def get_absolute_url(self):
        return reverse("team-detail", args=[str(self.slug)])

    def save(self, *args, **kwargs):
        super().save()
        img = Image.open(self.image.path)
        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.image.path)
