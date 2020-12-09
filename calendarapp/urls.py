from django.urls import path

from . import views

app_name = 'calendarapp'
urlpatterns = [
    path('', views.CalendarView.as_view(), name='calendar'),
    path('event/new/', views.create_event, name='event_new'),
    path('event/edit/<int:pk>/', views.EventEdit.as_view(), name='event_edit'),
    path('event/<int:event_id>/details/', views.event_details, name='event-detail'),
    path('add_eventmember/<int:event_id>', views.add_eventmember, name='add_eventmember'),
    path('event/<int:pk>/remove', views.EventMemberDeleteView.as_view(), name="remove_event"),
    path('add_student_to_event/',views.add_student_to_event, name='add_student_to_event'),
    path('export/ps_csv/<event_id>', views.export_presentees_csv, name='export_presentees_csv'),
    path('export/abs_csv/<event_id>', views.export_absentees_csv, name='export_absentees_csv'),
    path('news/add', views.add_latest_news, name='add_news'),
]