from django.db import models
from users.models import User
from hotels.models import Room
class Booking(models.Model):
    class Status(models.TextChoices):
        PENDING = 'PENDING', 'Pending'
        CONFIRMED = 'CONFIRMED', 'Confirmed'
        CANCELLED = 'CANCELLED', 'Cancelled'

    user = models.ForeignKey(User, related_name="bookings", on_delete=models.SET_NULL, null=True)
    room = models.ForeignKey(Room, related_name="bookings", on_delete=models.CASCADE)
    
    check_in = models.DateField()
    check_out = models.DateField()
    status = models.CharField(max_length=10, choices=Status.choices, default=Status.PENDING)

    def __str__(self):
        return f"{self.user.username} - {self.room.hotel.name} - {self.room.number} - {self.check_in} to {self.check_out}"

class Payment(models.Model):
    class Method(models.TextChoices):
        CASH = 'CASH', 'Cash'
        CARD = 'CARD', 'Card'
        TRANSFER = 'TRANSFER', 'Transfer'

    booking = models.OneToOneField(Booking, related_name="payment", on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateTimeField(auto_now_add=True)
    method = models.CharField(max_length=10, choices=Method.choices, default=Method.CARD)

    def __str__(self):
        return f"{self.booking} - {self.amount} - {self.date}"