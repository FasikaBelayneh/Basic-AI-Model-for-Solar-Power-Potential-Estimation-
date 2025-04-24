# solar_app/forms.py
from django import forms
from django.core.validators import MinValueValidator, MaxValueValidator

class SolarInputForm(forms.Form):
    latitude = forms.FloatField(
        label='Latitude',
        validators=[MinValueValidator(-90), MaxValueValidator(90)],
        widget=forms.NumberInput(attrs={'step': '0.0001'})
    )
    longitude = forms.FloatField(
        label='Longitude',
        validators=[MinValueValidator(-180), MaxValueValidator(180)],
        widget=forms.NumberInput(attrs={'step': '0.0001'})
    )
    month = forms.IntegerField(
        label='Month',
        validators=[MinValueValidator(1), MaxValueValidator(12)],
        widget=forms.NumberInput(attrs={'min': '1', 'max': '12'})
    )
    avg_temp = forms.FloatField(
        label='Average Temperature (°C)',
        widget=forms.NumberInput(attrs={'step': '0.1'})
    )
    precipitation = forms.FloatField(
        label='Precipitation (mm)',
        min_value=0,
        widget=forms.NumberInput(attrs={'step': '0.1'})
    )
    humidity = forms.FloatField(
        label='Humidity (%)',
        validators=[MinValueValidator(0), MaxValueValidator(100)],
        widget=forms.NumberInput(attrs={'step': '0.1'})
    )
    cloud_cover = forms.FloatField(
        label='Cloud Cover (%)',
        validators=[MinValueValidator(0), MaxValueValidator(100)],
        widget=forms.NumberInput(attrs={'step': '0.1'})
    )