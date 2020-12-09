import django_filters
from user.models import Profile
from django.db.models import F

class ClassFilter(django_filters.FilterSet):
    class Meta:
        model = Profile
        exclude=['user','image','backlogs','num_drives_attempt','section','is_cr']
