from django.shortcuts import render, redirect, get_object_or_404
from .forms import *
from django.contrib import messages
from django.contrib.auth.decorators import login_required
import random
import string
from .models import AttendanceRequest
from django.contrib.auth.models import User
from django.views.generic import CreateView
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.http import HttpResponseRedirect, HttpResponse
from django.utils.timezone import utc
import datetime
from datetime import datetime, date


def all_requests(request):
    requests=AttendanceRequest.objects.filter(user=request.user)
    context={
        'requests':requests
    }
    return render(request, 'attendance_request/all_requests.html', context)

@login_required(login_url='/account/login/')
def create_requuest(request):
    form = RequestForm(request.POST, request.FILES)
    if request.POST and form.is_valid():
        g = form.save(commit=False)
        g.user = request.user
        g.save()
        messages.success(request, f'Your request has been submitted! Your moderator will accept/reject your request based on proof you submitted.')
        return redirect('profile')
    else:
        form = RequestForm()
    return render(request, 'attendance_request/create_request.html', {'form': form})


def request_detail(request, request_id):
    r = AttendanceRequest.objects.get(id=request_id)
    # Seggregating only current user section students
    context = {
        'r': r
    }
    return render(request, 'attendance_request/request_details.html', context)

@login_required(login_url='/account/login/')
def cr_requests(request):
    letters = string.ascii_letters + string.digits
    result_str = ''.join(random.choice(letters) for i in range(8))
    now = datetime.now()
    dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
    if request.user.profile.is_cr:
        requests=AttendanceRequest.objects.filter(user__profile__section=request.user.profile.section).order_by('-start_time')
        request.user.profile.unique_string=result_str+' '+dt_string
        request.user.profile.save()
        messages.success(request, f'Authentication Completed! Unique Key {result_str} {dt_string}. 📝Log can be extracted to irresponsible Verification ✔')
        context={
            'requests':requests
        }
        return render(request, 'attendance_request/cr_requests.html', context)
    else:
        messages.success(request, f'You are not authorized to use this part of portal.{result_str}')
        return redirect('landing_page')


def amc_requests(request):
    letters = string.ascii_letters + string.digits
    result_str = ''.join(random.choice(letters) for i in range(8))
    now = datetime.now()
    dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
    requests=AttendanceRequest.objects.filter(user__profile__section='B13')
    messages.success(request, f'Authentication Completed! Welcome sir.✔')
    context={
        'requests':requests
    }
    return render(request, 'attendance_request/cr_requests.html', context)

def verify_accept(request):
    request_ = get_object_or_404(AttendanceRequest, id=request.POST.get('request_id'))
    if request_.granted==False:
        request_.granted=True
        request_.rejected=False
        request_.save()
    else:
        request_.granted=False
        request_.rejected=True
        request_.save()
    return HttpResponse(request_.granted)

def verify_reject(request):
    request_ = get_object_or_404(AttendanceRequest, id=request.POST.get('request_id'))
    if request_.rejected==False:
        request_.rejected=True
        request_.granted=False
        request_.save()
    else:
        request_.rejected=False
        request._granted=True
        request_.save()
    return HttpResponse(request_.rejected)







