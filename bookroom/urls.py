from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .models import Room, Booking
from .views import RoomViewSet, BookingViewSet


router = DefaultRouter()
router.register("rooms", RoomViewSet)
router.register("bookings", BookingViewSet)

urlpatterns = [
    path("", include(router.urls)),
]