from django.shortcuts import render
from django.contrib.auth import login, logout
from django.views.generic import CreateView
from django.core.urlresolvers import reverse_lazy

from . import forms
# Create your views here.
class SignUp(CreateView):
    form_class = forms.UserForm
    success_url = reverse_lazy("login")
    template_name = "accounts/signup.html"
