from django.contrib import admin
from django.forms import Textarea
from django.db import models
from .models import Projects, Entry

class EntryInline(admin.TabularInline):
    model = Entry

class ProjectAdmin(admin.ModelAdmin):
    inlines = [
        EntryInline,
    ]

class EntryAdmin(admin.ModelAdmin):
    formfield_overrides = {
        models.TextField: {'widget': Textarea(attrs={'rows':5, 'cols':23})},
    }

admin.site.register(Projects, ProjectAdmin)
admin.site.register(Entry, EntryAdmin)