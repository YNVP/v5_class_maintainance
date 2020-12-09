from django.shortcuts import render, get_object_or_404,redirect
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.models import User
from django.views.generic import (
    UpdateView,
    DeleteView
)
from django.contrib.auth.decorators import login_required
from .models import Meeting
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .forms import *
import string
import random
from django.core.mail import send_mail


def random_string_generator(size = 30, chars = string.ascii_lowercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))

@login_required
def meeting_create(request):
    if request.method == 'POST':
        meeting_form = MeetingForm(request.POST, request.FILES)
        if meeting_form.is_valid():
            g=meeting_form.save()
            g.slug=random_string_generator()
            g.save()
            for u in request.user.profile.team.team_members.all():
                send_mail(
                    'Team Meeting '+str(g.start_time),
                     '\nTeam Leader requests you to join meeting: \n'+'Agenda:' +g.agenda + '\nLink to join :' +g.link + '\nStart Time :'+ str(g.start_time)+ '\n',
                    'nagavarapradeepyendluri@gmail.com',
                    [u.email],
                    fail_silently=False,
                )
            request.user.profile.team.meetings.add(g)
            return redirect('/')
    else:
        meeting_form = MeetingForm(user=request.user)
        context = {'form':meeting_form}
        return render(request,'meeting/meeting_form.html',context=context)


class MeetingUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Meeting
    fields = ['team_name','team_instructor','subject','team_members','image','project_name','project_field','project_level']

    def form_valid(self, form):
        return super().form_valid(form)

    def test_func(self):
        team = self.get_object()
        if self.request.user.first_name == team.team_leader:
            return True
        return False

class MeetingDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Meeting
    success_url = '/'
    def test_func(self):
        team = self.get_object()
        if self.request.user.first_name == team.team_leader:
            return True
        return False
