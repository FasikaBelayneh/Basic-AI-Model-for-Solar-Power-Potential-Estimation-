
from django.test import TestCase, Client
from django.urls import reverse
from django.core.cache import cache

class SolarAppTests(TestCase):
    def setUp(self):
        self.client = Client()
        cache.clear()

    def test_home_page(self):
        response = self.client.get(reverse('predict_solar'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Solar Potential Estimation')

    def test_weather_api_rate_limiting(self):
        url = reverse('get_weather') + '?lat=9&lon=40'
        for _ in range(60):
            response = self.client.get(url)
            self.assertEqual(response.status_code, 200)
        
        response = self.client.get(url)
        self.assertEqual(response.status_code, 429)

    def test_invalid_form_submission(self):
        response = self.client.post(reverse('predict_solar'), {
            'latitude': 100,  # invalid value
            'longitude': 200,
            'month': 13,
            'avg_temp': 'invalid',
            'precipitation': -5,
            'humidity': 150,
            'cloud_cover': 150
        })
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Please enter a value between -90 and 90')

    def test_valid_form_submission(self):
        response = self.client.post(reverse('predict_solar'), {
            'latitude': 9.145,
            'longitude': 40.4897,
            'month': 6,
            'avg_temp': 25,
            'precipitation': 0,
            'humidity': 50,
            'cloud_cover': 20
        })
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'W/m²')