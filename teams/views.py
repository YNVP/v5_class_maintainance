from django.shortcuts import render, get_object_or_404,redirect
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.models import User
from django.views.generic import (
    UpdateView,
    DeleteView
)
from django.contrib.auth.decorators import login_required
from .models import Team
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .forms import *
import string
import random

def random_string_generator(size = 30, chars = string.ascii_lowercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))

def team_detail(request, slug):
    team=Team.objects.get(slug=slug)
    return render(request, 'teams/team_detail.html',{'team':team})

@login_required
def team_create(request):
    if request.method == 'POST':
        team_form = TeamForm(request.POST, request.FILES)
        if team_form.is_valid():
            team_form.instance.team_leader = request.user.first_name
            g=team_form.save()
            g.slug=random_string_generator()
            team=Team.objects.get(id=g.id)
            for u in g.team_members.all():
                u.profile.team=team
                u.profile.save()
            g.save()
            return redirect('/')
    else:
        team_form = TeamForm(user=request.user)
        context = {'form':team_form}
        return render(request,'teams/team_form.html',context=context)


class TeamUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Team
    fields = ['team_name','team_instructor','subject','team_members','image','project_name','project_field','project_level']

    def form_valid(self, form):
        return super().form_valid(form)

    def test_func(self):
        team = self.get_object()
        if self.request.user.first_name == team.team_leader:
            return True
        return False

class TeamDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Team
    success_url = '/'
    def test_func(self):
        team = self.get_object()
        if self.request.user.first_name == team.team_leader:
            return True
        return False

def all_teams(request):
    teams=Team.objects.all()
    return render(request,'teams/all_teams.html', {'teams':teams})

