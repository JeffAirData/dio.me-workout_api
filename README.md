# 🏋️ Workout API - Desafio DIO.me

Este projeto é minha implementação do **Desafio "Desenvolvendo sua Primeira API com FastAPI, Python e Docker"** da **Digital Innovation One (DIO.me)**.

## 🎯 **Objetivo do Desafio**

Implementar uma API completa para gerenciamento de atletas, categorias e centros de treinamento, aplicando conceitos avançados de **FastAPI**, **SQLAlchemy**, **PostgreSQL** e **Docker**.

## ✅ **Requisitos Implementados**

### 1. **Query Parameters nos Endpoints - Atleta**
- ✅ **nome**: Filtro por nome do atleta
- ✅ **cpf**: Filtro por CPF do atleta

### 2. **Response Customizada - GET all Atleta**  
- ✅ **nome**: Nome do atleta
- ✅ **centro_treinamento**: Nome do centro de treinamento
- ✅ **categoria**: Nome da categoria

### 3. **Exceção de Integridade**
- ✅ **sqlalchemy.exc.IntegrityError**: Capturada e tratada
- ✅ **Mensagem**: "Já existe um atleta cadastrado com o cpf: x"
- ✅ **Status Code**: 303

### 4. **Paginação com fastapi-pagination**
- ✅ **limit e offset**: Implementado através do `Page[AtletaCustomOut]`
- ✅ **fastapi-pagination**: Configurado no main.py

## 🛠️ **Tecnologias Utilizadas**

- **Python** 3.11+
- **FastAPI** 0.104.1
- **SQLAlchemy** 2.0.43 (Async)
- **PostgreSQL** com **psycopg** (driver async)
- **Alembic** (migrações de banco)
- **Docker** & **Docker Compose**
- **Pydantic** (validação de dados)
- **fastapi-pagination** (paginação)

## 🚀 **Como Executar**

### Pré-requisitos
- Python 3.11+
- Docker e Docker Compose
- Git

### 1. **Clone o repositório**
```bash
git clone https://github.com/JeffAirData/dio.me-workout_api.git
cd dio.me-workout_api
```

### 2. **Inicie o banco de dados**
```bash
docker-compose up -d
```

### 3. **Configure o ambiente virtual**
```bash
python -m venv workoutapi
.\workoutapi\Scripts\Activate.ps1  # Windows
# ou
source workoutapi/bin/activate     # Linux/Mac
```

### 4. **Instale as dependências**
```bash
pip install -r requirements.txt
```

### 5. **Execute as migrações**
```bash
alembic upgrade head
```

### 6. **Inicie o servidor**
```bash
uvicorn workoutapi.main:app --host 0.0.0.0 --port 8001 --reload
```

### 7. **Acesse a documentação**
- **Swagger UI**: http://localhost:8001/docs
- **ReDoc**: http://localhost:8001/redoc

## 📋 **Endpoints Principais**

### **Atletas**
- `GET /atletas` - Lista todos com paginação
- `GET /atletas?nome=João` - Filtro por nome
- `GET /atletas?cpf=12345678901` - Filtro por CPF
- `POST /atletas` - Criar atleta
- `GET /atletas/{id}` - Buscar por ID
- `PATCH /atletas/{id}` - Atualizar atleta
- `DELETE /atletas/{id}` - Deletar atleta

### **Categorias**
- `GET /categorias` - Listar categorias
- `POST /categorias` - Criar categoria
- `GET /categorias/{id}` - Buscar categoria por ID

### **Centros de Treinamento**
- `GET /centros_treinamento` - Listar centros
- `POST /centros_treinamento` - Criar centro
- `GET /centros_treinamento/{id}` - Buscar centro por ID

## 🎨 **Funcionalidades Extras**

- **Async/Await**: Todas as operações são assíncronas
- **Tratamento de Erros**: Rollback automático em falhas
- **Validação de Dados**: Schemas Pydantic robustos
- **Relacionamentos**: Foreign Keys entre tabelas
- **Documentação**: Swagger UI interativa

## 📝 **Estrutura do Projeto**

```
workout_api/
├── workoutapi/
│   ├── Atleta/
│   │   ├── controller.py
│   │   ├── models.py
│   │   └── schemas.py
│   ├── categorias/
│   │   ├── controller.py
│   │   ├── models.py
│   │   └── schemas.py
│   ├── centro_treinamento/
│   │   ├── controller.py
│   │   ├── models.py
│   │   └── schemas.py
│   ├── configs/
│   │   ├── database.py
│   │   └── settings.py
│   ├── contrib/
│   │   ├── dependencies.py
│   │   ├── models.py
│   │   └── schemas.py
│   ├── routers/
│   │   └── api_router.py
│   └── main.py
├── alembic/
├── docker-compose.yml
├── requirements.txt
└── README.md
```

## 🏆 **Conquistas do Desafio**

- ✅ **100% dos requisitos implementados**
- ✅ **Código totalmente assíncrono**
- ✅ **Tratamento robusto de exceções**
- ✅ **Paginação funcional**
- ✅ **Query parameters implementados**
- ✅ **Response customizada**
- ✅ **Arquitetura limpa e escalável**

## 👨‍💻 **Autor**

**Jefferson Magalhães** - [GitHub](https://github.com/JeffAirData)

Desenvolvido como parte do bootcamp **Digital Innovation One (DIO.me)**

## 📚 **Referências**

- [Repositório Original do Desafio](https://github.com/digitalinnovationone/workout_api)
- [FastAPI Documentation](https://fastapi.tiangolo.com/)
- [SQLAlchemy Documentation](https://docs.sqlalchemy.org/)
- [Docker Documentation](https://docs.docker.com/)

---

⭐ **Se este projeto te ajudou, deixe uma estrela!** ⭐