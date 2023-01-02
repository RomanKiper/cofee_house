from django.contrib.auth.views import LoginView, LogoutView
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView

from .forms import RegisterForm, LoginForm

class RegisterCreateView(CreateView):
    form_class = RegisterForm
    success_url = reverse_lazy('signin')
    template_name = 'registration/signup.html'


class SignInView(LoginView):
    form_class = LoginForm
    template_name = 'registration/signin.html'
    success_url = reverse_lazy('index')