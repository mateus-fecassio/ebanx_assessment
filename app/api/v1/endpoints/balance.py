from fastapi import APIRouter, Query, Response
from app.domain.services.account_service import AccountService

router = APIRouter()

@router.get("",
    summary="Get account balance.",
    description="Retrieve the current balance for a specific account."
)
def get_balance(account_id:str = Query(..., description="ID of the account to check balance.", examples=["100", "101", "102"])):
    status_code, balance = AccountService.get_balance(account_id)
    return Response(content=f"{balance}", status_code=status_code)