# Desafio Técnico — Backend API (Django + DRF)

Este projeto consiste em uma **API REST** desenvolvida com **Django** e **Django REST Framework**, como solução para um desafio técnico de backend.

O objetivo é fornecer endpoints que suportem autenticação, gerenciamento de projetos e listagem/seleção de planos de preços, simulando um backend real consumível por qualquer aplicação frontend.

## 📌 Stack Utilizada

* Python 3.14
* Django 5.2
* Django REST Framework 3.15.0
* PostgreSQL 16
* Autenticação JWT (SimpleJWT) 5.3.1
* Pytest 9.0.2 + pytest-django 4.11.1
* Swagger / OpenAPI

---

## 🧱 Arquitetura do Projeto

O projeto segue a separação por **apps**, respeitando o princípio de responsabilidade única:

* `accounts` → autenticação, registro e dados do usuário
* `projects` → gerenciamento de projetos do usuário autenticado
* `pricing` → listagem e simulação de seleção de planos

A API é **stateless**, protegida por JWT e estruturada de forma escalável e manutenível.

---

## 🧪 Testes Automatizados

O projeto conta com **testes automatizados cobrindo autenticação, projetos e planos**, utilizando **Pytest**.

* Cobertura de testes: **98%**
* Testes de endpoints protegidos
* Testes de regras de negócio

Execução:

```
pytest
```

---

## 📚 Documentação da API

A documentação interativa está disponível via Swagger em:

```
/api/docs/
```

---

## 🧠 Decisões Técnicas

Python 3.14 foi escolhido para o desenvolvimento local por ser uma das versões mais recentes da linguagem, permitindo acompanhar a evolução do ecossistema Python. A utilização dessa versão se reflete na preocupação em manter o projeto alinhado com as tecnologias mais recentes.

Django 5.2 foi adotado por ser uma versão estável e madura do framework. Embora já exista a versão 6.0, optou-se pela 5.2 devido à maior compatibilidade com bibliotecas amplamente utilizadas no ecossistema Django, além de ser uma versão com a qual possuo maior familiaridade.

PostgreSQL 16, foi escolhido pela sua robustez, integridade transacional e maturidade, A decisão pela versão 16 visa equilibrar atualização tecnológica e estabilidade, evitando possíveis problemas de compatibilidade com bibliotecas do Django.

As views genéricas (generics) do Django REST Framework foram utilizadas para acelerar o desenvolvimento e reduzir código repetitivo, mantendo os endpoints claros e padronizados, com personalizações apenas quando necessário.

O endpoint ```api/auth/refresh/```, embora não exigido explicitamente no desafio, foi implementado como boa prática. Ele permite a renovação do token de acesso sem a necessidade de um novo login constante, utilizando um token de refresh com validade maior.

Os testes automatizados utilizam pytest, pytest-django e model-bakery, garantindo que futuras expansões do modelo de dados não quebrem os testes existentes. A cobertura de 98% de todo código, reforça a confiabilidade e segurança na evolução do código.

Os projetos são sempre filtrados pelo usuário autenticado. Já o módulo pricing é global, pois os planos devem estar disponíveis independentemente do usuário. Para relacionar usuários a planos, foi criado o modelo UserProfile, que é automaticamente instanciado no registro do usuário e atualizado quando um plano é selecionado.
A validação dos dados de entrada é feita prioritariamente nos serializers, mantendo as views mais limpas e seguindo as boas práticas do DRF.

A validação de dados é realizada prioritariamente nos serializers, mantendo as views mais simples e alinhadas às boas práticas do Django REST Framework.

A arquitetura foi organizada por apps independentes (accounts, projects, pricing), para separação das responsabilidades de cada um e também com a ideia de separação dos módulos, facilitando a manutenção e a expansão dos projeto posteriomente.

A documentação da API é gerada automaticamente via Swagger/OpenAPI, com descrições detalhadas dos endpoints para facilitar o consumo por aplicações frontend.

No ambiente Docker, foi utilizado Python 3.12-slim, por ser uma versão estável e amplamente suportada em produção. Essa escolha garante maior compatibilidade com bibliotecas e não impacta o funcionamento da aplicação em relação ao ambiente local.

As variáveis de ambiente foram padronizadas com o prefixo POSTGRES_, assegurando compatibilidade com a imagem oficial do PostgreSQL e facilitando a integração com o Docker Compose. A aplicação Django se conecta ao banco utilizando o nome do serviço Docker como host.

---

## ▶️ Como Executar o Projeto (sem Docker)

1. Criar ambiente virtual (Windows)

```
python -m venv venv
venv\Scripts\activate
```

2. Instalar dependências

```
pip install -r requirements.txt
```

3. Configurar variáveis de ambiente (.env)

4. Rodar migrations

```
python manage.py migrate
```

5. Iniciar o servidor

```
python manage.py runserver
```
---

## ▶️ Como Executar o Projeto (com Docker)

1. Criar o arquivo .env com as variáveis necessárias

2. Subir os containers

```
docker-compose up --build
```

3. Executar as migrations

```
docker-compose exec api python manage.py migrate
```

4. A aplicação ficará disponível em:

```
http://localhost:8000
```

---

## 📬 Considerações Finais

Este projeto foi desenvolvido com foco em:

* Clareza nas estruturas
* Boas práticas em APIs REST
* Testabilidade
* Organização e legibilidade

Este projeto não contempla versionamento de API ou controle de permissões avançadas por escopo, porém tem como margem uma possível expansão futura.

O objetivo principal é demonstrar domínio prático de **Django + DRF** em um contexto realista de backend.
