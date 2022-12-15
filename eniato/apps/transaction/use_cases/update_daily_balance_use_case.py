from apps.transaction.repositories import DailyBalanceRepository
from apps.transaction.factories import DailyBalanceFactory

from apps.accounts.repositories import AccountRepository

from datetime import datetime, date


class UpdateDailyBalanceUseCase:

    def __init__(self, repository=None, factory=None, account_repository=None):
        self.repository = repository or DailyBalanceRepository()
        self.factory = factory or DailyBalanceFactory()
        self.account_repository = account_repository or AccountRepository() 

    def execute(self, domain, transaction):
        reference_date = datetime.strptime(domain.reference_date, '%Y-%m-%d').date() if isinstance(domain.reference_date, str) else domain.reference_date

        domain.update_balance(transaction)
        self.repository.save(domain)

        # update current account/credit card balance
        if reference_date <= date.today() and transaction.status:
            if transaction.account:
                account = self.account_repository.get_by_id(transaction.account.id)

                current_balance = account.current_balance + transaction.value_for_transaction_type
                self.account_repository.update_current_balance(account, current_balance)

        # update next daily if repeat
        # pegar até última transação criada e realizar atualização/criação
        # if transaction.repeat:

        # only update the balance for the next few daily
        next_daily_balance = self.repository.get_next_daily_balance(reference_date)

        for domain in next_daily_balance:
            domain.update_only_balance(transaction)
            self.repository.save(domain)
