# cal/views.py

from datetime import datetime, date
from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.views import generic
from django.utils.safestring import mark_safe
from datetime import timedelta
import calendar
from django.shortcuts import get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from .filters import *
from .models import *
from .utils import Calendar
from .forms import EventForm, AddMemberForm,AddLatestNewsForm
import csv
from django.contrib.auth.models import User
from django.db.models import F
from decimal import Decimal
from django.contrib.auth.models import User

def get_date(req_day):
    if req_day:
        year, month = (int(x) for x in req_day.split('-'))
        return date(year, month, day=1)
    return datetime.today()

def prev_month(d):
    first = d.replace(day=1)
    prev_month = first - timedelta(days=1)
    month = 'month=' + str(prev_month.year) + '-' + str(prev_month.month)
    return month

def next_month(d):
    days_in_month = calendar.monthrange(d.year, d.month)[1]
    last = d.replace(day=days_in_month)
    next_month = last + timedelta(days=1)
    month = 'month=' + str(next_month.year) + '-' + str(next_month.month)
    return month

class CalendarView(LoginRequiredMixin, generic.ListView):
    login_url = 'account_login'
    model = Event
    template_name = 'calendarapp/calendar.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        d = get_date(self.request.GET.get('month', None))
        cal = Calendar(d.year, d.month)
        html_cal = cal.formatmonth(withyear=True)
        context['calendar'] = mark_safe(html_cal)
        context['prev_month'] = prev_month(d)
        context['next_month'] = next_month(d)
        return context

@login_required(login_url='account_signup')
def create_event(request):
    form = EventForm(request.POST or None)
    if request.POST and form.is_valid():
        title = form.cleaned_data['title']
        description = form.cleaned_data['description']
        start_time = form.cleaned_data['start_time']
        end_time = form.cleaned_data['end_time']
        next_level = form.cleaned_data['next_level']
        cgpa = form.cleaned_data['cgpa']
        tenth = form.cleaned_data['tenth']
        inter = form.cleaned_data['inter']
        Event.objects.get_or_create(
            user=request.user,
            title=title,
            description=description,
            start_time=start_time,
            end_time=end_time,
            next_level=next_level,
            cgpa=cgpa,
            tenth=tenth,
            inter=inter,
        )
        event=Event.objects.get(title=title)
        EventMembers.objects.create(event=event)
        return HttpResponseRedirect(reverse('calendarapp:calendar'))
    return render(request, 'calendarapp/event.html', {'form': form})

class EventEdit(generic.UpdateView):
    model = Event
    fields = ['title', 'description', 'start_time', 'end_time', 'next_level','tenth','inter','cgpa','disable_add','is_completed']
    template_name = 'calendarapp/event.html'

@login_required(login_url='/account/login/')
def event_details(request, event_id):
    event = Event.objects.get(id=event_id)
    print(event)
    eventmembers = EventMembers.objects.get(event=event)
    # Seggregating only current user section students
    eventmembers = eventmembers.students.filter(profile__section=request.user.profile.section,)#profile__cgpa__gte=event.cgpa,profile__tenth__gte=Decimal.from_float(event.tenth/9.5),profile__inter__gte=Decimal.from_float(event.inter/0.1)
    users = ClassFilter(request.GET, queryset=Profile.objects.filter(section=request.user.profile.section)) #cgpa__gte = event.cgpa,tenth__gte = Decimal.from_float(event.tenth/9.5),inter__gte = Decimal.from_float(event.inter/0.1)
    context = {
        'event':event,
        'eventmembers': eventmembers,
        'users':users,
    }
    return render(request, 'calendarapp/event-details.html', context)


def add_eventmember(request, event_id):
    forms = AddMemberForm()
    if request.method == 'POST':
        forms = AddMemberForm(request.POST)
        if forms.is_valid():
            member = EventMember.objects.filter(event=event_id)
            event = Event.objects.get(id=event_id)
            curr_class = forms.cleaned_data['get_classes']
            get_rollnos = forms.cleaned_data['get_rolls']
            get_rollnos = get_rollnos.split(',')
            curr_year = str(datetime.today().year-3)[2:]
            for i in get_rollnos:
                if len(i) == 1:
                    rollno = '12'+curr_year+'103'+curr_class+'00'+i
                else:
                    rollno = '12'+curr_year+'103'+curr_class+'0'+i
                get_user = User.objects.filter(rollno=rollno)
                event.students.add(user=get_user)

    context = {
        'form': forms
    }
    return render(request, 'calendarapp/add_member.html', context)


class EventMemberDeleteView(generic.DeleteView):
    model = EventMembers
    template_name = 'calendarapp/event_delete.html'
    success_url = reverse_lazy('calendarapp:calendar')


def add_student_to_event(request):
    user = get_object_or_404(User, id=request.POST.get('user_id'))
    event = get_object_or_404(Event, id=request.POST.get('event_id'))
    user.profile.num_drives_attempt=user.profile.num_drives_attempt+1
    event_members=EventMembers.objects.get(event=event)

    if event_members.students.filter(id=user.id).exists():
        user.profile.current_events.remove(event)
        event_members.students.remove(user)
        user.profile.save()
        data='r'
        return HttpResponse(data)
    else:
        user.profile.current_events.add(event)
        event_members.students.add(user)
        user.profile.save()
        data='a'
        return HttpResponse(data)



def export_presentees_csv(request, event_id):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="attendance_presentees.csv"'

    writer = csv.writer(response)
    event = Event.objects.get(id=event_id)
    writer.writerow(['EVENT TITLE', 'EVENT DESCRIPTION', 'EVENT START TIME'])
    writer.writerow([event.title, event.description, str(event.start_time)])
    writer.writerow(['Roll_No', 'NAME', 'CGPA'])
    users = EventMembers.objects.get(event=event).students.filter(profile__section=request.user.profile.section,).values_list('profile__roll_no', 'first_name', 'profile__cgpa')
    for user in users:
        writer.writerow(user)
    return response

def export_absentees_csv(request, event_id):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="attendance_absentees.csv"'

    writer = csv.writer(response)
    event = Event.objects.get(id=event_id)
    writer.writerow(['EVENT TITLE', 'EVENT DESCRIPTION', 'EVENT START TIME'])
    writer.writerow([event.title, event.description, str(event.start_time)])
    writer.writerow(['Roll_No'])
    users=User.objects.filter(profile__section=request.user.profile.section)
    users_set=list([str(user.profile.roll_no) for user in users])
    presentees = EventMembers.objects.get(event=event).students.filter(profile__section=request.user.profile.section,)
    presentees_set = list([str(user.profile.roll_no) for user in presentees])
    absentees=[user for user in users_set if user not in presentees_set]
    for user in absentees:
        writer.writerow([user])
    return response

@login_required(login_url='/account/login/')
def add_latest_news(request):
    form = AddLatestNewsForm(request.POST)
    if request.method == 'POST':
        form = AddLatestNewsForm(request.POST)
        if form.is_valid():
            end_time = form.cleaned_data['end_time']
            post_data = form.cleaned_data['post_data']
            AddLatestNews.objects.get_or_create(
                end_time=end_time,
                post_data = post_data,)
        return HttpResponseRedirect(reverse('calendarapp:calendar'))
    context = {
        'form': form
    }
    return render(request, 'calendarapp/add_news.html', context)


