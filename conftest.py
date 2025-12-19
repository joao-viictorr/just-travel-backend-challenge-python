import pytest

from django.contrib.auth.models import User
from projects.models import Project
from pricing.models import Pricing
from rest_framework.test import APIClient

from model_bakery import baker

@pytest.fixture
def create_user_fixture():
    """
    Cria um usuário com dados aleatórios via model-bakery, mas define
    uma senha conhecida ('123456') para permitir a autenticação nos testes.
    Isso garante que mudanças no model User (novos campos) não quebrem a fixture.
    """
    user = baker.make(User)
    user.set_password("123456")
    user.save()
    return user


@pytest.fixture
def auth_client_fixture(create_user_fixture):
    """
    Realiza o fluxo de login completo e retorna uma instância de APIClient
    já configurada com o token JWT no header Authorization.
    Útil para testar endpoints protegidos sem repetir o código de login.
    """
    create_user_fixture.set_password("123456")
    create_user_fixture.save()

    client = APIClient()

    response = client.post(
        "/api/auth/login/",
        {
            "username": create_user_fixture.username,
            "password": "123456"
        },
        format="json"
    )

    token = response.data["access"]
    client.credentials(HTTP_AUTHORIZATION=f"Bearer {token}")

    return client


@pytest.fixture
def project_fixture(create_user_fixture):
    """
    Cria um projeto associado ao usuário principal do teste.
    """
    return baker.make(Project, user=create_user_fixture)


@pytest.fixture
def other_user_project_fixture():
    """
    Cria um cenário de 'outro usuário': gera um User novo e um Project dele.
    Essencial para testar isolamento de dados (se eu vejo os dados do vizinho).
    """
    other_user = baker.make(User)
    return baker.make(Project, user=other_user)


@pytest.fixture
def pricing_active_fixture():
    """
    Cria um plano de preços ativo.
    """
    return baker.make(Pricing, is_active=True)


@pytest.fixture
def pricing_inactive_fixture():
    """
    Cria um plano de preços inativo.
    """
    return baker.make(Pricing, is_active=False)
