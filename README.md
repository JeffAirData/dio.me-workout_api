# FastAPI
### Quem é o FastAPi?
Framework FastAPI, alta performance, fácil de aprender, fácil de codar, pronto para produção.
FastAPI é um moderno e rápido (alta performance) framework web para construção de APIs com Python 3.6 ou superior, baseado nos type hints padrões do Python.

### Async
Código assíncrono apenas significa que a linguagem tem um jeito de dizer para o computador / programa que em certo ponto, ele terá que esperar por algo para finalizar em outro lugar

# Projeto
## WorkoutAPI

Esta é uma API de competição de crossfit chamada WorkoutAPI (isso mesmo rs, eu acabei unificando duas coisas que gosto: codar e treinar). É uma API pequena, devido a ser um projeto mais hands-on e simplificado nós desenvolveremos uma API de poucas tabelas, mas com o necessário para você aprender como utilizar o FastAPI.

## Modelagem de entidade e relacionamento - MER
![MER](/mer.jpg "Modelagem de entidade e relacionamento")

## Stack da API

A API foi desenvolvida utilizando o `fastapi` (async), junto das seguintes libs: `alembic`, `SQLAlchemy`, `pydantic`. Para salvar os dados está sendo utilizando o `postgres`, por meio do `docker`.

## Execução da API

Para executar o projeto, utilizei a [pyenv](https://github.com/pyenv/pyenv), com a versão 3.11.4 do `python` para o ambiente virtual.

Caso opte por usar pyenv, após instalar, execute:

```bash
pyenv virtualenv 3.11.4 workoutapi
pyenv activate workoutapi
pip install -r requirements.txt
```
Para subir o banco de dados, caso não tenha o [docker-compose](https://docs.docker.com/compose/install/linux/) instalado, faça a instalação e logo em seguida, execute:

```bash
make run-docker
```
Para criar uma migration nova, execute:

```bash
make create-migrations d="nome_da_migration"
```

Para criar o banco de dados, execute:

```bash
make run-migrations
```

## API

Para subir a API, execute:
```bash
make run
```
e acesse: http://127.0.0.1:8000/docs

# Desafio Final
    - adicionar query parameters nos endpoints
        - atleta
            - nome
            - cpf
    - customizar response de retorno de endpoints
        - get all
            - atleta
                - nome
                - centro_treinamento
                - categoria
    - Manipular exceção de integridade dos dados em cada módulo/tabela
        - sqlalchemy.exc.IntegrityError e devolver a seguinte mensagem: “Já existe um atleta cadastrado com o cpf: x”
        - status_code: 303
    - Adicionar paginação utilizando a lib: fastapi-pagination
        - limit e offset

# Conclusão do Desafio

Ufa! Achei que não iria chegar lá.. mas como o pessoal da Dio.me não brinca em serviço eu também não! Então, toma!
Tive muitas dificuldades durante o processo, mas com ajuda da Nayanna Nara e com um pouco de GitHub Copilot tudo se resolveu.
Meu código se diferenciou um pouco do que foi passado pela Instrutora na busca de uma melhor adequação à realidade que enfrentei, como por exemplo o 'asyncpg' não funcionou nem por reza braba, o que acabou sendo mudado para o 'psycopg2-binary'. Fica a dica.

### Perfeito! Agora temos implementado todos os requisitos do Desafio DIO.me:

✅ Requisitos do Desafio Implementados:

1. Query Parameters nos Endpoints - Atleta ✅
✅ nome: Filtro por nome do atleta
✅ cpf: Filtro por CPF do atleta

2. Response Customizada - GET all Atleta ✅
✅ nome: Nome do atleta
✅ centro_treinamento: Nome do centro de treinamento
✅ categoria: Nome da categoria

3. Exceção de Integridade ✅
✅ sqlalchemy.exc.IntegrityError: Capturada e tratada
✅ Mensagem: "Já existe um atleta cadastrado com o cpf: x"
✅ Status Code: 303

4. Paginação com fastapi-pagination ✅
✅ limit e offset: Implementado através do Page[AtletaCustomOut]
✅ fastapi-pagination: Configurado no main.py

🚀 Funcionalidades Extras Implementadas:
Async/Await: Todas as funções são assíncronas conforme especificado
psycopg: Driver PostgreSQL moderno com suporte async
Tratamento de Erros: Rollback automático em todas as operações
Validação de Dados: Pydantic schemas para validação
Documentação: Swagger UI disponível em /docs

📋 Como Testar:
GET /atletas - Lista todos com paginação
GET /atletas?nome=João - Filtro por nome
GET /atletas?cpf=12345678901 - Filtro por CPF
POST /atletas - Criar atleta (retorna 303 se CPF duplicado)
        
# Referências

FastAPI: https://fastapi.tiangolo.com/

Pydantic: https://docs.pydantic.dev/latest/

SQLAlchemy: https://docs.sqlalchemy.org/en/20/

Alembic: https://alembic.sqlalchemy.org/en/latest/

Fastapi-pagination: https://uriyyo-fastapi-pagination.netlify.app/
