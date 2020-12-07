from django.contrib import admin
from django.forms import Textarea
from django.db import models
from .models import Projects, Entry

class EntryInline(admin.TabularInline):
    model = Entry

class ProjectAdmin(admin.ModelAdmin):
    inlines = [
        TabularInline,
    ]


admin.site.register(Projects, ProjectAdmin)
admin.site.register(Entry)