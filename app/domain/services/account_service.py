from app.infrastructure.repositories.account_repository import AccountRepository

class AccountService:
    @staticmethod
    def get_balance(account_id:str) -> tuple[int, int]:
        account = AccountRepository.get_account(account_id)
        if not account:
            return 404, 0
        return 200, account.balance