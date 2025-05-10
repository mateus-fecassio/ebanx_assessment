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

    @staticmethod
    def withdraw(origin:str, amount:int) -> tuple[int, dict]:
        account = AccountRepository.get_account(origin)
        if not account:
            return 404, 0
        
        if account.withdraw(amount):
            AccountRepository.save_account(account)
            return 201, {"origin": {"id":account.id, "balance":account.balance}}
        return 400, 0

    @staticmethod
    def transfer(origin:str, destination:str, amount:int) -> tuple[int, dict]:
        origin_account = AccountRepository.get_account(origin)
        if not origin_account:
            return 404, 0

        if not origin_account.withdraw(amount):
            return 400, 0

        dest_account = AccountRepository.get_account(destination)
        if not dest_account:
            dest_account = AccountRepository.create_account(destination, amount)
        else:
            dest_account.deposit(amount)
            AccountRepository.save_account(dest_account)

        AccountRepository.save_account(origin_account)
        
        return 201, {
            "origin": {"id":origin_account.id, "balance":origin_account.balance},
            "destination": {"id":dest_account.id, "balance":dest_account.balance}
        } 