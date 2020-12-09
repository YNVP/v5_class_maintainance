from django import forms
from .models import Team
from django.contrib.auth.models import User
from django.forms import Textarea

class TeamForm(forms.ModelForm):
    class Meta:
        model = Team
        fields = ['team_name','team_instructor','subject','team_members','image','project_name','project_field','project_level']

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user', None)
        super(TeamForm, self).__init__(*args, **kwargs)