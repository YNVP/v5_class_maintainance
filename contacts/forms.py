from django import forms
from .models import Contact
from django.contrib.auth.models import User
from django.forms import Textarea

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['name','subject','number','section']

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user', None)
        super(ContactForm, self).__init__(*args, **kwargs)

