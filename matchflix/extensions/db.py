from databases import Database
from dynaconf import settings

database = Database(settings.DATABASE_DSN)
