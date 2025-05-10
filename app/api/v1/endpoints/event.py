from fastapi import APIRouter, Response
from app.domain.services.account_service import AccountService

router = APIRouter()

@router.post("")
def event_handler(event:dict):
    event_type = event.get("type")
    
    if event_type == "deposit":
        status_code, response = AccountService.deposit(
            event["destination"],
            event["amount"]
        )
        return Response(content=f"{response}", status_code=status_code)
    
    elif event_type == "withdraw":
        status_code, response = AccountService.withdraw(
            event["origin"],
            event["amount"]
        )
        return Response(content=f"{response}", status_code=status_code)
    
    elif event_type == "transfer":
        status_code, response = AccountService.transfer(
            event["origin"],
            event["destination"],
            event["amount"]
        )
        return Response(content=f"{response}", status_code=status_code)
    
    return Response(content="Invalid event type.", status_code=400)