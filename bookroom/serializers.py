from rest_framework import serializers
from .models import *


class RoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Room
        fields = "__all__"


class BookingSerializer(serializers.ModelSerializer):
    room = serializers.SlugRelatedField(
        queryset = Room.objects.all(),
        slug_field = "room_number"         # Booking → ForeignKey → Room (via ID)
    )
    class Meta:
        model = Booking
        fields = "__all__"

    def Validate(self, data):
        room = data.get("room")
        start_date = data.get("start_date")
        end_date = data.get("end_date")

        if start_date > end_date:
            raise serializers.ValidationError("Start date must be before end date.")

        overlapping = Booking.objects.filter(
            room = room,
            start_date__lt = end_date,
            end_date__gt = start_date,
        )

        if overlapping.exists():
            booked_ranges = [
                f"{b.start_date} to {b.end_date}"
                for b in overlapping
            ]
            timeperiod = ", ".join(booked_ranges)
            raise serializers.ValidationError(f"Room is already booked during this period: {timeperiod}")

        return data
        