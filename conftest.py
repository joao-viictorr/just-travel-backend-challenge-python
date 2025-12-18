import pytest

from django.contrib.auth.models import User
from projects.models import Project
from pricing.models import Pricing
from rest_framework.test import APIClient

from model_bakery import baker

@pytest.fixture
def create_user_fixture():
    return User.objects.create_user(
        username="pedro",
        password="123456"
    )


@pytest.fixture
def auth_client_fixture(create_user_fixture):
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
    return baker.make(Project, user=create_user_fixture)


@pytest.fixture
def other_user_project_fixture():
    other_user = baker.make(User)
    return baker.make(Project, user=other_user)


@pytest.fixture
def pricing_active_fixture():
    return baker.make(Pricing, is_active=True)


@pytest.fixture
def pricing_inactive_fixture():
    return baker.make(Pricing, is_active=False)
