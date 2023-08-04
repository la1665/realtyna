from rest_framework import serializers

from .models import *


class RoomReservationSerializer(serializers.ModelSerializer):
    room = serializers.PrimaryKeyRelatedField(queryset=Room.objects.all())
    class Meta:
        model = RoomReservation
        fields = ('reservation_name', 'room', 'start_date', 'duration')

    def validate(self, data):
        duration = int(data.get('start_date').day) + int(data.get('duration'))
        if duration > int(data.get('start_date').day):
            return data
        error = 'End date should be greater than start date'
        raise serializers.ValidationError(error)
        
    def validate_duration(self ,value):
        if int(value) < 0 :
            raise serializers.ValidationError('Minimum duration must be postive')

        return value    

    
class ValidRoomSerializer(serializers.Serializer):
    date = serializers.CharField()
        
    def validate(self, data):
        # data = {'rooms': []}
        # date = str(f"{y}-{m}-{d}")
        date = data.split('-')
        rooms = RoomProfile.objects.all()
        available_rooms = []
        for room in rooms:
            year = list(room.value.keys())
            if not year:
                available_rooms.append(room.room.room_name)
            elif not date[0] in year:
                available_rooms.append(room.room.room_name)
            elif not date[1] in list(room.value[date[0]].keys()):
                available_rooms.append(room.room.room_name)
            elif not int(date[2]) in room.value[date[0]][date[1]]:
                available_rooms.append(room.room.room_name)
            else:
                available_rooms.append(0)
        return available_rooms