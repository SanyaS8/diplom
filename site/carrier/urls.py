from django.urls import path
from .views import *

urlpatterns = [
    path('add_trip/', add_trip, name='add_trip'),
    path('update_trip/', update_trip, name='update_trip'),
    path('cancel_trip/', cancel_trip, name='cancel_trip'),
    path('delete_trip/', delete_trip, name='delete_trip'),
    path('update_info/', update_carrier_info, name='update_carrier_info'),
]