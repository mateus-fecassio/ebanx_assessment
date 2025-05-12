# EBANX ASSESSMENT
Simple API for managing bank accounts and events.

## Running the Project

### Using Docker
```bash
Build the container:
docker build -t ebanx-api .

If you need to expose your API to the Internet, you may use Ngrok:
docker run -p 8000:8000 -e NGROK_AUTHTOKEN=<YOUR_TOKEN_HERE> ebanx-api /app/start.sh

If you don't, just use:
docker run -p 8000:8000 ebanx-api /app/start.sh
```

### Locally
```bash
pip install -r requirements.txt
uvicorn app.main:app --reload
```

### Tests
```bash
pytest
``` 

## API Documentation

### Endpoints

| Endpoint | Method | Description |
|----------|--------|-------------|
| `/reset` | POST | Reset system state. |
| `/balance` | GET | Check account balance. |
| `/event` | POST | Process operations (deposit, withdraw, transfer). |


### Request Parameters

#### Balance Endpoint:
| Parameter | Type | Description |
|-----------|------|-------------|
| `account_id` | string | ID of the account to check balance. |

#### Event Endpoint:
| Parameter | Type | Description |
|-----------|------|-------------|
| `type` | string | Type of operation (deposit, withdraw or transfer). |
| `origin` | string | Source account ID (**required for withdraw and transfer**). |
| `destination` | string | Destination account ID (**required for deposit and transfer**). |
| `amount` | integer | Amount to be processed. |

### Usage Examples

#### Reset System State:
```bash
curl -X POST "http://localhost:8000/reset"
```

#### Check Balance:
```bash
curl -X GET "http://localhost:8000/balance?account_id=100"
```

#### Deposit:
```bash
curl -X POST "http://localhost:8000/event" \
     -H "Content-Type: application/json" \
     -d '{"type":"deposit", "destination":"100", "amount":10}'
```

#### Withdrawal:
```bash
curl -X POST "http://localhost:8000/event" \
     -H "Content-Type: application/json" \
     -d '{"type":"withdraw", "origin":"100", "amount":5}'
```

#### Transfer:
```bash
curl -X POST "http://localhost:8000/event" \
     -H "Content-Type: application/json" \
     -d '{"type":"transfer", "origin":"100", "amount":15, "destination":"300"}'
```


## GitHub REPO:
[Source Code](https://github.com/mateus-fecassio/ebanx_assessment)

## Authors
- [@mateus-fecassio](https://github.com/mateus-fecassio)