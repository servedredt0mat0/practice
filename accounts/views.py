from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView, UpdateView
from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import Profile, CustomUser
from django.shortcuts import render



class SignUpView(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'

class ProfileView(DetailView):
    model = CustomUser 
    template_name = 'profile/profile.html'

class ChangeProfileView(UpdateView):
    form_class = CustomUserChangeForm
    success_url = reverse_lazy('home')
    template_name = 'profile/profile_edit.html'
    def get_object(self):
        return self.request.user

class UpdateProfileView(UpdateView):
    model = Profile
    template_name = 'profile/bio_update.html'
    def get_object(self):
        return self.request.user