from django.contrib.auth.models import User
from PIL import Image
from django.db import models
from django.urls import reverse
from calendarapp.models import Event
from teams.models import Team


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='user.png', upload_to='profile_pics')
    roll_no = models.CharField(max_length=12)
    SECTION = [("B01", "B01"), ("B02", "B02"), ("B03", "B03"), ("B04", "B04"), ("B05", "B05"), ("B06", "B06"), ("B07", "B07"), ("B08", "B08"), ("B09", "B09"),
               ("B10", "B10"), ("B11", "B11"), ("B12", "B12"), ("B13", "B13"), ("B14", "B14"), ("B15", "B15"), ("B16", "B16"), ("B17", "B17"), ("B18", "B18"), ("B19", "B19")]
    section = models.CharField(max_length=4, choices=SECTION)
    cgpa = models.DecimalField(max_digits=4, decimal_places=2, default=0.0)
    tenth=models.DecimalField(max_digits=4,decimal_places=2,default=0.0)
    inter= models.IntegerField(default=0)
    backlogs = models.IntegerField(default=0)
    num_drives_attempt = models.IntegerField(default=0)
    is_selected = models.BooleanField(default=False)
    is_cr = models.BooleanField(default=False)
    current_events=models.ManyToManyField(Event)
    unique_string = models.CharField(max_length=15,default='1xcVu0I')
    team = models.ForeignKey(Team, on_delete=models.CASCADE, default=7)

    @property
    def tenth_per(self):
        return '{:.2f}'.format(float(self.tenth)*9.5)

    @property
    def inter_per(self):
        return '{:.2f}'.format(float(self.inter)*0.1)

    @property
    def percentage(self):
        return '{:.2f}'.format(float(self.cgpa)*9.5)

    def __str__(self):
        return f'{self.user.username} Profile'

    def get_absolute_url(self):
        return reverse("profile_detail", args=[str(self.user.username)])

    def save(self, *args, **kwargs):
        super().save()
        img = Image.open(self.image.path)
        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.image.path)
