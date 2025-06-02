from rest_framework.permissions import BasePermission

class IsGuest(BasePermission):
    def has_permission(self, request, view):
        return request.auth and request.auth.get('role') == 'guest'