from django.shortcuts import render

# estimation_app/views.py
from django.shortcuts import render

def estimate_solar_potential(request):
    # This view will handle both displaying the form (GET)
    # and processing the form submission (POST) later
    return render(request, 'estimation_app/estimation_form.html', {})
