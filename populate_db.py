"""
Script para popular o banco de dados com dados iniciais para teste da API
"""
from datetime import datetime
from uuid import uuid4
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from workoutapi.configs.settings import settings
from workoutapi.categorias.models import CategoriaModel
from workoutapi.centro_treinamento.models import CentroTreinamentoModel
from workoutapi.Atleta.models import AtletaModel


def populate_database():
    """Popula o banco com dados iniciais"""
    
    # Criar engine e session
    engine = create_async_engine(settings.DB_URL)
    async_session = sessionmaker(
        engine, class_=AsyncSession, expire_on_commit=False
    )
    
    async with async_session() as session:
        # Verificar se já existem dados
        existing_categories = await session.execute("SELECT COUNT(*) FROM categorias")
        if existing_categories.scalar() > 0:
            print("Banco já possui dados. Saindo...")
            return
        
        # Categorias
        categorias = [
            CategoriaModel(id=uuid4(), nome="Scale", created_at=datetime.utcnow()),
            CategoriaModel(id=uuid4(), nome="Rx", created_at=datetime.utcnow()),
            CategoriaModel(id=uuid4(), nome="Masters", created_at=datetime.utcnow()),
        ]
        
        for categoria in categorias:
            session.add(categoria)
        
        # Centros de treinamento
        centros = [
            CentroTreinamentoModel(id=uuid4(), nome="CT King", endereco="Rua A, 123", proprietario="João Silva", created_at=datetime.utcnow()),
            CentroTreinamentoModel(id=uuid4(), nome="CT Strong", endereco="Rua B, 456", proprietario="Maria Santos", created_at=datetime.utcnow()),
            CentroTreinamentoModel(id=uuid4(), nome="CT Power", endereco="Rua C, 789", proprietario="Pedro Costa", created_at=datetime.utcnow()),
        ]
        
        for centro in centros:
            session.add(centro)
        
        await session.commit()
        
        # Atletas
        atletas = [
            AtletaModel(
                id=uuid4(),
                nome="João Silva",
                cpf="12345678901",
                idade=25,
                peso=75.5,
                altura=1.75,
                sexo="M",
                categoria_id=categorias[0].pk_id,
                centro_treinamento_id=centros[0].pk_id,
                created_at=datetime.utcnow()
            ),
            AtletaModel(
                id=uuid4(),
                nome="Maria Santos",
                cpf="98765432100",
                idade=28,
                peso=65.0,
                altura=1.68,
                sexo="F",
                categoria_id=categorias[1].pk_id,
                centro_treinamento_id=centros[1].pk_id,
                created_at=datetime.utcnow()
            ),
            AtletaModel(
                id=uuid4(),
                nome="Pedro Costa",
                cpf="11122233344",
                idade=32,
                peso=80.2,
                altura=1.82,
                sexo="M",
                categoria_id=categorias[2].pk_id,
                centro_treinamento_id=centros[2].pk_id,
                created_at=datetime.utcnow()
            ),
            AtletaModel(
                id=uuid4(),
                nome="Ana Paula",
                cpf="55566677788",
                idade=24,
                peso=58.3,
                altura=1.65,
                sexo="F",
                categoria_id=categorias[0].pk_id,
                centro_treinamento_id=centros[0].pk_id,
                created_at=datetime.utcnow()
            ),
            AtletaModel(
                id=uuid4(),
                nome="Carlos Alberto",
                cpf="99988877766",
                idade=35,
                peso=85.7,
                altura=1.78,
                sexo="M",
                categoria_id=categorias[1].pk_id,
                centro_treinamento_id=centros[1].pk_id,
                created_at=datetime.utcnow()
            ),
        ]
        
        for atleta in atletas:
            session.add(atleta)
        
        await session.commit()
        
        print("Banco de dados populado com sucesso!")
        print(f"- {len(categorias)} categorias criadas")
        print(f"- {len(centros)} centros de treinamento criados")
        print(f"- {len(atletas)} atletas criados")


if __name__ == "__main__":
    asyncio.run(populate_database())