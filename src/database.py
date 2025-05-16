import databases
import sqlalchemy as sa
from sqlalchemy.ext.asyncio import create_async_engine
from src.config import settings

# Configuração do banco de dados assíncrono
database = databases.Database(settings.DATABASE_URL)
metadata = sa.MetaData()

def get_engine():
    """Retorna o engine apropriado para o ambiente"""
    if settings.is_production:
        # PostgreSQL em produção
        return create_async_engine(
            settings.DATABASE_URL,
            pool_size=20,
            max_overflow=10
        )
    else:
        # SQLite em desenvolvimento
        return create_async_engine(
            settings.DATABASE_URL,
            connect_args={"check_same_thread": False}
        )

engine = get_engine()

async def connect_db():
    """Conecta ao banco de dados"""
    await database.connect()

async def disconnect_db():
    """Desconecta do banco de dados"""
    await database.disconnect()