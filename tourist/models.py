from pyexpat import model
from django.db import models
from django.contrib.auth.models import User
from guide.models import Guide
import uuid


class Tourist(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
    first_name = models.CharField(max_length=200, blank=True, null=True)
    last_name = models.CharField(max_length=200, blank=True, null=True)
    username = models.CharField(max_length=200, blank=True, null=True)
    password = models.CharField(max_length=200, blank=True, null=True)
    confirm_password = models.CharField(max_length=200, blank=True, null=True)
    email = models.CharField(max_length=500, blank=True, null=True)
    phone = models.CharField(max_length=500, blank=True, null=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.username)

class Booking(models.Model):
    tourist = models.ForeignKey(to=Tourist, blank=True, null=True, on_delete=models.SET_NULL)
    guide = models.ForeignKey(to=Guide, blank=True, null=True, on_delete=models.SET_NULL)
    offer = models.DecimalField(max_digits=100, decimal_places=2, blank=True, null=True, default=1.0)
    status = models.CharField(max_length=200, blank=True, null=True, default='Pending')
    trip_duration = models.CharField(max_length=200, blank=True, null=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)
    created = models.DateTimeField(auto_now_add=True)
    
