from rest_framework import viewsets
from .models import Hotel, Room
from .serializers import HotelSerializer, RoomSerializer
from hotel_booking_system.pagination import CustomPageNumberPagination
from django.db.models import Q, Count

class HotelViewSet(viewsets.ModelViewSet):
    queryset = Hotel.objects.all()
    serializer_class = HotelSerializer
    pagination_class = CustomPageNumberPagination

    def get_queryset(self):
        queryset = super().get_queryset()
        name = self.request.query_params.get('name', None)
        address = self.request.query_params.get('address', None)
        city = self.request.query_params.get('city', None)
        available = self.request.query_params.get('available', None)

        if name:
            queryset = queryset.filter(name__icontains = name)
        if address:
            queryset = queryset.filter(address__icontains = address)
        if city:
            queryset = queryset.filter(city__icontains = city)
        if available is not None:
            queryset = queryset.annotate(
                available_rooms_count=Count('rooms', filter=Q(rooms__available=True))
            ).filter(available_rooms_count__gt=0)
        
        return queryset

class RoomViewSet(viewsets.ModelViewSet):
    queryset = Room.objects.all()
    serializer_class = RoomSerializer
    pagination_class = CustomPageNumberPagination

    def get_queryset(self):
        queryset = super().get_queryset()
        type = self.request.query_params.get('type', None)
        price = self.request.query_params.get('price', None)
        available = self.request.query_params.get('available', None)
        ordering = self.request.query_params.get('ordering', None)

        if type:
            queryset = queryset.filter(type = type)
        if price:
            price = float(price)
            queryset = queryset.filter(price__lte = price)
        if available:
            queryset = queryset.filter(available = available.lower() in ['true', '1', 't', 'y', 'yes'])
        if ordering:
            if ordering in ["price", "-price", "type"]:
                queryset = queryset.order_by(ordering)
        
        return queryset