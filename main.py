from fastapi import FastAPI

app = FastAPI()

@app.get('/')
def read_root():
    """
    Función de prueba
    """
    return {"message": "Hola, FastAPI!"}
