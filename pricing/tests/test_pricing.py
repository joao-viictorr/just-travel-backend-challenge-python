import pytest
from rest_framework.test import APIClient


@pytest.mark.django_db
def test_listar_planos(auth_client_fixture, pricing_active_fixture):
    """
    Garante que a listagem de planos está acessível e retornando dados.
    """
    response = auth_client_fixture.get("/api/pricing/")

    assert response.status_code == 200
    assert len(response.data) >= 1


@pytest.mark.django_db
def test_selecionar_plano(
    auth_client_fixture,
    pricing_active_fixture,
    create_user_fixture
):
    """
    Testa a lógica de negócio de contratação de plano.
    Verifica se, após o POST, o perfil do usuário foi atualizado no banco.
    """
    payload = {"pricing_id": pricing_active_fixture.id}

    response = auth_client_fixture.post(
        "/api/pricing/select/",
        payload,
        format="json"
    )

    assert response.status_code == 200
    assert response.data["plan"] == pricing_active_fixture.plan_name

    create_user_fixture.userprofile.refresh_from_db()
    assert create_user_fixture.userprofile.pricing == pricing_active_fixture


@pytest.mark.django_db
def test_selecionar_plano_inexistente(auth_client_fixture):
    """
    Testa o tratamento de erro ao tentar contratar um plano que não existe ou de outro usuário.
    Espera-se um Bad Request (400).
    """
    payload = {"pricing_id": 999}

    response = auth_client_fixture.post(
        "/api/pricing/select/",
        payload,
        format="json"
    )

    assert response.status_code == 400
    assert "pricing_id" in response.data
