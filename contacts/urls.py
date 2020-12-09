from django.urls import path,include

from .views import (
    ContactUpdateView,
    ContactDeleteView,
)
from . import views

urlpatterns = [
    path('', views.home, name='contact-home'),
    path('new/', views.contact_create, name='contact-create'),
    path('<int:pk>/update/', ContactUpdateView.as_view(), name='contact-update'),
    path('<int:pk>/delete/', ContactDeleteView.as_view(), name='contact-delete'),
]