from settings import setting

from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.ext.asyncio import (
    AsyncEngine,
    AsyncSession,
    create_async_engine,
    async_sessionmaker
)


engine: AsyncEngine = create_async_engine(url=setting.db.dsn)
async_session: AsyncSession = async_sessionmaker(bind=engine, expire_on_commit=False)


async def get_async_session():
    async with async_session() as db_session:
        yield db_session
        

class Base(DeclarativeBase):
    pass


