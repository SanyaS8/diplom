from django.urls import path, include
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from .views import list_of_cities, search_trips_by_cities, exit, login, register_user, search_trips_all, search_trips_airplane, search_trips_train, search_trips_bus

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
    path('api/search_trips/all/', search_trips_all, name='search_trips_all'),
    path('api/search_trips/airplane/', search_trips_airplane, name='search_trips_airplane'),
    path('api/search_trips/train/', search_trips_train, name='search_trips_train'),
    path('api/search_trips/bus/', search_trips_bus, name='search_trips_bus'),
]
