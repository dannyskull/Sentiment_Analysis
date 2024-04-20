from fastapi.testclient import TestClient
import requests

from app.main import app

client = TestClient(app)

def test_info():

    payload = {"topic_name":"dummy topic 1","start_dt":"","end_dt":""}
    response = client.post("/classify/",json=payload)
    print(response.json())
    assert response.status_code == 200
    assert response.json()[0] == {'id': 1, 'text': 'It looks great!', 'polarity_score': 1.0, 'sentiment': 'positive'}
    
