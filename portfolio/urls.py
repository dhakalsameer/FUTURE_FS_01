from django.urls import path
from .views import home, about, projects, contact, contact_send_email, health_check

urlpatterns = [
    path('', home, name='home'),
    path('about/', about, name='about'),
    path('projects/', projects, name='projects'),
    path('contact/', contact, name='contact'),
    path('contact-send/', contact_send_email, name='contact_send_email'),
    path('health/', health_check, name='health_check'),
]
