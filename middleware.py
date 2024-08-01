from django.http import JsonResponse
from django.urls import resolve
from django.utils.deprecation import MiddlewareMixin

import jwt

from ChatbotAPI.models import User

#Verify Token Middleware
class TokenVerificationMiddleware(MiddlewareMixin):
    EXEMPT_VIEWS = [
        'register',
        'login'
    ]

    def process_request(self, request):
        current_view = resolve(request.path_info).view_name

        if current_view in self.EXEMPT_VIEWS:
            return None

        auth_header = request.headers.get('Authorization')
        if not auth_header:
            return JsonResponse({'error': 'Authorization header missing'}, status=401)

        token = auth_header.split(' ')[1] if auth_header else None
        print(f'{token} omooooo')
        if not token:
            return JsonResponse({'error': 'Token missing'}, status=401)

        try:

            payload = jwt.decode(token, 'secret', algorithms=['HS256'])
        except jwt.ExpiredSignatureError:
            return JsonResponse({'error': 'Token has expired'}, status=401)
        except jwt.InvalidTokenError:
            return JsonResponse({'error': 'Invalid token'}, status=401)

        user = User.objects.filter(id=payload['id']).first()
        if user is None:
            return JsonResponse({'error': 'User not found'}, status=401)
        request.user = user
