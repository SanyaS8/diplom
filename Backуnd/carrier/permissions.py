from rest_framework.permissions import BasePermission

class IsCarrier(BasePermission):
    def has_permission(self, request, view):
        return request.auth and request.auth.get('role') == 'carrier'