import joblib
import numpy as np
from django.shortcuts import render
from .forms import SolarInputForm

def predict_solar(request):
    if request.method == 'POST':
        form = SolarInputForm(request.POST)
        if form.is_valid():
            # Load trained model
            model = joblib.load('solar_app/ml_model/solar_potential_model.pkl')
            
            # Create feature array
            features = np.array([
                [
                    2023,  # Year
                    form.cleaned_data['month'],
                    form.cleaned_data['avg_temp'],
                    form.cleaned_data['avg_temp'] + 5,  # Max temp (example)
                    form.cleaned_data['avg_temp'] - 5,  # Min temp (example)
                    form.cleaned_data['precipitation'],
                    form.cleaned_data['humidity'],
                    4.5,  # Wind speed (default)
                    form.cleaned_data['cloud_cover'],
                    415,  # CO2 concentration (typical value)
                    form.cleaned_data['latitude'],
                    form.cleaned_data['longitude'],
                    150,  # Altitude (default)
                    10,   # Proximity to water
                    0.5,  # Urbanization index
                    0.7,  # Vegetation index
                    0.2,  # ENSO index
                    25,   # Particulate matter
                    28    # Sea surface temp
                ]
            ])
            
            # Make prediction
            prediction = model.predict(features)
            
            return render(request, 'solar_app/result.html', {
                'prediction': round(prediction[0], 2)
            })
    
    else:
        form = SolarInputForm()
    
    return render(request, 'solar_app/input_form.html', {'form': form})