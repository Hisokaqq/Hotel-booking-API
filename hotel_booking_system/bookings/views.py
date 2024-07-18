from rest_framework import viewsets
from .models import Booking
from .serializers import BookingSerializer, BokingFullSerializer
from hotel_booking_system.pagination import CustomPageNumberPagination
class BookingViewSet(viewsets.ModelViewSet):
    queryset = Booking.objects.all()
    pagination_class = CustomPageNumberPagination

    def get_serializer_class(self):
        if self.action == 'retrieve':
            return BokingFullSerializer
        return BookingSerializer

    def get_queryset(self):
        queryset = super().get_queryset()
        status = self.request.query_params.get('status')

        if status:
            queryset = queryset.filter(status = status)
        
        return  queryset
