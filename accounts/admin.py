from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import CustomUser, Profile

class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = ['email', 'username', 'name', 'age', 'city', 'country', 'is_staff']
    fieldsets = UserAdmin.fieldsets + ((None, {'fields': ('name', 'age', 'city', 'country')}),)
    add_fieldsets = UserAdmin.add_fieldsets + ((None, {'fields': ('name', 'age', 'city', 'country')}),)


admin.site.register(Profile)
admin.site.register(CustomUser, CustomUserAdmin)