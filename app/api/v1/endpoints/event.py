import json
from fastapi import APIRouter, Response
from app.domain.services.account_service import AccountService

router = APIRouter()

@router.post("",
    summary="Process account events.",
    description="Process different types of account events: deposit, withdrawal, and transfer."
)
def event_handler(event:dict):
    event_type = event.get("type")
    
    if event_type == "deposit":
        status_code, response = AccountService.deposit(
            event["destination"],
            event["amount"]
        )
        return Response(content=json.dumps(response), status_code=status_code, media_type="application/json")
    
    elif event_type == "withdraw":
        status_code, response = AccountService.withdraw(
            event["origin"],
            event["amount"]
        )
        return Response(content=json.dumps(response), status_code=status_code, media_type="application/json")
    
    elif event_type == "transfer":
        status_code, response = AccountService.transfer(
            event["origin"],
            event["destination"],
            event["amount"]
        )
        return Response(content=json.dumps(response), status_code=status_code, media_type="application/json")
    
    return Response(content="Invalid event type.", status_code=400)