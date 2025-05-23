# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Administrators(models.Model):
    admin_id = models.AutoField(primary_key=True)
    email = models.CharField(unique=True, max_length=100)
    password_hash = models.CharField(max_length=255)
    created_at = models.DateTimeField(blank=True, null=True)
    salt = models.CharField(max_length=64, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'administrators'
        db_table_comment = '└фьшэшёЄЁрЄюЁ√ ёшёЄхь√'


class Carriers(models.Model):
    carrier_id = models.AutoField(primary_key=True)
    name = models.CharField(unique=True, max_length=100)
    email = models.CharField(unique=True, max_length=100)
    phone = models.CharField(max_length=20, blank=True, null=True)
    password_hash = models.CharField(max_length=255)
    created_at = models.DateTimeField(blank=True, null=True)
    salt = models.CharField(max_length=64, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'carriers'
        db_table_comment = '╚эЇюЁьрЎш  ю ЄЁрэёяюЁЄэ√ї ъюьярэш ї'


class Cities(models.Model):
    city_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    country = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'cities'
        unique_together = (('name', 'country'),)
        db_table_comment = '╤яЁртюўэшъ уюЁюфют фы  ьрЁ°ЁєЄют'


class Payments(models.Model):
    payment_id = models.AutoField(primary_key=True)
    ticket = models.ForeignKey('Tickets', models.DO_NOTHING)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    payment_method = models.CharField(max_length=20)
    payment_status = models.CharField(max_length=20, blank=True, null=True)
    payment_time = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'payments'
        db_table_comment = '╥ЁрэчръЎшш фы  юяырЄ√ сшыхЄют'


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
        managed = False
        db_table = 'profile'
        unique_together = (('passport_series', 'passport_number'),)
        db_table_comment = '╧ЁюЇшыш яюы№чютрЄхыхщ, ёюфхЁцр∙шх яхЁёюэры№э√х фрээ√х'


class Routes(models.Model):
    route_id = models.AutoField(primary_key=True)
    departure_city = models.ForeignKey(Cities, models.DO_NOTHING)
    arrival_city = models.ForeignKey(Cities, models.DO_NOTHING, related_name='routes_arrival_city_set')

    class Meta:
        managed = False
        db_table = 'routes'
        db_table_comment = '╠рЁ°ЁєЄ√ ьхцфє уюЁюфрьш'


class Seats(models.Model):
    seat_id = models.AutoField(primary_key=True)
    vehicle = models.ForeignKey('Vehicles', models.DO_NOTHING)
    trip = models.ForeignKey('Trips', models.DO_NOTHING)
    seat_number = models.CharField(max_length=10)
    is_available = models.BooleanField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'seats'
        unique_together = (('trip', 'seat_number'),)
        db_table_comment = '╠хёЄр т ЄЁрэёяюЁЄх фы  Ёхщёют'


class Tickets(models.Model):
    ticket_id = models.AutoField(primary_key=True)
    user = models.ForeignKey('Users', models.DO_NOTHING)
    trip = models.ForeignKey('Trips', models.DO_NOTHING)
    seat = models.OneToOneField(Seats, models.DO_NOTHING)
    purchase_time = models.DateTimeField(blank=True, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tickets'
        db_table_comment = '╚эЇюЁьрЎш  ю яЁшюсЁхЄхээ√ї сшыхЄрї'


class Trips(models.Model):
    trip_id = models.AutoField(primary_key=True)
    route = models.ForeignKey(Routes, models.DO_NOTHING)
    vehicle = models.ForeignKey('Vehicles', models.DO_NOTHING)
    departure_time = models.DateTimeField()
    arrival_time = models.DateTimeField()
    base_price = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(max_length=20, blank=True, null=True)
    distance_km = models.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        managed = False
        db_table = 'trips'
        db_table_comment = '╩юэъЁхЄэ√х Ёхщё√ яю ьрЁ°ЁєЄрь'


class Users(models.Model):
    user_id = models.AutoField(primary_key=True)
    email = models.CharField(unique=True, max_length=100)
    password_hash = models.CharField(max_length=255)
    created_at = models.DateTimeField(blank=True, null=True)
    salt = models.CharField(max_length=64, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'users'
        db_table_comment = '╟рЁхушёЄЁшЁютрээ√х яюы№чютрЄхыш'


class Vehicles(models.Model):
    vehicle_id = models.AutoField(primary_key=True)
    carrier = models.ForeignKey(Carriers, models.DO_NOTHING)
    type = models.CharField(max_length=20)
    model = models.CharField(max_length=100, blank=True, null=True)
    total_seats = models.IntegerField()
    vehicle_number = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'vehicles'
        db_table_comment = '╥ЁрэёяюЁЄэ√х ёЁхфёЄтр яхЁхтючўшъют'
