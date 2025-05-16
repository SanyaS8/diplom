from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from transport_company.models import Administrators, Carriers, Trips, Users
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

