from .models import Pricing

from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from .serializers import PricingSerializer
from .serializers import PricingSelectSerializer

class PricingListView(generics.ListAPIView):
    queryset = Pricing.objects.all()
    serializer_class = PricingSerializer
    permission_classes = [IsAuthenticated]


class PricingSelectView(generics.GenericAPIView):
    serializer_class = PricingSelectSerializer
    permission_classes = [IsAuthenticated]

    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        pricing = Pricing.objects.get(id=serializer.validated_data["pricing_id"])

        request.user.userprofile.pricing = pricing
        request.user.userprofile.save()

        return Response({"message": "Plano selecionado com sucesso", "plan": pricing.plan_name})
