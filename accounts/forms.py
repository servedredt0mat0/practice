from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser, Profile

class CustomUserCreationForm(UserCreationForm):

    class Meta(UserCreationForm):
        model = CustomUser
        fields = ('username', 'email', 'name', 'age', 'city', 'country')

class CustomUserChangeForm(UserChangeForm):
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control'}))
    name = forms.CharField(max_length=255, widget=forms.TextInput(attrs={'class': 'form-control'}))
    age = forms.IntegerField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    city = forms.CharField(max_length=255, widget=forms.TextInput(attrs={'class': 'form-control'}))
    country = forms.CharField(max_length=3, widget=forms.TextInput(attrs={'class': 'form-control'}))

    class Meta(UserChangeForm):
        model = CustomUser
        fields = ('username', 'email', 'name', 'age', 'city', 'country')

