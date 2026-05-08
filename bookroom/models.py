from django.db import models
from django.core.exceptions import ValidationError
from datetime import date


class Room(models.Model):
    room_number = models.IntegerField(unique=True)

    def __str__(self):
        return self.name
    

class Booking(models.Model):
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    start_date = models.DateField()
    end_date = models.DateField()

    def clean(self):
        if self.start_date > self.end_date:
            raise ValidationError("Start date must be before end date.")

        today = date.today()
        if self.start_date < today:
            raise ValidationError("Cannot book rooms for past dates. Booking date is outdated.")

        if self.end_date < today:
            raise ValidationError("Cannot book rooms for past dates. Booking date is outdated.")

        overlapping_booking = Booking.objects.filter(
            room = self.room,
            start_date__lte = self.end_date,
            end_date__gte = self.start_date,
        ).exclude(pk = self.pk)

        if overlapping_booking.exists():
            booking_ranges = []
            for b in overlapping_booking:
                booking_ranges.append(f"{b.start_date.strftime('%d %b %Y')} to {b.end_date.strftime('%d %b %Y')}")
                timeperiod = ", ".join(booking_ranges)

            raise ValidationError(f"Room is already booked during this period: {timeperiod}")

    def save(self, *args, **kwargs):
        self.clean()
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.name} ({self.start_date} to {self.end_date})"
    