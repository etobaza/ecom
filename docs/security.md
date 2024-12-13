# Security Protocols

This document describes the security strategies employed to protect user login and registration functionalities within the Django application.

## Security Middleware

The `SecurityMiddleware` is crafted to apply security protocols to requests targeting sensitive endpoints.

### Middleware Implementation

```python
from django.utils.deprecation import MiddlewareMixin
from django.http import JsonResponse

class SecurityMiddleware(MiddlewareMixin):
    def process_request(self, request):
        if not request.META.get('CSRF_COOKIE'):
            return JsonResponse({'error': 'CSRF token missing'}, status=403)

        if request.path.startswith('/api/auth/') and request.method in ['POST', 'PUT', 'DELETE']:
            if not request.user.is_authenticated:
                return JsonResponse({'error': 'User not authenticated'}, status=401)
```

## Secure User Login (POST /api/auth/login/)

The login view manages user authentication utilizing a username and password.

### Implementation

```python
from django.contrib.auth import authenticate, login
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return JsonResponse({'message': 'Login successful'})
        else:
            return JsonResponse({'error': 'Invalid credentials'}, status=400)
```

## Secure User Registration (POST /api/auth/register/)

The registration view manages the creation of users, requiring a username, password, and email.

### Implementation

```python
from django.contrib.auth.models import User
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def register_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        email = request.POST.get('email')

        if User.objects.filter(username=username).exists():
            return JsonResponse({'error': 'Username already taken'}, status=400)

        user = User.objects.create_user(username=username, password=password, email=email)
        user.save()
        return JsonResponse({'message': 'User registered successfully'})
```
