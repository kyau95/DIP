from dotenv import dotenv_values
from .models import Product

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


if __name__ == "__main__":
    pass