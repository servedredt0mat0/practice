from django.contrib import admin
from .models import Projects, Entry

class EntryInline(admin.TabularInline):
    model = Entry

class ProjectAdmin(admin.ModelAdmin):
    inlines = [
        EntryInline,
    ]

admin.site.register(Projects, ProjectAdmin)
admin.site.register(Entry)