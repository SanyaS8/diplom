from django.urls import path
from .views import add_profile, delete_profile, my_profile, my_tickets, add_ticket, cancel_ticket

urlpatterns = [
    path('add-profile/', add_profile, name='add_profile'),
    path('delete-profile/', delete_profile, name='delete_profile'),
    path('my-profile/', my_profile, name='my_profile'),
    path('my-tickets/', my_tickets, name='my_tickets'),
    path('add-ticket/', add_ticket, name='add_ticket'),
    path('cancel-ticket/', cancel_ticket, name='cancel_ticket'),
]