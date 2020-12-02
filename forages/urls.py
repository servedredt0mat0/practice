from django.urls import path
from .views import HomePageView, ProjectListView, ProjectUpdateView, ProjectDetailView, ProjectDeleteView, ProjectCreateView, EntryCreateView, EntryDeleteView, EntryUpdateView, EntryDetailView, LikeView
from . import views
urlpatterns = [ 
    path('', HomePageView.as_view(), name='home'),
    path('projects/', ProjectListView.as_view(), name='project_list'),
 #   path('edit/<int:pk>/', ProjectUpdateView.as_view(), name='project_edit'),
    path('<int:pk>/', ProjectDetailView.as_view(), name='project_detail'),
 #   path('delete/<int:pk>/', ProjectDeleteView.as_view(), name='project_delete'),
    path('new/', ProjectCreateView.as_view(), name='project_new'),
    path('<int:pk>/new-entry/', EntryCreateView.as_view(), name='entry_new'),
 #   path('delete_entry/<int:pk>/', EntryDeleteView.as_view(), name='entry_delete'),
 #   path('update_entry/<int:pk>/', EntryUpdateView.as_view(), name='entry_edit'),
    path('detail/<int:pk>/', EntryDetailView.as_view(), name='entry_detail'),
 #   path('pie_chart/', views.pie_chart, name='pie_chart'),
   path('like/<int:pk>', LikeView, name="like_project"),

]