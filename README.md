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

Python 3.14 foi escolhido por ser uma das versões mais recentes do python e estável para o desenvolvimento de projetos com django, como a ideia é simular um sistema backend de api, eu achei interessante usar essa versão por ser estável e devido que as tecnologias se atualizam constantamente e está alinhado com as novas versões é de suma importância em projetos.

Django 5.2 foi utilizado devido a ser uma versão mais matura, embora, exista a nova versão 6.0, optei por utilizar essa versão pois grande partes das bibliotecas funcionam sem apresentar possíveis erros de compatibilidade entre elas ou com a própria versão do python, além de ser uma versão que tenho mais afinidade.

PostgreSQL 16, a escolha que tomei do banco de dados está relacionada a integridade, maturidade e robustez do PostgreSQL além de ser um banco que tenho maior afinidade. A versão eu escolhi a 16 por ser uma das mais recentes e novamente para evitar possíveis erros de compatibilidade com algumas bibliotecas do django, embora a gente atualmente esteja na versão 18.

A biblioteca generics foi escolhida devido a facilidade e praticidade na hora de criar endpoints na api, por isso em grande parte do projeto tentei ao máximo manter como o padrão ela nas views, ajustando os métodos conforme a necessidade do projeto.

O endpoint api/auth/refresh/ embora não esteja ímplicito no desafio, eu achei interessante criar pois isso permitir eu gerar um novo token de acesso(vida curta), no meu projeto sem a necessidade de ter que a todo momento está realizando o login, e passando o token de refresh que tem a vida útil no nosso projeto de 1 dia, podendo ser extendida, conforme a necessidade, eu criei esse endpoint mais como uma boa prática para o frontend consumir posteriomente.

Os testes automatizados foram utilizados com o pytest, 

Django + Django REST Framework foram escolhidos pela maturidade, robustez e forte adoção no mercado para construção de APIs REST escaláveis.

A arquitetura foi organizada por apps independentes (accounts, projects, pricing), promovendo separação de responsabilidades e facilitando manutenção e evolução do código.

A autenticação foi implementada com JWT (SimpleJWT), permitindo uma API stateless, compatível com aplicações frontend modernas.

O PostgreSQL foi utilizado como banco de dados relacional devido à necessidade de integridade e relacionamento entre entidades.

Os dados de projetos são sempre filtrados pelo usuário autenticado, garantindo segurança e evitando acesso indevido a recursos de terceiros.

A validação de dados de entrada é feita prioritariamente nos serializers, mantendo as views mais limpas e seguindo boas práticas do DRF.

O endpoint de seleção de plano (POST /api/pricing/select/) recebe o identificador do plano no corpo da requisição, respeitando a semântica REST e facilitando extensões futuras.

O projeto conta com testes automatizados utilizando Pytest, alcançando aproximadamente 98% de cobertura, garantindo confiabilidade e segurança na evolução do código.

A documentação da API é gerada automaticamente via Swagger/OpenAPI, permitindo fácil exploração e consumo dos endpoints.

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

## 📬 Considerações Finais

Este projeto foi desenvolvido com foco em:

* Clareza de código
* Boas práticas em APIs REST
* Testabilidade
* Organização e legibilidade

O objetivo principal é demonstrar domínio prático de **Django + DRF** em um contexto realista de backend.
