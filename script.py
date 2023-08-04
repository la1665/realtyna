from django.db.models import Q
from owner.models import Owner, Room, RoomReservation

s_year = 2023
s_month = 1
s_day = 4
e_year = 2023
e_month = 1
e_day = 8

if not RoomReservation.objects.filter(end_date__year=str(e_year)):
    print('reserve')
elif not RoomReservation.objects.filter(end_date__year=str(e_year)).filter(Q(start_date__month=str(s_month)) | Q(end_date__month=str(e_month))):
    print('reserve')
else:
    checker1 = RoomReservation.objects.filter(Q(end_date__year=str(e_year)) & Q(end_date__month=str(e_month))).order_by('-end_date').values_list('end_date__day', flat=True)[:2]
    checker2 = RoomReservation.objects.filter(Q(start_date__year=str(s_year)) & Q(start_date__month=str(s_month))).order_by('-start_date').values_list('start_date__day', flat=True).first()
    if s_day > checker1[0]:
        print('reserve')
    elif s_day > checker1[1] & e_day < checker2:
        print('reserve')
    else:
        print('you can\'t reserve at this date.')







# & Q(start_date__month=str(s_month))



# a = RoomReservation.objects.filter(Q(end_date__year='2023')&Q(end_date__month='8')).order_by('-end_date').values_list('end_date__day', flat=True)[:2]