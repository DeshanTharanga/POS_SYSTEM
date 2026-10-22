from typing import AsyncGenerator

from dotenv import load_dotenv
import os
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker, AsyncSession
from sqlalchemy.orm import declarative_base

load_dotenv()  #loding environment variable in .env file

DB_HOST = os.getenv("DB_HOST", "localhost")
DB_NAME = os.getenv("DB_NAME", "bookshop_db")
DB_USER= os.getenv("DB_USER", "postgres")
DB_PASSWORD= os.getenv("DB_PASSWORD", "123")
DB_PORT= os.getenv("DB_PORT", "5432")
POOL_SIZE = os.getenv("POOL_SIZE",5)
MAX_OVER_FLOW = os.getenv("MAX_OVER_FLOW",10)

DB_URL = f"postgresql+asyncpg://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"


engine = create_async_engine(
    DB_URL,
    pool_size= int(POOL_SIZE),
    max_overflow= int(MAX_OVER_FLOW),
    echo=False
)

async_session = async_sessionmaker(
    engine,
    class_=AsyncSession,
    expire_on_commit=False,
    autocommit=False,
    autoflush=False
)

Base = declarative_base()

async def get_session() -> AsyncGenerator[AsyncSession, None]: #Generator Function

    async with async_session() as session:
        yield session

async def init_db() -> None:

    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)

async def close_db() -> None:

    await engine.dispose()
