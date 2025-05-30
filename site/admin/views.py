from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from transport_company.models import Administrators, Carriers, Trips, Users, Profiles, Tickets
from .permissions import IsAdmin
import hashlib
import os


@permission_classes([IsAdmin])
@api_view(['GET'])
def list_of_users(request):
    try:
        users = Users.objects.all()
        users_data = [
            {
                'user_id': user.user_id,
                'email': user.email,
                'created_at': user.created_at
            }
            for user in users
        ]
        return Response({'users': users_data}, status=200)
    except Exception as e:
        return Response({'error': str(e)}, status=500)

@permission_classes([IsAdmin])
@api_view(['GET'])
def list_of_carriers(request):
    try:
        carriers = Carriers.objects.all()
        carriers_data = [
            {
                'carrier_id': carrier.carrier_id,
                'name': carrier.name,
                'email': carrier.email,
                'phone': carrier.phone
            }
            for carrier in carriers
        ]
        return Response({'carriers': carriers_data}, status=200)
    except Exception as e:
        return Response({'error': str(e)}, status=500)

@permission_classes([IsAdmin])
@api_view(['GET'])
def list_of_trips(request):
    try:
        trips = Trips.objects.all()
        trips_data = [
            {
                'trip_id': trip.trip_id,
                'route': {
                    'departure_city': trip.route.departure_city.name,
                    'arrival_city': trip.route.arrival_city.name
                },
                'vehicle': {
                    'type': trip.vehicle.type,
                    'model': trip.vehicle.model,
                    'vehicle_number': trip.vehicle.vehicle_number
                },
                'departure_time': trip.departure_time,
                'arrival_time': trip.arrival_time,
                'base_price': trip.base_price,
                'status': trip.status,
                'distance_km': trip.distance_km
            }
            for trip in trips
        ]
        return Response({'trips': trips_data}, status=200)
    except Exception as e:
        return Response({'error': str(e)}, status=500)

@permission_classes([IsAdmin])
@api_view(['GET'])
def list_of_profiles(request):
    try:
        profiles = Profiles.objects.all().order_by('profile_id')
        profiles_data = [
            {
                'profile_id': profile.profile_id,
                'full_name': f"{profile.first_name} {profile.last_name}",
                'phone': profile.phone,
                'account_id': profile.user_id
            }
            for profile in profiles
        ]
        return Response({'profiles': profiles_data}, status=200)
    except Exception as e:
        return Response({'error': str(e)}, status=500)

@permission_classes([IsAdmin])
@api_view(['DELETE'])
def delete_user(request):
    try:
        user_id = request.data.get('user_id')
        if not user_id:
            return Response({'error': 'user_id is required'}, status=400)

        if not Users.objects.filter(user_id=user_id).exists():
            return Response({'error': 'User does not exist'}, status=404)

        Users.objects.filter(user_id=user_id).delete()
        return Response({'message': 'User deleted successfully'}, status=200)
    except Exception as e:
        return Response({'error': str(e)}, status=500)

@permission_classes([IsAdmin])
@api_view(['DELETE'])
def delete_carrier(request):
    try:
        carrier_id = request.data.get('carrier_id')
        if not carrier_id:
            return Response({'error': 'carrier_id is required'}, status=400)

        if not Carriers.objects.filter(carrier_id=carrier_id).exists():
            return Response({'error': 'Carrier does not exist'}, status=404)

        Carriers.objects.filter(carrier_id=carrier_id).delete()
        return Response({'message': 'Carrier deleted successfully'}, status=200)
    except Exception as e:
        return Response({'error': str(e)}, status=500)

@permission_classes([IsAdmin])
@api_view(['DELETE'])
def delete_trip(request):
    try:
        trip_id = request.data.get('trip_id')
        if not trip_id:
            return Response({'error': 'trip_id is required'}, status=400)

        if not Trips.objects.filter(trip_id=trip_id).exists():
            return Response({'error': 'Trip does not exist'}, status=404)

        Trips.objects.filter(trip_id=trip_id).delete()
        return Response({'message': 'Trip deleted successfully'}, status=200)
    except Exception as e:
        return Response({'error': str(e)}, status=500)

@permission_classes([IsAdmin])
@api_view(['DELETE'])
def delete_profile(request):
    try:
        profile_id = request.data.get('profile_id')
        if not profile_id:
            return Response({'error': 'profile_id is required'}, status=400)

        if not Profiles.objects.filter(profile_id=profile_id).exists():
            return Response({'error': 'Profile does not exist'}, status=404)

        Profiles.objects.filter(profile_id=profile_id).delete()
        return Response({'message': 'Profile deleted successfully'}, status=200)
    except Exception as e:
        return Response({'error': str(e)}, status=500)

@permission_classes([IsAdmin])
@api_view(['POST'])
def create_carrier(request):
    try:
        # Extract name, email, and password from request data
        name = request.data.get('name')
        email = request.data.get('email')
        password = request.data.get('password')

        if not name or not email or not password:
            return Response({'error': 'name, email, and password are required'}, status=400)

        # Generate salt and hash the password
        salt = os.urandom(16).hex()
        password_hash = hashlib.sha256((password + salt).encode()).hexdigest()

        # Create the carrier
        carrier = Carriers.objects.create(
            name=name,
            email=email,
            password_hash=password_hash,
            salt=salt
        )

        return Response({'message': 'Carrier created successfully', 'carrier_id': carrier.carrier_id}, status=201)
    except Exception as e:
        return Response({'error': str(e)}, status=500)

@permission_classes([IsAdmin])
@api_view(['GET'])
def search_profile(request):
    try:
        last_name = request.GET.get('last_name')
        first_name = request.GET.get('first_name')
        account_id = request.GET.get('account_id')

        if not any([last_name, first_name, account_id]):
            return Response({'error': 'At least one parameter (last_name, first_name, account_id) is required.'}, status=400)

        profiles = Profiles.objects.all()

        if last_name:
            profiles = profiles.filter(last_name__icontains=last_name)
        if first_name:
            profiles = profiles.filter(first_name__icontains=first_name)
        if account_id:
            profiles = profiles.filter(user_id=account_id)

        profiles_data = [
            {
                'profile_id': profile.profile_id,
                'full_name': f"{profile.first_name} {profile.last_name}",
                'phone': profile.phone,
                'account_id': profile.user_id
            }
            for profile in profiles
        ]

        return Response({'profiles': profiles_data}, status=200)
    except Exception as e:
        return Response({'error': str(e)}, status=500)

@permission_classes([IsAdmin])
@api_view(['GET'])
def list_of_tickets(request):
    try:
        tickets = Tickets.objects.all()
        tickets_data = [
            {
                'ticket_id': ticket.ticket_id,
                'profile_id': ticket.profile_id,
                'trip_id': ticket.trip_id,
                'seat_number': ticket.seat.seat_number,
                'price': ticket.price,
                'status': ticket.status
            }
            for ticket in tickets
        ]
        return Response({'tickets': tickets_data}, status=200)
    except Exception as e:
        return Response({'error': str(e)}, status=500)

@permission_classes([IsAdmin])
@api_view(['GET'])
def search_tickets(request):
    try:
        profile_id = request.GET.get('profile_id')
        trip_id = request.GET.get('trip_id')

        if not any([profile_id, trip_id]):
            return Response({'error': 'At least one parameter (profile_id, trip_id) is required.'}, status=400)

        tickets = Tickets.objects.all()

        if profile_id:
            tickets = tickets.filter(profile_id=profile_id)
        if trip_id:
            tickets = tickets.filter(trip_id=trip_id)

        tickets_data = [
            {
                'ticket_id': ticket.ticket_id,
                'profile_id': ticket.profile_id,
                'trip_id': ticket.trip_id,
                'seat_number': ticket.seat.seat_number,
                'price': ticket.price,
                'status': ticket.status
            }
            for ticket in tickets
        ]

        return Response({'tickets': tickets_data}, status=200)
    except Exception as e:
        return Response({'error': str(e)}, status=500)

@permission_classes([IsAdmin])
@api_view(['GET'])
def search_users(request):
    try:
        last_name = request.GET.get('last_name')
        first_name = request.GET.get('first_name')
        user_id = request.GET.get('user_id')

        if not any([last_name, first_name, user_id]):
            return Response({'error': 'At least one parameter (last_name, first_name, user_id) is required.'}, status=400)

        users = Users.objects.all()

        if last_name:
            users = users.filter(last_name__icontains=last_name)
        if first_name:
            users = users.filter(first_name__icontains=first_name)
        if user_id:
            users = users.filter(user_id=user_id)

        users_data = [
            {
                'user_id': user.user_id,
                'full_name': f"{user.first_name} {user.last_name}",
                'email': user.email,
                'created_at': user.created_at
            }
            for user in users
        ]

        return Response({'users': users_data}, status=200)
    except Exception as e:
        return Response({'error': str(e)}, status=500)

@permission_classes([IsAdmin])
@api_view(['GET'])
def search_trips(request):
    try:
        date = request.GET.get('date')
        carrier_id = request.GET.get('carrier_id')
        route_id = request.GET.get('route_id')

        if not any([date, carrier_id, route_id]):
            return Response({'error': 'At least one parameter (date, carrier_id, route_id) is required.'}, status=400)

        trips = Trips.objects.all()

        if date:
            trips = trips.filter(departure_time__date=date)
        if carrier_id:
            trips = trips.filter(vehicle__carrier_id=carrier_id)
        if route_id:
            trips = trips.filter(route_id=route_id)

        trips_data = [
            {
                'trip_id': trip.trip_id,
                'departure_time': trip.departure_time,
                'arrival_time': trip.arrival_time,
                'base_price': trip.base_price,
                'status': trip.status,
                'distance_km': trip.distance_km,
                'route': {
                    'departure_city': trip.route.departure_city.name,
                    'arrival_city': trip.route.arrival_city.name
                },
                'vehicle': {
                    'type': trip.vehicle.type,
                    'model': trip.vehicle.model,
                    'vehicle_number': trip.vehicle.vehicle_number
                }
            }
            for trip in trips
        ]

        return Response({'trips': trips_data}, status=200)
    except Exception as e:
        return Response({'error': str(e)}, status=500)

@permission_classes([IsAdmin])
@api_view(['GET'])
def search_carrier(request):
    try:
        name = request.GET.get('name')
        carrier_id = request.GET.get('carrier_id')

        if not any([name, carrier_id]):
            return Response({'error': 'At least one parameter (name, carrier_id) is required.'}, status=400)

        carriers = Carriers.objects.all()

        if name:
            carriers = carriers.filter(name__icontains=name)
        if carrier_id:
            carriers = carriers.filter(carrier_id=carrier_id)

        carriers_data = [
            {
                'carrier_id': carrier.carrier_id,
                'name': carrier.name,
                'email': carrier.email,
                'phone': carrier.phone
            }
            for carrier in carriers
        ]

        return Response({'carriers': carriers_data}, status=200)
    except Exception as e:
        return Response({'error': str(e)}, status=500)

