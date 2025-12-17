from rest_framework import serializers
from .models import Pricing

class PricingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pricing
        fields = ["id", "plan_name", "description", "price"]
        read_only_fields = ["id", "created_at"]


class PricingSelectSerializer(serializers.Serializer):
    pricing_id = serializers.IntegerField()

    def validate_pricing_id(self, value):
        if not Pricing.objects.filter(id=value, is_active=True).exists():
            raise serializers.ValidationError("Plano inválido.")
        return value
