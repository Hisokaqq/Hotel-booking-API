from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    class UserType(models.TextChoices):
        GUEST = 'GUEST', 'Guest'
        STAFF = 'STAFF', 'Staff'
        ADMIN = 'ADMIN', 'Admin'

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    
    phone_number = models.CharField(max_length=20)
    email = models.EmailField()
    address = models.CharField(max_length=255)
    type = models.CharField(max_length=10, choices=UserType.choices, default=UserType.GUEST)

    def __str__(self):
        return self.user.username


