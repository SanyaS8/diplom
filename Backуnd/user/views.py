from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from transport_company.models import Profile, Users
from .permissions import IsUser
from rest_framework_simplejwt.authentication import JWTAuthentication
from django.db import connection

@permission_classes([IsUser])
@api_view(['POST'])
def add_profile(request):
    try:
        # Authenticate and extract user info from token
        jwt_authenticator = JWTAuthentication()
        validated_token = jwt_authenticator.get_validated_token(request.headers.get('Authorization').split()[1])
        user_id = validated_token.get('id')

        first_name = request.data.get('first_name')
        last_name = request.data.get('last_name')
        phone = request.data.get('phone')
        birth_date = request.data.get('birth_date')
        passport_series = request.data.get('passport_series')
        passport_number = request.data.get('passport_number')

        if not Users.objects.filter(user_id=user_id).exists():
            return Response({'error': 'User does not exist'}, status=400)

        profile = Profile.objects.create(
            user_id=user_id,
            first_name=first_name,
            last_name=last_name,
            phone=phone,
            birth_date=birth_date,
            passport_series=passport_series,
            passport_number=passport_number
        )

        return Response({'message': 'Profile created successfully'}, status=201)
    except Exception as e:
        return Response({'error': str(e)}, status=500)

@permission_classes([IsUser])
@api_view(['DELETE'])
def delete_profile(request):
    try:
        # Authenticate and extract user info from token
        jwt_authenticator = JWTAuthentication()
        validated_token = jwt_authenticator.get_validated_token(request.headers.get('Authorization').split()[1])
        user_id = validated_token.get('id')

        # Extract profile_id from request data
        profile_id = request.data.get('profile_id')

        # Check if profile exists and belongs to the user
        if not Profile.objects.filter(profile_id=profile_id, user_id=user_id).exists():
            return Response({'error': 'Profile does not exist or does not belong to the user'}, status=404)

        # Delete the profile
        Profile.objects.filter(profile_id=profile_id, user_id=user_id).delete()
        return Response({'message': 'Profile deleted successfully'}, status=200)
    except Exception as e:
        return Response({'error': str(e)}, status=500)

@permission_classes([IsUser])
@api_view(['GET'])
def my_profile(request):
    try:
        # Authenticate and extract user info from token
        jwt_authenticator = JWTAuthentication()
        validated_token = jwt_authenticator.get_validated_token(request.headers.get('Authorization').split()[1])
        user_id = validated_token.get('id')

        # Retrieve all profiles for the user
        profiles = Profile.objects.filter(user_id=user_id)
        if not profiles.exists():
            return Response({'error': 'No profiles found for the user'}, status=404)

        # Serialize profile data
        profiles_data = [
            {
                'profile_id': profile.profile_id,
                'first_name': profile.first_name,
                'last_name': profile.last_name,
                'phone': profile.phone,
                'birth_date': profile.birth_date,
                'passport_series': profile.passport_series,
                'passport_number': profile.passport_number
            }
            for profile in profiles
        ]

        return Response({'profiles': profiles_data}, status=200)
    except Exception as e:
        return Response({'error': str(e)}, status=500)

@permission_classes([IsUser])
@api_view(['GET'])
def my_tickets(request):
    try:
        # Extract user_id from request data first
        user_id = request.data.get('user_id')

        # If user_id is not in request data, extract it from token
        if not user_id:
            jwt_authenticator = JWTAuthentication()
            token = request.headers.get('Authorization')
            if token:
                validated_token = jwt_authenticator.get_validated_token(token.split()[1])
                user_id = validated_token.get('id')

        if not user_id:
            return Response({'error': 'User ID is required'}, status=400)

        # Query the database using the user_tickets function
        with connection.cursor() as cursor:
            cursor.execute("SELECT * FROM transport_company.user_tickets(%s)", [user_id])
            tickets = cursor.fetchall()

        # Map the results to a list of dictionaries
        tickets_data = [
            {
                'ticket_id': ticket[0],
                'departure_time': ticket[1],
                'arrival_time': ticket[2],
                'price': ticket[3],
                'status': ticket[4],
                'type': ticket[5],
                'model': ticket[6],
                'vehicle_number': ticket[7],
                'distance_km': ticket[8],
                'carrier_name': ticket[9],
                'seat_number': ticket[10],
                'departure_city': ticket[11],
                'arrival_city': ticket[12],
                'first_name': ticket[13],
                'last_name': ticket[14],
                'payment_status': ticket[15]
            }
            for ticket in tickets
        ]

        return Response({'tickets': tickets_data}, status=200)
    except Exception as e:
        return Response({'error': str(e)}, status=500)

@permission_classes([IsUser])
@api_view(['POST'])
def add_ticket(request):
    try:
        # Authenticate and extract user info from token
        jwt_authenticator = JWTAuthentication()
        token = request.headers.get('Authorization')
        if not token:
            return Response({'error': 'Authorization token is required'}, status=401)

        validated_token = jwt_authenticator.get_validated_token(token.split()[1])
        user_id = validated_token.get('id')

        # Extract trip_id and profile_id from request data
        trip_id = request.data.get('trip_id')
        profile_id = request.data.get('profile_id')

        if not trip_id or not profile_id:
            return Response({'error': 'trip_id and profile_id are required'}, status=400)

        # Call the database function to add a ticket
        with connection.cursor() as cursor:
            cursor.execute(
                "SELECT * FROM transport_company.add_ticket(%s, %s, %s)",
                [user_id, trip_id, profile_id]
            )
            result = cursor.fetchone()

        return Response({'message': 'Ticket added successfully', 'ticket': result}, status=201)
    except Exception as e:
        return Response({'error': str(e)}, status=500)

@permission_classes([IsUser])
@api_view(['POST'])
def cancel_ticket(request):
    try:
        # Authenticate and extract user info from token
        jwt_authenticator = JWTAuthentication()
        token = request.headers.get('Authorization')
        if not token:
            return Response({'error': 'Authorization token is required'}, status=401)

        validated_token = jwt_authenticator.get_validated_token(token.split()[1])
        user_id = validated_token.get('id')

        # Extract ticket_id from request data
        ticket_id = request.data.get('ticket_id')

        if not ticket_id:
            return Response({'error': 'ticket_id is required'}, status=400)

        # Check if the ticket exists and belongs to the user
        with connection.cursor() as cursor:
            cursor.execute(
                "SELECT status FROM tickets WHERE ticket_id = %s AND user_id = %s",
                [ticket_id, user_id]
            )
            ticket = cursor.fetchone()

        if not ticket:
            return Response({'error': 'Ticket does not exist or does not belong to the user'}, status=404)

        # Update the ticket status to 'cancelled_by_user'
        with connection.cursor() as cursor:
            cursor.execute(
                "UPDATE tickets SET status = %s WHERE ticket_id = %s",
                ['cancelled_by_user', ticket_id]
            )

        return Response({'message': 'Ticket cancelled successfully'}, status=200)
    except Exception as e:
        return Response({'error': str(e)}, status=500)
