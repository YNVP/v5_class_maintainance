from django.urls import path,include

from .views import (
    TeamUpdateView,
    TeamDeleteView,
    team_create,
    team_detail,
    all_teams,
)

urlpatterns = [
    path('<slug>/detail/', team_detail, name='team-detail'),
    path('new/', team_create, name='team-create'),
    path('<slug>/update/', TeamUpdateView.as_view(), name='team-update'),
    path('<slug>/delete/', TeamDeleteView.as_view(), name='team-delete'),
    path('all_teams/', all_teams,name="all_teams"),
]