from fastapi import FastAPI
from app.routes.token import router as token_router

app = FastAPI()

app.include_router(token_router, prefix='/tokens', tags=['tokens'])

@app.get('/')
def read_root():
    """
    Función de prueba
    """
    return {"message": "Bienvenido al servicio de generación de tokens."}
