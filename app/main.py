from fastapi import FastAPI
from app.routes.token import router as token_router

app = FastAPI()

app.include_router(token_router, prefix='/tokens', tags=['tokens'])

@app.get('/')
def health_check():
    """
    Función de prueba
    """
    return {"status": "ok"}
