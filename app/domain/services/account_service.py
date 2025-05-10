from app.infrastructure.repositories.account_repository import AccountRepository

class AccountService:
    @staticmethod
    def get_balance(account_id:str) -> tuple[int, int]:
        account = AccountRepository.get_account(account_id)
        if not account:
            return 404, 0
        return 200, account.balance
    
    @staticmethod
    def deposit(destination:str, amount:int) -> tuple[int, dict]:
        account = AccountRepository.get_account(destination)
        if not account:
            account = AccountRepository.create_account(destination, amount)
        else:
            account.deposit(amount)
            AccountRepository.save_account(account)
        
        return 201, {"destination": {"id":account.id, "balance":account.balance}}
