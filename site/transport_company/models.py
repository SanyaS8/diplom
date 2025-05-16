from django.db import models


class Administrators(models.Model):
    admin_id = models.AutoField(primary_key=True)
    email = models.CharField(unique=True, max_length=100)
    password_hash = models.CharField(max_length=255)
    created_at = models.DateTimeField(blank=True, null=True)
    salt = models.CharField(max_length=64, blank=True, null=True)

    class Meta:
        db_table = 'administrators'


class Carriers(models.Model):
    carrier_id = models.AutoField(primary_key=True)
    name = models.CharField(unique=True, max_length=100)
    email = models.CharField(unique=True, max_length=100)
    phone = models.CharField(max_length=20, blank=True, null=True)
    password_hash = models.CharField(max_length=255)
    created_at = models.DateTimeField(blank=True, null=True)
    salt = models.CharField(max_length=64, blank=True, null=True)
    tin = models.CharField(max_length=20, unique=True, blank=True, null=True)

    class Meta:
        db_table = 'carriers'



class Cities(models.Model):
    city_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    country = models.CharField(max_length=100)

    class Meta:
        db_table = 'cities'
        unique_together = (('name', 'country'),)


class Payments(models.Model):
    payment_id = models.AutoField(primary_key=True)
    ticket = models.ForeignKey('Tickets', models.DO_NOTHING)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    payment_method = models.CharField(max_length=20)
    payment_status = models.CharField(max_length=20, blank=True, null=True)
    payment_time = models.DateTimeField(blank=True, null=True)

    class Meta:
        db_table = 'payments'


class Profile(models.Model):
    profile_id = models.AutoField(primary_key=True)
    user = models.ForeignKey('Users', models.DO_NOTHING)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    phone = models.CharField(max_length=20)
    birth_date = models.DateField()
    passport_series = models.CharField(max_length=10)
    passport_number = models.CharField(max_length=20)

    class Meta:
        db_table = 'profile'
        unique_together = (('passport_series', 'passport_number'),)


class Routes(models.Model):
    route_id = models.AutoField(primary_key=True)
    departure_city = models.ForeignKey(Cities, models.DO_NOTHING)
    arrival_city = models.ForeignKey(Cities, models.DO_NOTHING, related_name='routes_arrival_city_set')

    class Meta:
        db_table = 'routes'


class Seats(models.Model):
    seat_id = models.AutoField(primary_key=True)
    vehicle = models.ForeignKey('Vehicles', models.DO_NOTHING)
    trip = models.ForeignKey('Trips', models.DO_NOTHING)
    seat_number = models.CharField(max_length=10)
    is_available = models.BooleanField(blank=True, null=True)

    class Meta:
        db_table = 'seats'
        unique_together = (('trip', 'seat_number'),)


class Tickets(models.Model):
    ticket_id = models.AutoField(primary_key=True)
    user = models.ForeignKey('Users', models.DO_NOTHING)
    trip = models.ForeignKey('Trips', models.DO_NOTHING)
    seat = models.OneToOneField(Seats, models.DO_NOTHING)
    profile = models.ForeignKey('Profile', models.DO_NOTHING)
    purchase_time = models.DateTimeField(blank=True, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        db_table = 'tickets'


class Trips(models.Model):
    trip_id = models.AutoField(primary_key=True)
    route = models.ForeignKey(Routes, models.DO_NOTHING)
    vehicle = models.ForeignKey('Vehicles', models.DO_NOTHING)
    departure_time = models.DateTimeField()
    arrival_time = models.DateTimeField()
    base_price = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(max_length=20, blank=True, null=True)
    distance_km = models.DecimalField(max_digits=10, decimal_places=2)
    trip_number = models.CharField(max_length=20, unique=True)

    class Meta:
        db_table = 'trips'


class Users(models.Model):
    user_id = models.AutoField(primary_key=True)
    email = models.CharField(unique=True, max_length=100)
    password_hash = models.CharField(max_length=255)
    created_at = models.DateTimeField(blank=True, null=True)
    salt = models.CharField(max_length=64, blank=True, null=True)

    class Meta:
        db_table = 'users'


class Vehicles(models.Model):
    vehicle_id = models.AutoField(primary_key=True)
    carrier = models.ForeignKey(Carriers, models.DO_NOTHING)
    type = models.CharField(max_length=20)
    model = models.CharField(max_length=100, blank=True, null=True)
    total_seats = models.IntegerField()
    vehicle_number = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        db_table = 'vehicles'
