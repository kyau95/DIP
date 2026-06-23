from dotenv import dotenv_values

from redis import Redis
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


CONF = dotenv_values()
engine = create_engine(
    CONF["DB_URL"],
    echo=True if CONF["DEBUG"] == 1 else False
)

SessionLocal = sessionmaker(
    bind=engine,
    autoflush=False,
    autocommit=False,
)

redis_client = Redis(
    host="localhost",
    port=6379,
    decode_responses=True
)

def get_db():
    db = SessionLocal()
    
    try:
        yield db
    except Exception:
        raise
    finally:
        db.close()

def get_redis():
    return redis_client