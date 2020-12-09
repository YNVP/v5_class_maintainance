from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm
from .forms import UserUpdateForm, ProfileUpdateForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from .models import Profile
from django.contrib.auth.models import User

from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.http import HttpResponseRedirect, HttpResponse
from django.utils.timezone import utc
import datetime
from datetime import datetime, date
from calendarapp.utils import Calendar

# SITE HOME PAGE


def get_date(req_day):
    if req_day:
        year, month = (int(x) for x in req_day.split('-'))
        return date(year, month, day=1)
    return datetime.today()


def home(request):
    d = get_date(request.GET.get('month', None))
    cal = Calendar(d.year, d.month)
    html_cal = cal.formatmonth(withyear=True)
    if request.user.profile.is_cr:
        message='Welcome CR '+request.user.first_name,
    else:
        message='Welcome '+request.user.first_name,
    context={
        'message':message,
        'main_calendar':html_cal
    }
    return render(request, 'user/base.html', context)


def land(request):
    d = get_date(request.GET.get('month', None))
    cal = Calendar(d.year, d.month)
    html_cal = cal.formatmonth(withyear=True)
    context={
        'calendar':html_cal
    }
    return render(request, 'user/land.html',context)


@login_required
def profile(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST,
                                   request.FILES,
                                   instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, f'Your account has been updated!')
            return redirect('profile')

    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)

    context = {
        'u_form': u_form,
        'p_form': p_form
    }

    return render(request, 'user/profile.html', context)

def view_profile(request, username):
    user = User.objects.get(username=username)
    return render(request, 'user/view_profile.html', {'user': user})


def handler404(request, exception):
    return render(request, 'user/404.html')


def handler500(request):
    return render(request, 'user/500.html')
