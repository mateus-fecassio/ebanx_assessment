from fastapi import FastAPI, Response
from app.api.v1.endpoints import balance, event
from app.infrastructure.repositories.account_repository import AccountRepository

app = FastAPI(
    title="Ebanx Account API",
    description="API for Account Management.",
    version="1.0.0",
    docs_url="/docs"
)

app.include_router(balance.router, prefix="/balance", tags=["balance"])
app.include_router(event.router, prefix="/event", tags=["event"])

@app.post("/reset",
    summary="Reset system state.",
    description="Reset all accounts from the database."
)
def reset():
    AccountRepository.reset()
    return Response(content="OK", status_code=200)