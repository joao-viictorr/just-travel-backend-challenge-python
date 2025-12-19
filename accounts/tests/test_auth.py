import pytest
from rest_framework.test import APIClient


@pytest.mark.django_db
def test_login_com_credenciais_validas(create_user_fixture):
    """
    Deve autenticar o usuário e retornar tokens JWT válidos
    quando credenciais corretas são fornecidas.
    """
    client = APIClient()

    payload = {
        "username": create_user_fixture.username,
        "password": "123456"
    }

    response = client.post("/api/auth/login/", payload, format="json")

    assert response.status_code == 200
    assert "access" in response.data
    assert "refresh" in response.data


@pytest.mark.django_db
def test_me_sem_token_retorna_401():
    """
    Deve impedir acesso ao endpoint /me quando o usuário não está autenticado.
    """
    client = APIClient()

    response = client.get("/api/auth/me/")

    assert response.status_code == 401


@pytest.mark.django_db
def test_me_com_token_retorna_dados(auth_client_fixture, create_user_fixture):
    """
    Deve permitir acesso ao endpoint /me quando o usuário está autenticado.
    """
    response = auth_client_fixture.get("/api/auth/me/")

    assert response.status_code == 200
    assert response.data["username"] == create_user_fixture.username
