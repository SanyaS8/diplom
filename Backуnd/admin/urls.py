from django.urls import path
from .views import list_of_users, list_of_carriers, list_of_trips, delete_user, delete_carrier, delete_trip, create_carrier, list_of_profiles, delete_profile, search_profile, list_of_tickets, search_tickets, search_users, search_trips, search_carrier

urlpatterns = [
    path('list_of_users/', list_of_users, name='list_of_users'),
    path('list_of_carriers/', list_of_carriers, name='list_of_carriers'),
    path('list_of_trips/', list_of_trips, name='list_of_trips'),
    path('delete_user/', delete_user, name='delete_user'),
    path('delete_carrier/', delete_carrier, name='delete_carrier'),
    path('delete_trip/', delete_trip, name='delete_trip'),
    path('create_carrier/', create_carrier, name='create_carrier'),
    path('list_of_profiles/', list_of_profiles, name='list_of_profiles'),
    path('delete_profile/', delete_profile, name='delete_profile'),
    path('search_profile/', search_profile, name='search_profile'),
    path('list_of_tickets/', list_of_tickets, name='list_of_tickets'),
    path('search_tickets/', search_tickets, name='search_tickets'),
    path('search_users/', search_users, name='search_users'),
    path('search_trips/', search_trips, name='search_trips'),
    path('search_carrier/', search_carrier, name='search_carrier'),
]