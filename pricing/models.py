from django.db import models
from django.contrib.auth.models import User

class Pricing(models.Model):
    plan_name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class meta:
        db_table = "pricing"

    def __str__(self):
        return f"{self.plan_name} - {self.price}"

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    pricing = models.ForeignKey(Pricing, on_delete=models.SET_NULL, null=True, blank=True)

    class meta:
        db_table = "user_profile"

    def __str__(self):
        return f"{self.user.username} - {self.pricing.plan_name if self.pricing else 'No Plan'}"
