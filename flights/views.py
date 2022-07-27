import datetime

from rest_framework import generics

from flights import serializers
from flights.models import Booking, Flight
from .serializers import UserLoginSerializer

class FlightsList(generics.ListAPIView):
    queryset = Flight.objects.all()
    serializer_class = serializers.FlightSerializer


class BookingsList(generics.ListAPIView):
    serializer_class = serializers.BookingSerializer

    def get_queryset(self):
        return Booking.objects.filter(date__gte=datetime.date.today())


class BookingDetails(generics.RetrieveAPIView):
    queryset = Booking.objects.all()
    serializer_class = serializers.BookingDetailsSerializer
    lookup_url_kwarg = "booking_id"


class UpdateBooking(generics.RetrieveUpdateAPIView):
    queryset = Booking.objects.all()
    serializer_class = serializers.UpdateBookingSerializer
    lookup_url_kwarg = "booking_id"


class CancelBooking(generics.DestroyAPIView):
    queryset = Booking.objects.all()
    lookup_url_kwarg = "booking_id"
    
class UserLoginAPIView(serializers.Serializer):
     username = serializers.CharField()
     password = serializers.CharField(write_only=True)
     def validate(self, data):
        my_username = data.get("username")
        my_password = data.get("password")
class BookingcreateAPIView(CreateAPIView):
    queryset= User.objects.all
    serializer_class=BookingcreateSerializer
    lookup_url_kwarg= "flights/"