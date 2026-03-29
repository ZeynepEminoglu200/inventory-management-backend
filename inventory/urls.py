from django.urls import path
from .views import RegisterView
# creating my endpointds here
urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
]