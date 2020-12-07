from django.contrib import admin
from django.forms import Textarea
from django.db import models
from .models import Projects, Entry, Mushrooms, MushroomData

class EntryInline(admin.TabularInline):
    model = Entry

class ProjectAdmin(admin.ModelAdmin):
    inlines = [
        EntryInline,
    ]


admin.site.register(Projects, ProjectAdmin)
admin.site.register(Entry)
admin.site.register(Mushrooms)
admin.site.register(MushroomData)