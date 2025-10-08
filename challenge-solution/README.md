# Challenge Solution - Workout API

## 🎯 Desafio DIO.me: Desenvolvendo sua Primeira API com FastAPI, Python e Docker

Esta é a **solução completa** do desafio da DIO.me, implementando todos os requisitos solicitados:

### ✅ Requisitos Implementados

1. **Query Parameters (nome, cpf)** - Filtros na consulta de atletas
2. **Customização de Response** - AtletaCustomOut com campos específicos
3. **Tratamento de Exceção de Integridade** - IntegrityError retorna status 303
4. **Paginação** - Implementada com fastapi-pagination

### 🚀 Como Executar

1. **Clone o repositório**
```bash
git clone https://github.com/JeffAirData/dio.me-workout_api.git
cd dio.me-workout_api/challenge-solution
```

2. **Configure o ambiente virtual**
```bash
python -m venv venv
venv\Scripts\activate  # Windows
# source venv/bin/activate  # Linux/Mac
```

3. **Instale as dependências**
```bash
pip install -r requirements.txt
```

4. **Execute o PostgreSQL com Docker**
```bash
docker-compose up postgres -d
```

5. **Execute as migrações**
```bash
python -m alembic upgrade head
```

6. **Popule o banco (opcional)**
```bash
python populate_db.py
```

7. **Execute a API**
```bash
uvicorn workoutapi.main:app --host 0.0.0.0 --port 8001 --reload
```

### 📊 Endpoints Principais

- **POST** `/atletas` - Cadastrar atleta
- **GET** `/atletas` - Listar atletas (com paginação e filtros)
- **GET** `/atletas/{id}` - Consultar atleta por ID

### 🔍 Query Parameters

```bash
# Filtrar por nome
GET /atletas?nome=João

# Filtrar por CPF
GET /atletas?cpf=12345678900

# Paginação
GET /atletas?offset=0&limit=5
```

### 🛠 Tecnologias Utilizadas

- **FastAPI** 0.104.1 - Framework web async
- **SQLAlchemy** 2.0.43 - ORM assíncrono
- **PostgreSQL** - Banco de dados
- **Docker** - Containerização
- **Alembic** - Migrações
- **fastapi-pagination** 0.12.13 - Paginação
- **psycopg** - Driver async PostgreSQL

### 📝 Estrutura do Projeto

```
challenge-solution/
├── workoutapi/
│   ├── Atleta/          # Módulo de atletas (ASYNC)
│   ├── categorias/      # Módulo de categorias (ASYNC)
│   ├── centro_treinamento/  # Módulo de centros (ASYNC)
│   ├── configs/         # Configurações do banco
│   ├── contrib/         # Modelos base e dependências
│   └── routers/         # Roteadores da API
├── requirements.txt     # Dependências Python
├── docker-compose.yml   # Container PostgreSQL
├── alembic.ini         # Configuração Alembic
└── populate_db.py      # Script para popular banco
```

### 🎯 Diferencial da Implementação

- **100% Assíncrono** - Todos os controllers implementados com async/await
- **Tratamento Completo de Exceções** - IntegrityError retorna status 303
- **Paginação Robusta** - Integração nativa com fastapi-pagination
- **Query Parameters Funcionais** - Filtros por nome e CPF operacionais
- **Response Customizada** - AtletaCustomOut conforme especificação

### 🤝 Contribuição

Esta implementação serve como referência para outros desenvolvedores que estão fazendo o mesmo desafio. Todos os requisitos foram implementados seguindo as melhores práticas do FastAPI.

---

**💡 Dica**: Compare com a pasta `workout_api/` (código original do DIO) para ver as diferenças e melhorias implementadas!