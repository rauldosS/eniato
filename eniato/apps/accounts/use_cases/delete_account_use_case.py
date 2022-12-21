from apps.accounts.repositories import AccountRepository
from apps.transaction.repositories.transaction_repository import TransactionRepository

class DeleteAccountUseCase(object):

    def __init__(self, repository=None, transaction_repository=None):
        self.repository = repository or AccountRepository()
        self.transaction_repository = transaction_repository or TransactionRepository()

    def execute(self, account_id):
        transactions = self.transaction_repository.get_by_account(account_id)

        for transaction in transactions:
            if transaction.status:
                # update daily balance
                daily_balance = self.daily_balance_repository.get_by_id(transaction.daily_balance.id)
                daily_balance.update_balance(transaction, delete_transactoin=True)
                self.daily_balance_repository.save(daily_balance)

                # update next daily balances
                next_daily_balance = self.repository.get_next_daily_balance(daily_balance.reference_date)

                for domain in next_daily_balance:
                    domain.update_only_balance(transaction)
                    self.repository.save(domain)

            self.transaction_repository.delete_by_id(transaction.id)

        self.repository.delete_by_id(account_id)
