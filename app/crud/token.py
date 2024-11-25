import random
from app.models.token import Token
from sqlalchemy.orm import Session


def generate_token(collection_point: int, session: Session) -> int:
    existing_token = session.query(Token).filter(Token.collection_point == collection_point).first()

    if existing_token:
        return existing_token.token

    token = random.randint(1000, 9999)
    while session.query(Token).filter(Token.token == token).first():
        token = random.randint(1000, 9999)

    new_token = Token(
        collection_point=collection_point,
        token=token
    )
    session.add(new_token)
    session.commit()
    return token


def get_winner(session: Session) -> dict:
    tokens = session.query(Token).all()
    if tokens:
        winner = random.choice(tokens)
        return {"token": winner.token, "collection_point": winner.collection_point}
    return None
