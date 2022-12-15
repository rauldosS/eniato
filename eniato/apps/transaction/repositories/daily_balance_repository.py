from lib.framework.models.base_repository import BaseRepository

from apps.transaction.factories.daily_balance_factory import DailyBalanceFactory
from apps.transaction.models.daily_balance import DailyBalance
from apps.transaction.domain import DailyBalance as DailyBalanceDomain


class DailyBalanceRepository(BaseRepository):

    def __init__(self, model=None, domain_object=None, factory=None):
        self.model = model or DailyBalance
        self.domain_object = domain_object or DailyBalanceDomain
        self.factory = factory or DailyBalanceFactory()

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

    def get_by_reference_date(self, reference_date):
        try:
            return self.factory.create_from_model(
                self.model.stored.get(reference_date=reference_date)
            )
        except self.model.DoesNotExist:
            previous_daily_balance = self.get_previous_daily_balance(reference_date)

            return self.save(
                self.factory.create_from_previous_daily_balance(reference_date, previous_daily_balance)
            )

    def get_previous_daily_balance(self, reference_date):
        try:
            previous_daily_balance = self.model.stored.filter(reference_date__lt=reference_date).latest('reference_date')
            return self.factory.create_from_previous_daily_balance(reference_date, previous_daily_balance)
        except self.model.DoesNotExist:
            return self.factory.create_from_data({ 'reference_date': reference_date })

    def get_next_daily_balance(self, reference_date):
        months_balance = self.model.stored.filter(reference_date__gt=reference_date)
        return [
            self.factory.create_from_model(daily_balance)
            for daily_balance in months_balance
        ]

    def save(self, domain):
        model, created = self.model.stored.update_or_create(
            reference_date=domain.reference_date,
            defaults=dict(
                balance=domain.balance,
                income=domain.income,
                expense=domain.expense,
                credit=domain.credit,
                expected_balance=domain.expected_balance,
                expected_income=domain.expected_income,
                expected_expense=domain.expected_expense,
                expected_credit=domain.expected_credit
            )
        )

        domain.set_id(model.id)

        return domain
