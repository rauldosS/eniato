from apps.transaction.domain import Transaction as TransactionDomain

from apps.transaction.repositories.transaction_repository import TransactionRepository
from apps.transaction.repositories.recurrence_repository import RecurrenceRepository
from apps.transaction.factories import TransactionFactory, RecurrenceFactory

from apps.category.repositories import CategoryRepository
from apps.accounts.repositories import AccountRepository

from lib.users.repositories import UserRepository

from datetime import datetime, date
from dateutil.relativedelta import relativedelta


class SaveTransactionUseCase:

    def __init__(
        self,
        transaction_repository=None,
        transaction_factory=None,
        category_repository=None,
        account_repository=None,
        user_repository=None,
        recurrence_repository=None,
        recurrence_factory=None
    ):
        self.transaction_repository = transaction_repository or TransactionRepository()
        self.transaction_factory = transaction_factory or TransactionFactory()
        self.category_repository = category_repository or CategoryRepository()
        self.account_repository = account_repository or AccountRepository()
        self.user_repository = user_repository or UserRepository()
        self.recurrence_repository = recurrence_repository or RecurrenceRepository()
        self.recurrence_factory = recurrence_factory or RecurrenceFactory()

    def execute(self, user, form) -> TransactionDomain:
        category_domain = self.category_repository.get_by_id(form['category_id'])
        account_domain = self.account_repository.get_by_id(form['account_id'])
        user_domain = self.user_repository.get_by_id(user.id)
        recurrence_domain = None
        current_trasaction = None

        if form.get('recurrence'):
            recurrence_domain = self.recurrence_repository.get_by_id(form['recurrence_id'])
        elif form.get('repeat') or form.get('fixed'):
            recurrence_domain = self.recurrence_factory.create_from_data({
                'fixed': form['fixed'],
                'repeat_amount': form['repeat_amount'],
                'repeat_period': form['repeat_period']
            })
            recurrence_domain = self.recurrence_repository.create(recurrence_domain)

        transaction_domain = self.transaction_factory.create_from_data({
            'id': form['id'],
            'user': user_domain,
            'category': category_domain,
            'recurrence': recurrence_domain,
            'account': account_domain,
            'value': form['value'],
            'description': form['description'],
            'transaction_date': form['transaction_date'],
            'transaction_type': form['transaction_type'],
            'installment': form['installment'],
            'status': form['status'],
            'observation': form['observation']
        })

        if form['id']:
            current_trasaction = self.transaction_repository.get_by_id(form['id'])

        created, domain = self.transaction_repository.save(transaction_domain)

        transaction_date = datetime.strptime(domain.transaction_date, '%Y-%m-%d').date()

        if (transaction_date <= self.get_today()):
            if created:
                balance = domain.account.current_balance + domain.value_for_transaction_type
                self.account_repository.update_current_balance(domain.account, balance)
            elif current_trasaction.status != domain.status:
                if domain.status:
                    balance = domain.account.current_balance + domain.value_for_transaction_type
                else:
                    balance = domain.account.current_balance - domain.value_for_transaction_type
                self.account_repository.update_current_balance(domain.account, balance)
        elif domain.status:
            balance = domain.account.current_balance - domain.value_for_transaction_type
            self.account_repository.update_current_balance(domain.account, balance)

        if recurrence_domain:
            domain.transaction_date = transaction_date

            repeat_amount = 600 if recurrence_domain.fixed else recurrence_domain.repeat_amount
            repeat_period = 'monthly' if recurrence_domain.fixed else recurrence_domain.repeat_period
            
            for installment in range(2, repeat_amount):
                date = self.get_next_date(domain.transaction_date, repeat_period)

                domain.id = None
                domain.installment = installment
                domain.transaction_date = date
                domain.status = False

                self.transaction_repository.save(domain)

        return domain

    def get_next_date(self, date, repeat_period):
        if repeat_period == 'everyday':
            return date + relativedelta(days=1)
        if repeat_period == 'weekly':
            return date + relativedelta(weeks=1)
        if repeat_period == 'monthly':
            return date + relativedelta(months=1)
        if repeat_period == 'annually':
            return date + relativedelta(years=1)

    def get_today(self):
        return date.today()
