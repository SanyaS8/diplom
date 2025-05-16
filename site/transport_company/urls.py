from django.urls import path, include
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from .views import list_of_cities, search_trips_by_cities, exit, login, register_user

urlpatterns = [
    path('api/user/', include('user.urls')),
    path('api/carrier/', include('carrier.urls')),
    path('api/admin/', include('admin.urls')),
    path('api/list_of_cities/', list_of_cities, name='list_of_cities'),
    path('api/search_trips/', search_trips_by_cities, name='search_trips_by_cities'),
    path('api/exit/', exit, name='exit'),
    path('api/login/', login, name='login'),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/register/', register_user, name='register_user'),
]
