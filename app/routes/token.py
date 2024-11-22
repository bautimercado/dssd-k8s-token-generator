from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session

from app.crud.token import generate_token, get_winner
from app.db.session import get_db

router = APIRouter()

@router.post('/generate-token/')
def create_token(collection_point: int, db: Session = Depends(get_db)) -> int:
    """
    Endpoint POST para crear un token.
    - Si el token se puede crear, lo retorna.
    - Sino, se levanta una excepción.
    """
    try:
        token = generate_token(collection_point, db)
        return {'message': 'Token generado', 'token': token}
    except Exception as e:
        return HTTPException(status_code=400, detail=str(e))


@router.get('/winner/')
def get_winner_route(db: Session = Depends(get_db)) -> int:
    """
    Endpoint GET para retornar el token del ganador
    """
    winner_token = get_winner(db)
    if winner_token:
        return {'message': 'Ganador seleccionado', 'token': winner_token}
    raise HTTPException(status_code=404, detail="No hay tokens registrados")
