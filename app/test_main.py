from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app,base_url="http://127.0.0.1:8000")

def test_info():

    payload = {"topic_name":"dummy topic 1","start_dt":"","end_dt":""}
    response = client.post("/classify/",params=payload)
    assert response.status_code == 200
    assert response.json() == {'id': 1, 'text': 'It looks great!', 'polarity_score': 1.0}
    