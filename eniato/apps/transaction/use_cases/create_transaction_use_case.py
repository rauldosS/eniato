from apps.transaction.domain import Transaction as TransactionDomain

from apps.transaction.repositories.transaction_repository import TransactionRepository
from apps.transaction.factories import TransactionFactory
from apps.transaction.use_cases.update_daily_balance_use_case import UpdateDailyBalanceUseCase

from apps.category.repositories import CategoryRepository
from apps.accounts.repositories import AccountRepository
from apps.transaction.repositories import DailyBalanceRepository


class CreateTransactionUseCase:

    def __init__(self, transaction_repository=None, transaction_factory=None, update_daily_balance_use_case=None, category_repository=None, account_repository=None, daily_balance_repository=None):
        self.transaction_repository = transaction_repository or TransactionRepository()
        self.transaction_factory = transaction_factory or TransactionFactory()
        self.update_daily_balance_use_case = update_daily_balance_use_case or UpdateDailyBalanceUseCase()
        self.category_repository = category_repository or CategoryRepository()
        self.account_repository = account_repository or AccountRepository()
        self.daily_balance_repository = daily_balance_repository or DailyBalanceRepository()

    def execute(self, form) -> TransactionDomain:
        category_domain = self.category_repository.get_by_id(form['category_id'])
        account_domain = self.account_repository.get_by_id(form['account_id'])

        transaction_domain = self.transaction_factory.create_from_data({
            'category': category_domain,
            'account': account_domain,
            'value': form['value'],
            'description': form['description'],
            'transaction_date': form['transaction_date'],
            'transaction_type': form['transaction_type'],
            'status': form['status'],
            'ignore': form['ignore'],
            'observation': form['observation'],
        })

        self.transaction_repository.create(transaction_domain)

        if not transaction_domain.ignore:
            daily_balance_domain = self.daily_balance_repository.get_by_reference_date(form['transaction_date'])

            self.update_daily_balance_use_case.execute(daily_balance_domain, transaction_domain)
            self.transaction_repository.update_daily_balance(transaction_domain, daily_balance_domain)

        return transaction_domain
