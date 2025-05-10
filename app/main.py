from fastapi import FastAPI, Response
from app.api.v1.endpoints import balance
from app.infrastructure.repositories.account_repository import AccountRepository

app = FastAPI(
    title="Ebanx Account API",
    description="API for Account Management.",
    version="1.0.0"
)

app.include_router(balance.router, prefix="/balance", tags=["balance"])

@app.post("/reset")
def reset():
    AccountRepository.reset()
    return Response(content="OK", status_code=200)