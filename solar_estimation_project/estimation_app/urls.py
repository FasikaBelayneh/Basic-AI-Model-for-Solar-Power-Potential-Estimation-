# estimation_app/urls.py
from django.urls import path
from . import views

urlpatterns = [
    # Define a URL pattern for your estimation page
    path('estimate/', views.estimate_solar_potential, name='estimate_solar_potential'),
    # You can add a root URL for the app later if needed
    # path('', views.home, name='home'),
]