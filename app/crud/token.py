import random
from app.models.token import Token
from sqlalchemy.orm import Session


def generate_token(collection_point: int, session: Session) -> int:
    """
    Función que crea un token aleatorio y único para
    el punto de recolección.
    """
    token = random.randint(1000,9999)

    while session.query(Token).filter(Token.token == token).first():
        token = random.randint(1000,9999)

    new_token = Token(
        collection_point=collection_point,
        token=token
    )

    session.add(new_token)
    session.commit()

    return token


def get_winner(session: Session) -> int:
    """
    Función que retorna el token del ganador del sorteo (obtenido
    de manera aleatoria).
    """
    tokens = session.query(Token).all()
    if tokens:
        # THE WINNER TAKES IT ALL
        winner = random.choice(tokens)
        return winner.token
    else:
        return None
