from django.forms import ModelForm, DateInput
from calendarapp.models import Event, EventMembers
from django import forms
from .models import *

class EventForm(ModelForm):
  class Meta:
    model = Event
    # datetime-local is a HTML5 input type, format to make date time show on fields
    widgets = {
      'start_time': DateInput(attrs={'type': 'datetime-local'}, format='%Y-%m-%dT%H:%M'),
      'end_time': DateInput(attrs={'type': 'datetime-local'}, format='%Y-%m-%dT%H:%M'),
    }
    exclude = ['user']

  def __init__(self, *args, **kwargs):
    super(EventForm, self).__init__(*args, **kwargs)
    # input_formats to parse HTML5 datetime-local input to datetime field
    self.fields['start_time'].input_formats = ('%Y-%m-%dT%H:%M',)
    self.fields['end_time'].input_formats = ('%Y-%m-%dT%H:%M',)



class AddMemberForm(forms.ModelForm):
  class Meta:
    model = AddManualMembers
    fields = '__all__'

class AddLatestNewsForm(forms.ModelForm):
    class Meta:
        model = AddLatestNews
        widgets = {
            'end_time':DateInput(attrs={'type':'datetime-local'},format='%Y-%m-%dT%H:%M'),
        }
        exclude=['user']
    def __init__(self,*args,**kwargs):
        super(AddLatestNewsForm,self).__init__(*args,**kwargs)
        self.fields['end_time'].input_format = ('%Y-%m-%dT%H:%M',)