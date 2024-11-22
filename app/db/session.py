from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.models import Base
from app.core.config import DATABASE_URL

engine = create_engine(DATABASE_URL)
Base.metadata.create_all(engine)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def get_db():
    """
    Función para obtener la sesión de la base de datos
    """
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
