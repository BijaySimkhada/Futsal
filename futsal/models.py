from django.db import models
from account.models import Account, FutsalInfo


class Booking(models.Model):
    verified = models.BooleanField(default=False)
    booked_date = models.DateField(null=False)
    booked_time = models.TimeField(null=False)
    booked_at = models.DateTimeField(auto_now_add=True)
    booked_by = models.ForeignKey(Account, on_delete=models.CASCADE, null=False)
    booked_futsal = models.CharField(max_length=40)
    contact = models.CharField(max_length=20, default=None)
