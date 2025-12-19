import pytest
from rest_framework.test import APIClient

@pytest.mark.django_db
def test_projects_sem_token_retorna_401():
    """
    Garante que a listagem de projetos é protegida por autenticação.
    """
    client = APIClient()

    response = client.get("/api/projects/")

    assert response.status_code == 401


@pytest.mark.django_db
def test_listar_apenas_projetos_do_usuario(auth_client_fixture, project_fixture, other_user_project_fixture):
    """
    Garante isolamento de dados entre usuários diferentes gerados pelo baker.
    """
    response = auth_client_fixture.get("/api/projects/")

    assert response.status_code == 200
    assert len(response.data) == 1

    project = response.data[0]
    assert project["id"] == project_fixture.id
    assert project["id"] != other_user_project_fixture.id


@pytest.mark.django_db
def test_criar_projeto_com_usuario_autenticado(auth_client_fixture):
    """
    Testa a criação de um novo projeto (CRUD).
    """
    payload = {
        "title": "Novo Projeto",
        "description": "Projeto criado via teste"
    }

    response = auth_client_fixture.post(
        "/api/projects/",
        payload,
        format="json"
    )

    assert response.status_code == 201
    assert response.data["title"] == "Novo Projeto"


@pytest.mark.django_db
def test_nao_acessar_projeto_de_outro_usuario(
    auth_client_fixture,
    other_user_project_fixture
):
    """
    Tenta acessar via GET o ID de um projeto que pertence a outro usuário.
    A API deve retornar o status 404 ou o status 403
    """
    response = auth_client_fixture.get(
        f"/api/projects/{other_user_project_fixture.id}/"
    )

    assert response.status_code in (403, 404)


@pytest.mark.django_db
def test_atualizar_projeto_patch(
    auth_client_fixture,
    project_fixture
):
    """
    Testa a atualização parcial de um projeto via PATCH.
    """
    payload = {
        "title": "Projeto Atualizado"
    }

    response = auth_client_fixture.patch(
        f"/api/projects/{project_fixture.id}/",
        payload,
        format="json"
    )

    assert response.status_code == 200
    assert response.data["title"] == "Projeto Atualizado"


@pytest.mark.django_db
def test_delete_projeto_nao_permitido(
    auth_client_fixture,
    project_fixture
):
    """
    Garante que método (DELETE) está bloqueados.
    """
    response = auth_client_fixture.delete(
        f"/api/projects/{project_fixture.id}/"
    )

    assert response.status_code == 405
