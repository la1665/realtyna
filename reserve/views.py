from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.generics import get_object_or_404

from .serializers import *
from .models import *


class AddReservationAPIView(APIView):
    def post(self, request):
        reservation_ser = RoomReservationSerializer(data=request.data)
        if reservation_ser.is_valid():
            reservation_ser.save()
            return Response({'message': 'Reservation added successfully!'})

        return Response({'message': reservation_ser.errors})


class ReservationAPIView(APIView):
    def get(self, request, res_id):
        reservation = get_object_or_404(RoomReservation, id=res_id)
        reservation_ser = RoomReservationSerializer(instance=reservation)
        data = reservation_ser.data
        return Response({'reservation': data})

    
class AvailableRoomsAPIView(APIView):
    def get(self, request, y, m, d):
        # free_rooms_ser = ValidRoomSerializer(data = request.data)
        # if free_rooms_ser.is_valid():
        #     data = free_rooms_ser.data
        #     return Response({'available rooms': data})
        # return Response({'message': free_rooms_ser.errors})
        data = {'rooms': []}
        date = str(f"{y}-{m}-{d}")
        date = date.split('-')
        rooms = RoomProfile.objects.all()
        for room in rooms:
            year = list(room.value.keys())
            if not year:
                data['rooms'].append(room.room.room_name)
            elif not date[0] in year:
                data['rooms'].append(room.room.room_name)
            elif not date[1] in list(room.value[date[0]].keys()):
                data['rooms'].append(room.room.room_name)
            elif not int(date[2]) in room.value[date[0]][date[1]]:
                data['rooms'].append(room.room.room_name)
            else:
                return Response({'available rooms': data})
        
        return Response({'available rooms': data})
                
                

            # else :
            #     months = list(room.value[d][1].keys)
            #     for d in range(len(value_list)):
            #         if date[0] == value_list[d][0]:
            #             if date[1] in months:
            #                if int(date[2]) in value_list[d][1][date[1]]:
            #                    return
                           
            #         else:
            #             return room.room_name