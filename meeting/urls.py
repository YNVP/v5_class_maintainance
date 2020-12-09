from django.urls import path,include

from .views import (
    MeetingUpdateView,
    MeetingDeleteView,
    meeting_create,
)

urlpatterns = [
    path('new/', meeting_create, name='meeting-create'),
    path('<slug>/update/', MeetingUpdateView.as_view(), name='meeting-update'),
    path('<slug>/delete/', MeetingDeleteView.as_view(), name='meeting-delete'),
]