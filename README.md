# DSSD 2024 - Extensión de Kubernetes

## Entorno virtual

Activar entorno virutal (si no está la carpeta venv, ejecutar también la primera instrucción, si la carpeta está no es necesario ejecutarla):
- Linux:
    ```bash
    python -m venv venv
    source venv/bin/activate
    ```
- Windows:
    ```powershell
    python -m venv venv
    venv\Scripts\activate
    ```

## Instalar dependencias:
```bash
pip install -r requirements.txt
```

## Levantar servidor:
```bash
uvicorn app.main:app --reload
```

## Ejecución de tests:
```bash
pytest
```
