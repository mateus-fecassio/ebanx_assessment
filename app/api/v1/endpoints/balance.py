from fastapi import APIRouter, Query, Response
from app.domain.services.account_service import AccountService

router = APIRouter()

@router.get("")
def get_balance(account_id:str = Query(...)):
    status_code, balance = AccountService.get_balance(account_id)
    return Response(content=f"{balance}", status_code=status_code)