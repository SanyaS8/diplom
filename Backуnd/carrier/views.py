from django.shortcuts import render
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from transport_company.models import Carriers, Trips
from .permissions import IsCarrier
from django.db import connection
from rest_framework_simplejwt.authentication import JWTAuthentication


@permission_classes([IsCarrier])
@api_view(['PATCH'])
def update_carrier_info(request):
    # Authenticate and extract carrier info from token
    jwt_authenticator = JWTAuthentication()
    token = request.headers.get('Authorization')
    if not token:
        return Response({'error': 'Authorization token is required'}, status=401)

    validated_token = jwt_authenticator.get_validated_token(token.split()[1])
    carrier_id = validated_token.get('id')

    try:
        carrier = Carriers.objects.get(pk=carrier_id)
    except Carriers.DoesNotExist:
        return Response({'error': 'Carrier not found'}, status=404)

    # Получаем данные из запроса
    name = request.data.get('name')
    phone = request.data.get('phone')
    tin = request.data.get('TIN')

    # Обновляем данные, если они переданы
    if name:
        carrier.name = name
    if phone:
        carrier.phone = phone
    if tin:
        carrier.tin = tin

    # Сохраняем изменения
    carrier.save()

    return Response({"message": "Информация обновлена успешно"})


@permission_classes([IsCarrier])
@api_view(['POST'])
def add_trip(request):
    # Authenticate and extract carrier info from token
    jwt_authenticator = JWTAuthentication()
    token = request.headers.get('Authorization')
    if not token:
        return Response({'error': 'Authorization token is required'}, status=401)

    validated_token = jwt_authenticator.get_validated_token(token.split()[1])
    carrier_id = validated_token.get('id')

    # Получаем данные из запроса
    departure_city_id = request.data.get('departure_city_id')
    arrival_city_id = request.data.get('arrival_city_id')
    vehicle_type = request.data.get('vehicle_type')
    vehicle_model = request.data.get('vehicle_model')
    total_seats = request.data.get('total_seats')
    vehicle_number = request.data.get('vehicle_number')
    departure_time = request.data.get('departure_time')
    arrival_time = request.data.get('arrival_time')
    base_price = request.data.get('base_price')
    distance_km = request.data.get('distance_km')
    trip_number = request.data.get('trip_number')

    # Проверка обязательных параметров
    required_fields = [
        'departure_city_id', 'arrival_city_id', 'vehicle_type', 'vehicle_model',
        'total_seats', 'vehicle_number', 'departure_time', 'arrival_time',
        'base_price', 'distance_km', 'trip_number'
    ]
    for field in required_fields:
        if not request.data.get(field):
            return Response({"error": f"Field {field} is required."}, status=400)

    try:
        with connection.cursor() as cursor:
            cursor.execute(
                """
                SELECT transport_company.add_trip(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
                """,
                [
                    carrier_id, departure_city_id, arrival_city_id, vehicle_type,
                    vehicle_model, total_seats, vehicle_number, departure_time,
                    arrival_time, base_price, distance_km, trip_number
                ]
            )
            new_trip_id = cursor.fetchone()[0]

        return Response({"message": "Trip created successfully", "trip_id": new_trip_id})
    except Exception as e:
        return Response({"error": str(e)}, status=400)


@permission_classes([IsCarrier])
@api_view(['PATCH'])
def update_trip(request):
    # Authenticate and extract carrier info from token
    jwt_authenticator = JWTAuthentication()
    token = request.headers.get('Authorization')
    if not token:
        return Response({'error': 'Authorization token is required'}, status=401)

    validated_token = jwt_authenticator.get_validated_token(token.split()[1])
    carrier_id = validated_token.get('id')

    # Получаем данные из запроса
    trip_id = request.data.get('trip_id')
    departure_time = request.data.get('departure_time')
    arrival_time = request.data.get('arrival_time')
    trip_number = request.data.get('trip_number')

    if not trip_id:
        return Response({'error': 'Field trip_id is required.'}, status=400)

    try:
        trip = Trips.objects.get(pk=trip_id, vehicle__carrier_id=carrier_id)
    except Trips.DoesNotExist:
        return Response({'error': 'Trip not found or you do not have permission to modify it.'}, status=404)

    # Обновляем данные, если они переданы
    if departure_time:
        trip.departure_time = departure_time
    if arrival_time:
        trip.arrival_time = arrival_time
    if trip_number:
        trip.trip_number = trip_number

    # Сохраняем изменения
    trip.save()

    return Response({"message": "Trip updated successfully"})


@permission_classes([IsCarrier])
@api_view(['PATCH'])
def cancel_trip(request):
    # Authenticate and extract carrier info from token
    jwt_authenticator = JWTAuthentication()
    token = request.headers.get('Authorization')
    if not token:
        return Response({'error': 'Authorization token is required'}, status=401)

    validated_token = jwt_authenticator.get_validated_token(token.split()[1])
    carrier_id = validated_token.get('id')

    # Получаем ID рейса из запроса
    trip_id = request.data.get('trip_id')

    if not trip_id:
        return Response({'error': 'Field trip_id is required.'}, status=400)

    try:
        trip = Trips.objects.get(pk=trip_id, vehicle__carrier_id=carrier_id)
    except Trips.DoesNotExist:
        return Response({'error': 'Trip not found or you do not have permission to modify it.'}, status=404)

    # Обновляем статус рейса на "cancelled"
    trip.status = 'cancelled'
    trip.save()

    return Response({"message": "Trip cancelled successfully"})


@permission_classes([IsCarrier])
@api_view(['DELETE'])
def delete_trip(request):
    # Authenticate and extract carrier info from token
    jwt_authenticator = JWTAuthentication()
    token = request.headers.get('Authorization')
    if not token:
        return Response({'error': 'Authorization token is required'}, status=401)

    validated_token = jwt_authenticator.get_validated_token(token.split()[1])
    carrier_id = validated_token.get('id')

    # Получаем ID рейса из запроса
    trip_id = request.data.get('trip_id')

    if not trip_id:
        return Response({'error': 'Field trip_id is required.'}, status=400)

    try:
        # Проверяем, что рейс принадлежит перевозчику
        with connection.cursor() as cursor:
            cursor.execute(
                """
                SELECT 1 FROM transport_company.trips t
                JOIN transport_company.vehicles v ON t.vehicle_id = v.vehicle_id
                WHERE t.trip_id = %s AND v.carrier_id = %s
                """,
                [trip_id, carrier_id]
            )
            if cursor.fetchone() is None:
                return Response({'error': 'Trip not found or does not belong to the carrier.'}, status=404)

        # Вызываем функцию удаления рейса
        with connection.cursor() as cursor:
            cursor.execute(
                """
                SELECT transport_company.delete_trip(%s)
                """,
                [trip_id]
            )
            result_message = cursor.fetchone()[0]

        return Response({"message": result_message})
    except Exception as e:
        return Response({'error': str(e)}, status=400)
