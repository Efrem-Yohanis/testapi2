from django.db import models
from django.utils import timezone

class Portfolio(models.Model):
    event_id= models.CharField(max_length=50, null=true, blank=true)
    event_type= models.CharField(max_length=50, null=true, blank=true)
    user_sk = models.CharField(max_length=50)
    user_id = models.CharField(max_length=50)
    number = models.CharField(max_length=50)
    name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    first_name = models.CharField(max_length=100)
    is_active = models.BooleanField(default=True)
    broker_dealer_id = models.CharField(max_length=50, null=True, blank=True)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        indexes = [
            models.Index(fields=['user_id']),
            models.Index(fields=['number']),
        ]

    def __str__(self):
        return f"{self.number} - {self.name}"