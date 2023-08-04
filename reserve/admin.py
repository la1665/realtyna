from django.contrib import admin

from .models import *

@admin.register(Owner)
class OwnerAdmin(admin.ModelAdmin):
    list_display = ['owner_name', 'active', 'create_time']
    list_filter = ['owner_name', 'active', 'create_time']
    search_fields = ['owner_name', 'active']
    date_hierarchy = 'create_time'
    ordering = ['create_time']    


@admin.register(Room)
class RoomAdmin(admin.ModelAdmin):
    list_display = ['room_name', 'owner']


@admin.register(RoomReservation)
class ReservationAdmin(admin.ModelAdmin):
    list_display = ['reservation_name', 'start_date', 'duration', 'room']
    list_filter = ['start_date', 'duration', 'room']
    search_fields = ['room',]


@admin.register(RoomProfile)
class RoomProfileAdmin(admin.ModelAdmin):
    list_display = ['room', 'value']
    

