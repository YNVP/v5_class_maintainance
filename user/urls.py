from django.urls import path,include
from django.contrib.auth import views as auth_views
from . import views
from django.conf.urls.static import static
from django.contrib import messages
from django.views.generic import TemplateView

urlpatterns = [
    path('',views.land, name='landing_page'),
    path('home/',views.home, name='home'),
    path('view_profile/<str:username>', views.view_profile, name='profile_detail'),
    path('profile/',views.profile, name='profile'),
    # path(r'robots.txt',TemplateView(template_name='robots.txt'))
]

