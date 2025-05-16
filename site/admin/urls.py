from django.urls import path
from .views import list_of_users, list_of_carriers, list_of_trips, delete_user, delete_carrier, delete_trip, create_carrier

urlpatterns = [
    path('list-of-users/', list_of_users, name='list_of_users'),
    path('list-of-carriers/', list_of_carriers, name='list_of_carriers'),
    path('list-of-trips/', list_of_trips, name='list_of_trips'),
    path('delete-user/', delete_user, name='delete_user'),
    path('delete-carrier/', delete_carrier, name='delete_carrier'),
    path('delete-trip/', delete_trip, name='delete_trip'),
    path('create-carrier/', create_carrier, name='create_carrier'),
]