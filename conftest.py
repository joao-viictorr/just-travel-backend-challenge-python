import pytest

from django.contrib.auth.models import User
from projects.models import Project
from pricing.models import Pricing
from rest_framework.test import APIClient


@pytest.fixture
def create_user_fixture():
    return User.objects.create_user(
        username="pedro",
        password="123456"
    )


@pytest.fixture
def auth_client_fixture(create_user_fixture):
    client = APIClient()

    response = client.post(
        "/api/auth/login/",
        {
            "username": "pedro",
            "password": "123456"
        },
        format="json"
    )

    token = response.data["access"]
    client.credentials(HTTP_AUTHORIZATION=f"Bearer {token}")

    return client

@pytest.fixture
def project_fixture(create_user_fixture):
    return Project.objects.create(
        title="Projeto Teste",
        description="Descrição do projeto",
        user=create_user_fixture
    )


@pytest.fixture
def other_user_project():
    from django.contrib.auth.models import User

    user = User.objects.create_user(
        username="outro_user",
        password="123456"
    )

    return Project.objects.create(
        title="Projeto de outro usuário",
        description="Não deveria aparecer",
        user=user
    )


@pytest.fixture
def pricing_fixture(db):
    return Pricing.objects.create(
        plan_name="Plano Básico",
        description="Plano teste",
        price=99.90,
        is_active=True
    )


@pytest.fixture
def pricing_inactive_fixture(db):
    return Pricing.objects.create(
        plan_name="Plano Inativo",
        description="Plano inativo",
        price=199.90,
        is_active=False
    )
