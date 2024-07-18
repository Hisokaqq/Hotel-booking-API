from .models import Booking, Payment
from hotels.serializers import RoomSerializer
from hotels.models import Room
from rest_framework import serializers

class PaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payment
        fields = '__all__'

class BookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = '__all__'

class BokingFullSerializer(serializers.ModelSerializer):
    payment = PaymentSerializer()
    room = RoomSerializer()
    user_name = serializers.CharField(source='user.username', read_only=True)
    class Meta:
        model = Booking
        fields = '__all__'

