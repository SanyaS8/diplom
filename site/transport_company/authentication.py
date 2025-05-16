from rest_framework.authentication import BaseAuthentication
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.exceptions import AuthenticationFailed

class GuestJWTAuthentication(BaseAuthentication):
    def authenticate(self, request):
        jwt_token = request.headers.get('Authorization')
        if not jwt_token:
            # Генерация гостевого токена
            guest_token = RefreshToken()
            guest_token['role'] = 'guest'
            return None, {
                'refresh': str(guest_token),
                'access': str(guest_token.access_token),
                'role': 'guest'
            }