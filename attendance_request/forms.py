from django.forms import ModelForm, DateInput
from attendance_request.models import *
from django import forms
from .models import *

class RequestForm(ModelForm):
  class Meta:
    model = AttendanceRequest
    widgets = {
      'start_time': DateInput(attrs={'type': 'datetime-local'}, format='%Y-%m-%dT%H:%M'),
    }
    exclude = ['user','granted','rejected']

  def __init__(self, *args, **kwargs):
    super(RequestForm, self).__init__(*args, **kwargs)
    # input_formats to parse HTML5 datetime-local input to datetime field
    self.fields['start_time'].input_formats = ('%Y-%m-%dT%H:%M',)

# class RequestForm(forms.ModelForm):
#     class Meta:
#         model  = AttendanceRequest
#         fields=['company','request_type','start_time']

#     def __init__(self, *args, **kwargs):
#         super(RequestForm, self).__init__(*args, **kwargs)
#         self.fields['start_time'].input_formats = ('%Y-%m-%dT%H:%M',)
