from django.urls import path

from . import views
# from .views import AttendanceRequestCreateView
urlpatterns = [
    path('', views.all_requests, name='all_requests'),
    path('new_request/', views.create_requuest, name='new_request'),
    path('cr_requests/',views.cr_requests, name='cr_requests'),
    path('amc_requests/',views.amc_requests, name='amc_requests'),
    path('verify_accept/',views.verify_accept, name='verify_accept'),
    path('verify_reject/',views.verify_reject, name='verify_reject'),
    path('<int:request_id>/details/', views.request_detail, name='request_detail'),
]