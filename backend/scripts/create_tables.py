

import sys
from pathlib import Path

# Add backend directory to path so we can import src
backend_dir = Path(__file__).parent.parent
sys.path.insert(0, str(backend_dir))

from src.database.session import engine
from src.database.models import BaseModel as Base
from src.database.models import Product
from src.database.models import PriceHistory
from src.database.models import Alert
from src.database.models import ScrapeJob


def create_tables():
    Base.metadata.create_all(bind=engine)