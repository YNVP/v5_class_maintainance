from django.forms import ModelForm, DateInput
from django import forms
from .models import Meeting
from django.contrib.auth.models import User
from django.forms import Textarea

class MeetingForm(forms.ModelForm):
    class Meta:
        model = Meeting
        widgets = {
          'start_time': DateInput(attrs={'type': 'datetime-local'}, format='%Y-%m-%dT%H:%M'),
        }
        fields = ['meeting_name','agenda','link','start_time']

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user', None)
        super(MeetingForm, self).__init__(*args, **kwargs)
        self.fields['start_time'].input_formats = ('%Y-%m-%dT%H:%M',)