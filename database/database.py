from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm.decl_api import declarative_base
from sqlalchemy.orm.session import sessionmaker

from settings import get_settings

settings = get_settings()

engine = create_async_engine(
    url=settings.SQLITE_URL, connect_args={"check_same_thread": False}
)
SessionLocal = sessionmaker(
    autocommit=False, autoflush=False, bind=engine, class_=AsyncSession
)

Base = declarative_base()
