from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from pydantic import BaseModel

from app.crud.token import generate_token, get_winner
from app.db.session import get_db

router = APIRouter()

class GenerateTokenRequest(BaseModel):
    collection_point: int

@router.post('/generate-token/')
def create_token(request: GenerateTokenRequest, db: Session = Depends(get_db)) -> dict:
    """
    Endpoint POST para crear un token.
    - Si el token se puede crear, lo retorna.
    - Sino, se levanta una excepción.
    """
    print(f'PROCESANDO TOKEN PARA {request.collection_point}')
    try:
        token = generate_token(request.collection_point, db)
        return {'message': 'Token generado', 'token': token}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e)) from e


@router.get('/winner/')
def get_winner_route(db: Session = Depends(get_db)) -> dict:
    """
    Endpoint GET para retornar el token del ganador
    """
    winner_token = get_winner(db)
    if winner_token:
        return {'message': 'Ganador seleccionado', 'token': winner_token}
    raise HTTPException(status_code=404, detail='No hay tokens registrados')
