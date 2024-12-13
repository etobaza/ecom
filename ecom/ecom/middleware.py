from django.utils.deprecation import MiddlewareMixin
from django.http import JsonResponse
from django.conf import settings

class SecurityMiddleware(MiddlewareMixin):
    def process_request(self, request):
        if settings.DEBUG:
            return None
        if request.path.startswith("/metrics"):
            return None
        if not request.META.get('CSRF_COOKIE'):
            return JsonResponse({'error': 'CSRF token missing'}, status=403)

        if request.path.startswith('/api/auth/') and request.method in ['POST', 'PUT', 'DELETE']:
            if not request.user.is_authenticated:
                return JsonResponse({'error': 'User not authenticated'}, status=401)
        return None

