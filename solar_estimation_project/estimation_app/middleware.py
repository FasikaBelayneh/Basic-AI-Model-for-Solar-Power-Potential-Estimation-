
from django.core.cache import cache
from django.http import JsonResponse
from django.conf import settings

class RateLimitMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if request.path == '/get_weather/':
            ip = request.META.get('REMOTE_ADDR')
            cache_key = f'weather_requests_{ip}'
            requests = cache.get(cache_key, 0)
            
            if requests >= 60:  # 60 requests per hour
                return JsonResponse(
                    {'error': 'Rate limit exceeded. Try again later.'},
                    status=429
                )
            
            cache.set(cache_key, requests + 1, 3600)  # 1 hour expiration
        
        return self.get_response(request)