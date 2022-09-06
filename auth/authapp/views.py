from http.client import HTTPResponse
from re import template
from django.shortcuts import render, get_object_or_404
from django.views.generic.edit import CreateView
from .forms import *
from django.http import HttpResponseRedirect,JsonResponse, HttpResponse
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect
from django.contrib.sites.shortcuts import get_current_site  
from django.template.loader import render_to_string 
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes
from django.core.mail import EmailMessage
from django.db import IntegrityError
from django.views.generic import ListView, DetailView
from django.views.generic.edit import ModelFormMixin, FormMixin
from django.views import View


# Create your views here.
class LoginPageView(CreateView):
    template_name='login.html'
    form_class=LoginForm
  
    def get(self, request):
        form = self.form_class()
       
        return render(request, self.template_name, context={'form': form})
    
    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            return self.form_valid(form, request)
        else:
            return self.form_invalid(form, request)

    def form_valid(self, form, request):
        user = authenticate(
                username=form.cleaned_data['username'],
                password=form.cleaned_data['password'],
            )
        if user is not None:
            if user.is_active:
                login(request, user)
                return HttpResponse(user.get_username())