from django import forms

class SolarInputForm(forms.Form):
    latitude = forms.FloatField(label='Latitude', min_value=-90, max_value=90)
    longitude = forms.FloatField(label='Longitude', min_value=-180, max_value=180)
    month = forms.IntegerField(label='Month', min_value=1, max_value=12)
    avg_temp = forms.FloatField(label='Average Temperature (°C)')
    precipitation = forms.FloatField(label='Precipitation (mm)')
    humidity = forms.FloatField(label='Humidity (%)')
    cloud_cover = forms.FloatField(label='Cloud Cover (%)')