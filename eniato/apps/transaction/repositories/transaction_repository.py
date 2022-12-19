from lib.framework.models.base_repository import BaseRepository

from apps.transaction.factories import TransactionFactory
from apps.transaction.models.transaction import Transaction
from apps.transaction.domain import Transaction as TransactionDomain


class TransactionRepository(BaseRepository):

    def __init__(self, model=None, domain_object=None, factory=None):
        self.model = model or Transaction
        self.domain_object = domain_object or TransactionDomain
        self.factory = factory or TransactionFactory()

    def update_daily_balance(self, domain, daily_balance):
        self.model.stored.filter(id=domain.id).update(daily_balance_id=daily_balance.id)

    def get_by_account(self, account_id):
        transactions = self.model.stored.filter(account=account_id).order_by('-transaction_date')
        return [
            self.factory.create_from_model(transaction)
            for transaction in transactions
        ]

    def get_by_query_params(self, user, query_params):
        queryset = self.model.stored.filter(
            reference_date__range=[query_params['initial_date'], query_params['final_date']],
            user=user
        ).prefetch_related(
            'transaction_set'
        )

        print('repository', queryset)

        return [
            self.factory.create_from_model(daily_balance, map_transactions=True)
            for daily_balance in queryset
        ]

    def create(self, domain):
        model = self.model.stored.create(
            category_id=domain.category.id,
            account_id=domain.account.id,
            # credit_card
            # store
            # tag
            # recurrence
            installment=domain.installment,
            value=domain.value,
            description=domain.description,
            transaction_date=domain.transaction_date,
            transaction_type=domain.transaction_type,
            status=domain.status,
            ignore=domain.ignore,
            # file
            observation=domain.observation,
        )

        return self.factory.create_from_model(model)
