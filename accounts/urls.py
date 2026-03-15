from django.urls import path
from .views import RegisterView, ProfileView, GuestSessionView

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('profile/', ProfileView.as_view(), name='profile'),
    path('guest/', GuestSessionView.as_view(), name='guest-session'),
]