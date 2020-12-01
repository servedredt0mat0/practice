from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import TemplateView, ListView, DetailView
from django.views.generic.edit import UpdateView, DeleteView, CreateView
from django.urls import reverse_lazy
from .models import Projects, Entry

class HomePageView(TemplateView):
    template_name = 'index.html'

class ProjectListView(ListView, LoginRequiredMixin):
    model = Projects
    template_name = 'forages/project_list.html'

class ProjectDetailView(LoginRequiredMixin, DetailView):
    model = Projects
    template_name = 'forages/project_detail.html'

class ProjectUpdateView(UpdateView, LoginRequiredMixin, UserPassesTestMixin):
    model = Projects
    fields = ('title', 'description', )
    template_name = 'forages/project_edit.html'
    success_url = reverse_lazy('project_list')

    def test_func(self):
        obj = self.get_object()
        return obj.author == self.request.user

class ProjectDeleteView(DeleteView, LoginRequiredMixin, UserPassesTestMixin):
    model = Projects
    template_name = 'forages/project_delete.html'
    success_url = reverse_lazy('project_list')

    def test_func(self):
        obj = self.get_object()
        return obj.author == self.request.user
        
class ProjectCreateView(LoginRequiredMixin, CreateView):
    model = Projects
    template_name = 'forages/project_new.html'
    fields = ('title', 'description',)
    success_url = reverse_lazy('project_list')

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class EntryCreateView(LoginRequiredMixin, CreateView):
    model = Entry
    template_name = 'forages/entry_new.html'
    fields = ('material', 'latitude', 'longitude',)

    def form_valid(self, form):
        form.instance.project_id = self.kwargs["pk"]
        form.instance.author = self.request.user
        return super().form_valid(form)

class EntryUpdateView(UpdateView, LoginRequiredMixin, UserPassesTestMixin):
    model = Entry
    fields = ('material', 'latitude', 'longitude' )
    template_name = 'forages/entry_edit.html'
    success_url = reverse_lazy('project_list')

    def test_func(self):
        obj = self.get_object()
        return obj.author == self.request.user

class EntryDeleteView(DeleteView, LoginRequiredMixin, UserPassesTestMixin):
    model = Entry
    template_name = 'forages/entry_delete.html'
    success_url = reverse_lazy('project_list')

    def test_func(self):
        obj = self.get_object()
        return obj.author == self.request.user