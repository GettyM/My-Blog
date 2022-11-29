from django.urls import path
from . views import UserRegistrationView

# we are using as_view function because we are using class based views
urlpatterns = [
    path('register/', UserRegistrationView.as_view(), name='register'),
]
