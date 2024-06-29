from django.contrib import admin

from hotel.models import Hotel, Citi, Room, Booking


@admin.register(Citi)
class CitiAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')


@admin.register(Room)
class RoomAdmin(admin.ModelAdmin):
    list_display = ('id', 'number', 'room_price', 'room_type', 'hotel')


@admin.register(Hotel)
class HotelAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'stars', 'address', 'rooms', 'swimming_pool')


@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = ('id', 'client', 'date_add', 'check_in_date', 'eviction_date')

