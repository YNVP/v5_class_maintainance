from django.shortcuts import render, get_object_or_404,redirect
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.models import User
from django.views.generic import (
    ListView,
    CreateView,
    UpdateView,
    DeleteView
)
from django.contrib.auth.decorators import login_required
from .models import *
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .forms import *
from django.contrib.auth.decorators import login_required


@login_required
def home(request):
   #Querying required data
    contact_list = Contact.objects.filter(section=request.user.profile.section).order_by('-date_posted')
    #Sending data to page
    context={
        "contacts":contact_list,
    }
    return render(request, 'contacts/home.html', context)



@login_required
def contact_create(request):
    if request.method == 'POST':
        contact_form = ContactForm(request.POST,user=request.user)
        if contact_form.is_valid():
            contact_form.instance.creator = request.user
            contact_form.save()
            return redirect('contact-home')
    else:
        contact_form = ContactForm(user=request.user)
        context = {'form':contact_form}
        return render(request,'contacts/contact_form.html',context=context)


class ContactUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Contact
    fields = ['name', 'number']

    def form_valid(self, form):
        form.instance.creator = self.request.user
        return super().form_valid(form)

    def test_func(self):
        contact = self.get_object()
        if self.request.user == post.author:
            return True
        return False


class ContactDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Contact
    success_url = '/contact'

    def test_func(self):
        contact = self.get_object()
        if self.request.user == contact.author:
            return True
        return False
