from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import hashlib
from rest_framework_simplejwt.tokens import RefreshToken
from transport_company.models import Administrators, Carriers, Cities, Users
import json
from django.db import connection
from .permissions import IsGuest
from rest_framework.decorators import permission_classes

def list_of_cities(request):
    cities = Cities.objects.values('name', 'country')
    return JsonResponse(list(cities), safe=False)

def search_trips_by_cities(request):
    city1_name = request.GET.get('city1_name')
    country1_name = request.GET.get('country1_name')
    city2_name = request.GET.get('city2_name')
    country2_name = request.GET.get('country2_name')

    if not all([city1_name, country1_name, city2_name, country2_name]):
        return JsonResponse({'error': 'All parameters (city1_name, country1_name, city2_name, country2_name) are required.'}, status=400)

    with connection.cursor() as cursor:
        cursor.execute("""
            SELECT * FROM transport_company.search_trips_by_cities(%s, %s, %s, %s);
        """, [city1_name, country1_name, city2_name, country2_name])
        columns = [col[0] for col in cursor.description]
        results = [dict(zip(columns, row)) for row in cursor.fetchall()]

    return JsonResponse(results, safe=False)

def exit(request):
    # Генерация нового гостевого токена
    guest_token = RefreshToken()
    guest_token['role'] = 'guest'
    response = JsonResponse({'message': 'Guest token generated'})
    response['Authorization'] = f"Bearer {guest_token.access_token}"
    return response

def generate_jwt_token(user_role, id):
    refresh = RefreshToken.for_user(user_role)
    refresh['role'] = user_role
    refresh['id'] = id
    return {
        'refresh': str(refresh),
        'access': str(refresh.access_token),
        'role': user_role,
        'id': id
    }

@csrf_exempt
@permission_classes([IsGuest])
def login(request):
    if request.method != 'POST':
        return JsonResponse({'error': 'Only POST method is allowed'}, status=405)

    try:
        data = json.loads(request.body)
        username = data.get('username')
        password = data.get('password')

        if not username or not password:
            return JsonResponse({'error': 'Username and password are required'}, status=400)

        # Check in Users table
        user = Users.objects.filter(email=username).first()
        if user:
            salt = user.salt
            hashed_password = hashlib.sha256((password + salt).encode()).hexdigest()
            if hashed_password == user.password_hash:
                token = generate_jwt_token('user', user.user_id)
                response = JsonResponse({'message': 'Login successful'})
                response['Authorization'] = f"Bearer {token['access']}"
                return response

        # Check in Administrators table
        admin = Administrators.objects.filter(email=username).first()
        if admin:
            salt = admin.salt
            hashed_password = hashlib.sha256((password + salt).encode()).hexdigest()
            if hashed_password == admin.password_hash:
                token = generate_jwt_token('administrator', admin.admin_id)
                response = JsonResponse({'message': 'Login successful'})
                response['Authorization'] = f"Bearer {token['access']}"
                return response

        # Check in Carriers table
        carrier = Carriers.objects.filter(email=username).first()
        if carrier:
            salt = carrier.salt
            hashed_password = hashlib.sha256((password + salt).encode()).hexdigest()
            if hashed_password == carrier.password_hash:
                token = generate_jwt_token('carrier', carrier.carrier_id)
                response = JsonResponse({'message': 'Login successful'})
                response['Authorization'] = f"Bearer {token['access']}"
                return response

        return JsonResponse({'error': 'Invalid username or password'}, status=401)

    except json.JSONDecodeError:
        return JsonResponse({'error': 'Invalid JSON'}, status=400)


@csrf_exempt
@permission_classes([IsGuest])
def register_user(request):
    if request.method != 'POST':
        return JsonResponse({'error': 'Only POST method is allowed'}, status=405)

    try:
        data = json.loads(request.body)
        email = data.get('email')
        password = data.get('password')

        if not email or not password:
            return JsonResponse({'error': 'Email and password are required'}, status=400)

        # Check if email already exists
        if Users.objects.filter(email=email).exists():
            return JsonResponse({'error': 'Email already in use'}, status=400)

        # Generate salt and hash the password
        salt = hashlib.sha256(str(email).encode()).hexdigest()
        password_hash = hashlib.sha256((password + salt).encode()).hexdigest()

        # Create new user
        user = Users.objects.create(email=email, salt=salt, password_hash=password_hash)
        user.save()

        # Generate JWT token
        token = generate_jwt_token('user', user.user_id)

        response = JsonResponse({'message': 'User registered successfully'}, status=201)
        response['Authorization'] = f"Bearer {token['access']}"
        return response

    except json.JSONDecodeError:
        return JsonResponse({'error': 'Invalid JSON'}, status=400)

# Добавление новых API для поиска рейсов
@csrf_exempt
@permission_classes([IsGuest])
def search_trips_all(request):
    return search_trips_by_type(request, None)

@csrf_exempt
@permission_classes([IsGuest])
def search_trips_airplane(request):
    return search_trips_by_type(request, 'airplane')

@csrf_exempt
@permission_classes([IsGuest])
def search_trips_train(request):
    return search_trips_by_type(request, 'train')

@csrf_exempt
@permission_classes([IsGuest])
def search_trips_bus(request):
    return search_trips_by_type(request, 'bus')

# Общая функция для фильтрации по типу транспорта
def search_trips_by_type(request, vehicle_type):
    city1_name = request.GET.get('city1_name')
    country1_name = request.GET.get('country1_name')
    city2_name = request.GET.get('city2_name')
    country2_name = request.GET.get('country2_name')
    departure_date = request.GET.get('departure_date')

    if not all([city1_name, country1_name, city2_name, country2_name, departure_date]):
        return JsonResponse({'error': 'All parameters (city1_name, country1_name, city2_name, country2_name, departure_date) are required.'}, status=400)

    with connection.cursor() as cursor:
        query = """
            SELECT * FROM transport_company.search_trips_by_cities(%s, %s, %s, %s)
            WHERE DATE(departure_time) = %s
        """
        params = [city1_name, country1_name, city2_name, country2_name, departure_date]

        if vehicle_type:
            query += " AND type = %s"
            params.append(vehicle_type)

        cursor.execute(query, params)
        columns = [col[0] for col in cursor.description]
        results = [dict(zip(columns, row)) for row in cursor.fetchall()]

    return JsonResponse(results, safe=False)