from django.shortcuts import render
from rest_framework import serializers, viewsets
from .models import Room, Booking
from .serializers import RoomSerializer, BookingSerializer
from django.core.exceptions import ValidationError


class RoomViewSet(viewsets.ModelViewSet):
    queryset = Room.objects.all()
    serializer_class = RoomSerializer


class BookingViewSet(viewsets.ModelViewSet):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer

    def perform_create(self, serializer):
        try:
            serializer.save()
        except ValidationError as e:
            raise serializers.ValidationError(e.message) 


# from rest_framework.decorators import action
# from rest_framework.response import Response

# class RoomViewSet(viewsets.ModelViewSet):
#     queryset = Room.objects.all()
#     serializer_class = RoomSerializer

#     @action(detail=False, methods=['get'])
#     def available(self, request):
#         start_date = request.query_params.get("start_date")
#         end_date = request.query_params.get("end_date")

#         booked_rooms = Booking.objects.filter(
#             start_date__lt=end_date,
#             end_date__gt=start_date
#         ).values_list("room_id", flat=True)

#         rooms = Room.objects.exclude(id__in=booked_rooms)

#         serializer = self.get_serializer(rooms, many=True)
#         return Response(serializer.data)