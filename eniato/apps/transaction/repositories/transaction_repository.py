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
        return self.model.stored.filter(id=domain.id).update(daily_balance_id=daily_balance.id)

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
