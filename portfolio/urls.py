from django import views
from django.urls import path
from .views import home

urlpatterns = [
    path('', home, name='home'),
   path("contact-send/", views.contact_send_email, name="contact_send_email")
]
