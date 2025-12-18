import pytest
from rest_framework.test import APIClient


@pytest.mark.django_db
def test_listar_planos(auth_client_fixture, pricing_active_fixture):
    response = auth_client_fixture.get("/api/pricing/")

    assert response.status_code == 200
    assert len(response.data) >= 1


@pytest.mark.django_db
def test_selecionar_plano(
    auth_client_fixture,
    pricing_active_fixture,
    create_user_fixture
):
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
    payload = {"pricing_id": 999}

    response = auth_client_fixture.post(
        "/api/pricing/select/",
        payload,
        format="json"
    )

    assert response.status_code == 400
    assert "pricing_id" in response.data
