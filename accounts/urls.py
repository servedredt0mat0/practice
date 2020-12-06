from django.urls import path
from .views import SignUpView, ChangeProfileView, ProfileView
from django.conf import settings
from django.conf.urls.static import static



urlpatterns = [
    path('signup/', SignUpView.as_view(), name='signup'),
    path('<int:pk>/profile_edit/', ChangeProfileView.as_view(), name='profile_edit'),
    path('<int:pk>/profile/', ProfileView.as_view(), name='profile'),
    
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
