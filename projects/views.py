from .models import Project

from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from drf_spectacular.utils import extend_schema, extend_schema_view, OpenApiResponse

from .serializers import ProjectSerializer

@extend_schema_view(
    get=extend_schema(
        summary="Listar projetos",
        description="Retorna todos os projetos pertencentes ao usuário autenticado.",
        tags=["Projects"],
        responses={
            200: OpenApiResponse(
                response=ProjectSerializer,
                description="Operação realizada com sucesso"
            ),
            401: OpenApiResponse(
                description="Usuário não autenticado"
            ),
            404: OpenApiResponse(
                description="Recurso não encontrado"
            ),
        }
    ),
    post=extend_schema(
        summary="Criar projeto",
        description="Cria um novo projeto associado ao usuário autenticado.",
        tags=["Projects"],
        request=ProjectSerializer,
        responses={
            201: OpenApiResponse(
                response=ProjectSerializer,
                description="Recurso criado com sucesso"
            ),
            400: OpenApiResponse(
                description="Dados inválidos enviados na requisição"
            ),
            401: OpenApiResponse(
                description="Usuário não autenticado"
            ),
        }
    ),
)
class ProjectListCreateView(generics.ListCreateAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Project.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


@extend_schema_view(
    get=extend_schema(
        summary="Detalhar projeto",
        description="Retorna os dados de um projeto específico do usuário.",
        tags=["Projects"],
        responses={
            200: OpenApiResponse(
                response=ProjectSerializer,
                description="Operação realizada com sucesso"
            ),
            401: OpenApiResponse(
                description="Usuário não autenticado"
            ),
            404: OpenApiResponse(
                description="Recurso não encontrado"
            ),
        }
    ),
    patch=extend_schema(
        summary="Atualizar projeto",
        description="Atualiza parcialmente os dados de um projeto existente.",
        tags=["Projects"],
        request=ProjectSerializer,
        responses={
            201: OpenApiResponse(
                response=ProjectSerializer,
                description="Recurso criado com sucesso"
            ),
            400: OpenApiResponse(
                description="Dados inválidos enviados na requisição"
            ),
            401: OpenApiResponse(
                description="Usuário não autenticado"
            ),
            404: OpenApiResponse(
                description="Recurso não encontrado"
            ),
        }
    ),
)
class ProjectDetailView(generics.RetrieveUpdateAPIView):
    serializer_class = ProjectSerializer
    permission_classes = [IsAuthenticated]
    http_method_names = ["get", "patch"]

    def get_queryset(self):
        return Project.objects.filter(user=self.request.user)
