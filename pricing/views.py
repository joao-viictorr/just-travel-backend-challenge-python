from .models import Pricing

from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from drf_spectacular.utils import extend_schema, OpenApiResponse

from .serializers import PricingSerializer
from .serializers import PricingSelectSerializer

@extend_schema(
    summary="Listar planos disponíveis",
    description="Retorna os planos disponíveis para seleção.",
    tags=["Pricing"],
    responses={
        200: OpenApiResponse(
            response=PricingSerializer,
            description="Operação realizada com sucesso"
        ),
        401: OpenApiResponse(
            description="Usuário não autenticado"
        ),
        404: OpenApiResponse(
            description="Recurso não encontrado"
        ),
    }
)
class PricingListView(generics.ListAPIView):
    queryset = Pricing.objects.all()
    serializer_class = PricingSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Pricing.objects.filter(is_active=True)[:3]


@extend_schema(
    summary="Selecionar plano",
    description="Associa um plano ao usuário autenticado.",
    tags=["Pricing"],
    responses={
        200: OpenApiResponse(
            response=PricingSelectSerializer,
            description="Recurso criado com sucesso"
        ),
        400: OpenApiResponse(
            description="Dados inválidos enviados na requisição"
        ),
        401: OpenApiResponse(
            description="Usuário não autenticado"
        ),
    }
)
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
