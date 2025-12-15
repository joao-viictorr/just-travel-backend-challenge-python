from rest_framework import serializers
from .models import Pricing

class PricingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pricing
        fields = ["id", "plan_name", "description", "price"]


class PricingSelectSerializer(serializers.Serializer):
    pricing_id = serializers.IntegerField()

    def validate_pricing_id(self, value):
        if not Pricing.objects.filter(id=value).exists():
            raise serializers.ValidationError("Plano inválido.")
        return value
