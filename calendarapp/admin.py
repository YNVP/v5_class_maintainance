from django.contrib import admin
from calendarapp.models import Event, EventMembers, AddLatestNews

admin.site.register(Event)
admin.site.register(EventMembers)
admin.site.register(AddLatestNews)