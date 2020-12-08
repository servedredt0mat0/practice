from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView, UpdateView
from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import Profile, CustomUser
from django.shortcuts import render, reverse, redirect, HttpResponseRedirect
from django.contrib.auth import get_user_model


class SignUpView(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'

class ProfileView(DetailView, LoginRequiredMixin):
    model = CustomUser 
    template_name = 'profile/profile.html'

class ChangeProfileView(UpdateView, LoginRequiredMixin):
    form_class = CustomUserChangeForm
    success_url = reverse_lazy('project_list')
    template_name = 'profile/profile_edit.html'

    def get_success_url(self):
        return reverse_lazy('profile', kwargs = {'pk':self.kwargs['pk']})


    def get_object(self):
        return self.request.user

class UpdateProfileView(UpdateView, LoginRequiredMixin, UserPassesTestMixin):
    model = Profile
    template_name = 'profile/bio_update.html'

    def get_object(self):
        return self.request.user