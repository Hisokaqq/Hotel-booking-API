from rest_framework import viewsets, filters
from .models import Hotel, Room
from .serializers import HotelSerializer, RoomSerializer
from hotel_booking_system.pagination import CustomPageNumberPagination

class HotelViewSet(viewsets.ModelViewSet):
    queryset = Hotel.objects.all()
    serializer_class = HotelSerializer
    pagination_class = CustomPageNumberPagination
    filter_backends = [filters.SearchFilter]
    search_fields = ['name', 'address']

class RoomViewSet(viewsets.ModelViewSet):
    queryset = Room.objects.all()
    serializer_class = RoomSerializer
    pagination_class = CustomPageNumberPagination
    filter_backends = [filters.SearchFilter]
    search_fields = ['number', 'hotel']
