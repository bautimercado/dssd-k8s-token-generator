from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_generate_token():
    """
    Test que hace una request HTTP al endpoint de creación de tokens
    """
    collection_point: int = 123
    token_generation_data: dict = {
        "collection_point": collection_point
    }
    response = client.post('/tokens/generate-token/', json=token_generation_data)
    assert response.status_code == 200
    assert 'token' in response.json()


def test_get_winner():
    """
    Test que obtiene al token ganador
    """
    client.post('/tokens/generate-token/', json={'collection_point': 123})
    response = client.get('/tokens/winner/')
    assert response.status_code == 200
    assert 'token' in response.json()
