from django.db import models
from django.utils import timezone


class Owner(models.Model):
    owner_name = models.CharField(max_length=250, blank=True, null=True)
    active = models.BooleanField(default=True)
    create_time = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.owner_name


class Room(models.Model):
    room_name = models.CharField(max_length=250)
    owner = models.ForeignKey(Owner, on_delete=models.CASCADE, related_name='rooms')
    
    def __str__(self):
        return self.room_name
    
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)  # Call the "real" save() method.
        room_profile = RoomProfile.objects.create(room=self, value = dict())
        # room_profile = RoomProfile.objects.update_or_create(room=self, value=dict())
        room_profile.save()


class RoomReservation(models.Model):
    reservation_name = models.CharField(max_length=250, blank=False, null=False)
    room = models.ForeignKey(Room, on_delete=models.CASCADE, related_name='reservations')
    start_date = models.DateField(blank=False, null=False)
    duration = models.PositiveIntegerField(blank=False, null=False)
    
    def __str__(self):
        return f"{self.reservation_name} for {self.room.room_name}"
    
    def save(self, *args, **kwargs):
        # room = self.room
        room_profile = RoomProfile.objects.get(room=self.room)
        days = [day for day in range(self.start_date.day, self.start_date.day+self.duration)]
        year = str(self.start_date.year)
        month = str(self.start_date.month)
        day = str(self.start_date.day)
        if not room_profile.value:
            print('4')
            super().save(*args, **kwargs)
            # dict = {month: [day for day in days],}
            room_profile.value[year] = {}
            room_profile.value[year].update({month: [day for day in days]})
            room_profile.save()
        # RoomProfile.objects.get(room=room)
        elif room_profile.value.get(year):
            yearly = room_profile.value.get(year)
            if not yearly.get(month):
                print('2')
                super().save(*args, **kwargs)
                room_profile.value[year].update({month: [day for day in days]})
                room_profile.save()
            elif all(day not in room_profile.value[year][month] for day in days):
                print('1')
                super().save(*args, **kwargs)
                room_profile.value[year][month].extend(days)
                room_profile.save()
            else:
                return
        else:
            
            print(year)
            print(type(year))
            super().save(*args, **kwargs)
            dict = {month: [day for day in days],}
            room_profile.value.update({year: dict})
            room_profile.save()
                           

class RoomProfile(models.Model):
    room = models.OneToOneField(Room, on_delete=models.CASCADE, related_name='room_profile')
    # key = models.PositiveIntegerField(blank=False, null=False)
    value = models.JSONField(blank=True, null=True)
    
    def __str__(self):
        return f"{self.room}"
    

