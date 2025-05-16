# 🏦 API Bancária Assíncrona com FastAPI - Formação Python Backend Developer

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.11+-blue.svg" alt="Python">
  <img src="https://img.shields.io/badge/FastAPI-0.95+-green.svg" alt="FastAPI">
  <img src="https://img.shields.io/badge/license-MIT-yellow.svg" alt="License">
</p>

## 📝 Descrição

Sistema bancário completo com operações de:
- 💳 Criação de contas
- 💰 Depósitos
- 🏧 Saques
- 📊 Extrato de transações

Desenvolvido com arquitetura limpa e autenticação JWT.

## 🛠 Tecnologias

- **Backend**:
  - 🐍 Python 3.11+
  - ⚡ FastAPI (Framework assíncrono)
  - 🔐 JWT (Autenticação)
  - 🗄️ SQLite (Dev) / PostgreSQL (Prod)
  - 📦 Pydantic (Validação de dados)
  - 🧪 Pytest (Testes)

## 👨‍💻 Autor

**Christian da Silva Barbosa**  
[![GitHub](https://img.shields.io/badge/GitHub-100000?style=flat&logo=github&logoColor=white)](https://github.com/djchristiandf)  
[![LinkedIn](https://img.shields.io/badge/LinkedIn-0077B5?style=flat&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/christian-sbarbosa)

## 🚀 Começando

### Pré-requisitos

- Python 3.11+
- Poetry (gerenciador de dependências)
- Git

### 🔧 Instalação Local

1. Clone o repositório:
```bash
git clone https://github.com/djchristiandf/fastapi-desafio.git
cd fastapi-desafio
Configure o ambiente:

bash
poetry install
cp .env.example .env
Execute as migrações:

bash
poetry run alembic upgrade head
Inicie o servidor:

bash
poetry run uvicorn src.main:app --reload
Acesse a documentação: http://localhost:8000/docs

🧪 Executando Testes
bash
poetry run pytest -v
🌐 Rotas Principais
Método	Rota	Descrição
POST	/auth/login	Autenticação JWT
POST	/accounts	Cria nova conta
GET	/accounts	Lista contas
POST	/transactions	Registra transação
GET	/accounts/{id}/transactions	Extrato da conta
🚀 Deploy em Produção
Opção 1: Fly.io
bash
# Configure as variáveis
fly secrets set DATABASE_URL=postgresql+asyncpg://user:pass@host:5432/db
fly secrets set ENVIRONMENT=production

# Aplique migrações
fly ssh console -a seu-app
alembic upgrade head
exit

# Faça deploy
fly deploy
Opção 2: Render
Crie novo serviço "Web Service"

Conecte ao seu repositório GitHub

Configure variáveis:

DATABASE_URL

ENVIRONMENT=production

Adicione comando de build:

bash
poetry install && alembic upgrade head
📄 Licença
Este projeto está licenciado sob a MIT License - veja o arquivo LICENSE para detalhes.

<p align="center"> Desenvolvido com ❤️ por <a href="https://github.com/djchristiandf">Christian Barbosa</a> </p> ```
Destaques do README:
Cabeçalho visual com badges e emojis

Seção de autor com links sociais

Guia passo-a-passo para instalação

Tabela de rotas para rápida consulta

Instruções de deploy para dois serviços populares

Formatação consistente com emojis temáticos