from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_reset_state():
    response = client.post("/reset")
    assert response.status_code == 200
    assert response.text == "OK"

def test_get_balance_non_existing_account():
    response = client.get("/balance?account_id=1234")
    assert response.status_code == 404
    assert response.json() == 0

def test_create_account_with_initial_balance():
    response = client.post("/event", json={
        "type": "deposit",
        "destination": "100",
        "amount": 10
    })
    assert response.status_code == 201
    assert response.json() == {"destination": {"id": "100", "balance": 10}}

def test_deposit_into_existing_account():
    response = client.post("/event", json={
        "type": "deposit",
        "destination": "100",
        "amount": 10
    })
    assert response.status_code == 201
    assert response.json() == {"destination": {"id": "100", "balance": 20}}

def test_get_balance_existing_account():  
    response = client.get("/balance?account_id=100")
    assert response.status_code == 200
    assert response.json() == 20

def test_withdraw_from_non_existing_account():
    response = client.post("/event", json={
        "type": "withdraw",
        "origin": "200",
        "amount": 10
    })
    assert response.status_code == 404
    assert response.json() == 0

def test_withdraw_from_existing_account():  
    response = client.post("/event", json={
        "type": "withdraw",
        "origin": "100",
        "amount": 5
    })
    assert response.status_code == 201
    assert response.json() == {"origin": {"id": "100", "balance": 15}}

def test_transfer_from_existing_account():
    response = client.post("/event", json={
        "type": "transfer",
        "origin": "100",
        "amount": 15,
        "destination": "300"
    })
    assert response.status_code == 201
    assert response.json() == {
        "origin": {"id": "100", "balance": 0},
        "destination": {"id": "300", "balance": 15}
    }

def test_transfer_from_non_existing_account():
    response = client.post("/event", json={
        "type": "transfer",
        "origin": "200",
        "amount": 15,
        "destination": "300"
    })
    assert response.status_code == 404
    assert response.json() == 0