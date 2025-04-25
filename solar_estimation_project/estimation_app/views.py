import joblib
import numpy as np
import requests
import warnings
from django.shortcuts import render
from django.http import JsonResponse
from django.conf import settings
from .forms import SolarInputForm
from datetime import datetime

warnings.filterwarnings("ignore", category=UserWarning)
warnings.filterwarnings("ignore", category=DeprecationWarning)

def get_weather(request):
    lat = request.GET.get('lat')
    lon = request.GET.get('lon')
    
    try:
        response = requests.get(
            'https://api.openweathermap.org/data/2.5/weather',
            params={
                'lat': lat,
                'lon': lon,
                'appid': settings.OPENWEATHER_API_KEY,
                'units': 'metric'
            },
            timeout=5
        )
        data = response.json()
        return JsonResponse({
            'temp': data['main']['temp'],
            'humidity': data['main']['humidity'],
            'clouds': data['clouds']['all'],
            'rain': data.get('rain', {}).get('1h', 0)
        })
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=500)

def predict_solar(request):
    if request.method == 'POST':
        form = SolarInputForm(request.POST)
        if form.is_valid():
            try:
                model = joblib.load('estimation_app/ML_Model/solar_potential_model.pkl')
                
                features = np.array([[
                    datetime.now().year,
                    form.cleaned_data['month'],
                    form.cleaned_data['avg_temp'],
                    form.cleaned_data['avg_temp'] + 5,
                    form.cleaned_data['avg_temp'] - 5,
                    form.cleaned_data['precipitation'],
                    form.cleaned_data['humidity'],
                    4.5,
                    form.cleaned_data['cloud_cover'],
                    415,
                    form.cleaned_data['latitude'],
                    form.cleaned_data['longitude'],
                    150,
                    10,
                    0.5,
                    0.7,
                    0.2,
                    25,
                    28
                ]])

                prediction = model.predict(features)[0]
                efficiency_percent = (prediction / 300) * 100
                usable_energy = prediction * 0.85
                system_losses = prediction * 0.15

                seasonal_values = [
                    int(prediction * 0.56),
                    int(prediction * 0.63),
                    int(prediction * 0.72),
                    int(prediction * 0.85),
                    int(prediction * 0.95),
                    int(prediction * 1.1),
                    int(prediction * 1.25),
                    int(prediction * 1.15),
                    int(prediction * 0.92),
                    int(prediction * 0.78),
                    int(prediction * 0.65),
                    int(prediction * 0.58)
                ]

                context = {
                    'prediction': round(prediction, 2),
                    'month_name': datetime(2000, int(form.cleaned_data['month']), 1).strftime('%B'),
                    'seasonal_months': ['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec'],
                    'seasonal_values': seasonal_values,
                    'cost_savings': round(prediction * 0.15 * 365, 2),
                    'lat': form.cleaned_data['latitude'],
                    'lon': form.cleaned_data['longitude'],
                    'status': 'Excellent' if prediction >= 200 else 'Good' if prediction >= 100 else 'Moderate' if prediction >= 50 else 'Poor',
                    'regional_avg': round(prediction * 0.85, 2),
                    'efficiency_percent': efficiency_percent,
                    'usable_energy': round(usable_energy, 2),
                    'system_losses': round(system_losses, 2),
                    'recommendation': {
                        'panels': f"{int(prediction/50)}kW Solar System",
                        'battery': f"{int(prediction/20)}kWh Storage",
                        'incentives': f"{int(efficiency_percent)}% Tax Credit"
                    }
                }

                return render(request, 'estimation_app/result.html', context)

            except Exception as e:
                form.add_error(None, f"Prediction failed: {str(e)}")
                return render(request, 'estimation_app/estimation_form.html', {'form': form})
        
        return render(request, 'estimation_app/estimation_form.html', {'form': form})
    
    form = SolarInputForm(initial={'month': datetime.now().month})
    return render(request, 'estimation_app/estimation_form.html', {'form': form})