from .models import Hotel, Room
from rest_framework import serializers

class HotelSerializer(serializers.ModelSerializer):
    room_count = serializers.IntegerField(source='rooms.count', read_only=True)
    available_room_count = serializers.SerializerMethodField()

    class Meta:
        model = Hotel
        fields = "__all__"

    def get_available_room_count(self, obj):
        return Room.objects.filter(hotel=obj, available=True).count()

class RoomSerializer(serializers.ModelSerializer):
    hotel_name = serializers.CharField(source = 'hotel.name', read_only=True)
    class Meta:
        model = Room
        fields = "__all__"

