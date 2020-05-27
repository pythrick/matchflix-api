import databases
from dynaconf import settings
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

database = databases.Database(settings.DATABASE_DSN)

engine = create_engine(settings.DATABASE_DSN, pool_pre_ping=True)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
