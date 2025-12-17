from django.contrib.auth.models import User

from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer, TokenRefreshSerializer
from drf_spectacular.utils import extend_schema, OpenApiResponse

from .serializers import RegisterSerializer
from .serializers import UserMeSerializer


@extend_schema(
    summary="Registro de usuário",
    description="Cria um novo usuário no sistema.",
    tags=["Auth"],
    responses={
        201: OpenApiResponse(
            response=RegisterSerializer,
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
class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = RegisterSerializer


@extend_schema(
    summary="Login do usuário",
    description="Autentica o usuário e retorna os tokens JWT (access e refresh).",
    tags=["Auth"],
    request=TokenObtainPairSerializer,
    responses={
        200: OpenApiResponse(
            response=TokenObtainPairSerializer,
            description="Login realizado com sucesso"
        ),
        401: OpenApiResponse(description="Credenciais inválidas"),
    }
)
class LoginView(TokenObtainPairView):
    pass

@extend_schema(
    summary="Atualizar token de acesso",
    description="Gera um novo token de acesso a partir de um refresh token válido.",
    tags=["Auth"],
    request=TokenRefreshSerializer,
    responses={
        200: OpenApiResponse(
            response=TokenRefreshSerializer,
            description="Token atualizado com sucesso"
        ),
        401: OpenApiResponse(description="Refresh token inválido ou expirado"),
    }
)
class RefreshTokenView(TokenRefreshView):
    pass


@extend_schema(
    summary="Dados do usuário autenticado",
    description="Retorna as informações do usuário logado.",
    tags=["Auth"],
    responses={
        200: OpenApiResponse(
            response=UserMeSerializer,
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

class MeView(generics.RetrieveAPIView):
    serializer_class = UserMeSerializer
    permission_classes = [IsAuthenticated]

    def get_object(self):
        return self.request.user
