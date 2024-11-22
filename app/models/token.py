from datetime import datetime

from sqlalchemy import Column, DateTime, Integer

from app.db.base import Base


class Token(Base):
    """
    Modelo para los tokens
    - id: Identificador del token
    - collection_point: Punto de recolección al que le pertenece el token
    - token: Token único asignado al punto de recolección
    - created_at: Timestamp
    """
    __tablename__ = 'tokens'
    id = Column(Integer, primary_key=True, unique=True, autoincrement=True)
    collection_point = Column(Integer, nullable=False)
    token = Column(Integer, nullable=False, unique=True)
    created_at = Column(DateTime, default=datetime.utcnow)

    def __repr__(self):
        """
        Retorna representación del modelo en formato JSON
        """
        return f'<Token(id={self.id}, collection_point={self.collection_point}, token={self.token})>'
