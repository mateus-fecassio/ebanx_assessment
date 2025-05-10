from app.domain.models.account import Account

class AccountRepository:
    _accounts = {}

    @classmethod
    def reset(cls):
        cls._accounts.clear()
    
    @classmethod
    def create_account(cls, account_id:str, initial_balance:int = 0) -> Account:
        account = Account(account_id, initial_balance)
        cls._accounts[account_id] = account
        return account

    @classmethod
    def get_account(cls, account_id:str) -> Account:
        return cls._accounts.get(account_id)

    @classmethod
    def save_account(cls, account:Account) -> None:
        cls._accounts[account.id] = account 