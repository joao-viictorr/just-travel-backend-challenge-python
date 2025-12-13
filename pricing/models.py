from django.db import models
from django.contrib.auth.models import User

class Pricing(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="pricing")
    plant_name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.plant_name} - {self.price}"
