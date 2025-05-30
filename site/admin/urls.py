from django.urls import path
from .views import list_of_users, list_of_carriers, list_of_trips, delete_user, delete_carrier, delete_trip, create_carrier, list_of_profiles, delete_profile, search_profile, list_of_tickets, search_tickets, search_users, search_trips, search_carrier

urlpatterns = [
    path('list-of-users/', list_of_users, name='list_of_users'),
    path('list-of-carriers/', list_of_carriers, name='list_of_carriers'),
    path('list-of-trips/', list_of_trips, name='list_of_trips'),
    path('delete-user/', delete_user, name='delete_user'),
    path('delete-carrier/', delete_carrier, name='delete_carrier'),
    path('delete-trip/', delete_trip, name='delete_trip'),
    path('create-carrier/', create_carrier, name='create_carrier'),
    path('list-of-profiles/', list_of_profiles, name='list_of_profiles'),
    path('delete-profile/', delete_profile, name='delete_profile'),
    path('search-profile/', search_profile, name='search_profile'),
    path('list-of-tickets/', list_of_tickets, name='list_of_tickets'),
    path('search-tickets/', search_tickets, name='search_tickets'),
    path('search-users/', search_users, name='search_users'),
    path('search-trips/', search_trips, name='search_trips'),
    path('search-carrier/', search_carrier, name='search_carrier'),
]