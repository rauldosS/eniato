from lib.framework.models.base_repository import BaseRepository

from apps.transaction.factories import TransactionFactory
from apps.transaction.models.transaction import Transaction
from apps.transaction.domain import Transaction as TransactionDomain

from apps.transaction.constants import TransactionType

from django.db.models import Sum, Case, When, DecimalField
import decimal


class TransactionRepository(BaseRepository):

    def __init__(self, model=None, domain_object=None, factory=None):
        self.model = model or Transaction
        self.domain_object = domain_object or TransactionDomain
        self.factory = factory or TransactionFactory()

    def get_by_account(self, account_id):
        transactions = self.model.stored.filter(account=account_id).order_by('-transaction_date')
        return [
            self.factory.create_from_model(transaction)
            for transaction in transactions
        ]

    def get_list_by_query_params(self, user, reference_date):
        transactions = self.model.stored.filter(
            user=user,
            transaction_date=reference_date,
            account__active=True
        ).order_by('id')
        return [
            self.factory.create_from_model(transaction)
            for transaction in transactions
        ]

    def get_balance_by_params(self, user, final_date, query_params):
        totals = self.model.stored.filter(
            user=user,
            transaction_date__lte=final_date,
            account__active=True
        ).aggregate(
            balance=Sum(Case(
                When(transaction_type=TransactionType.INCOME.value, status=True, then='value'),
                output_field=DecimalField()
            ), default=decimal.Decimal(0)) - Sum(Case(
                When(transaction_type=TransactionType.EXPENSE.value, status=True, then='value'),
                output_field=DecimalField()
            ), default=decimal.Decimal(0)),
            expected_balance=Sum(Case(
                When(transaction_type=TransactionType.INCOME.value, status=False, then='value'),
                output_field=DecimalField()
            ), default=decimal.Decimal(0)) - Sum(Case(
                When(transaction_type=TransactionType.EXPENSE.value, status=False, then='value'),
                output_field=DecimalField()
            ), default=decimal.Decimal(0))
        )

        return {
            'balance': totals['balance'],
            'expected_balance': totals['expected_balance'] + totals['balance']
        }

    def get_totals(self, user, query_params):
        qs = self.model.stored.filter(
            user=user,
            transaction_date__range=[query_params['initial_date'], query_params['final_date']],
            account__active=True
        )

        print('query_params', query_params)

        if query_params.get('query'):
            pass

        if query_params.get('status'):
            qs = qs.filter(status=int(query_params['status']))

        if query_params.get('category_id'):
            qs = qs.filter(category_id=int(query_params['category_id']))

        totals_by_period = self.get_totals_by_period(qs)
        totals_grouped_by_day = self.get_totals_grouped_by_day(qs)

        return totals_by_period, totals_grouped_by_day

    def get_totals_by_period(self, qs):
        totals = qs.aggregate(
            total_income=Sum(Case(
                When(transaction_type=TransactionType.INCOME.value, status=True, then='value'),
                output_field=DecimalField(),
            ), default=decimal.Decimal(0)),
            total_expense=Sum(Case(
                When(transaction_type=TransactionType.EXPENSE.value, status=True, then='value'),
                output_field=DecimalField()
            ), default=decimal.Decimal(0)),
            total_expected_income=Sum(Case(
                When(transaction_type=TransactionType.INCOME.value, status=False, then='value'),
                output_field=DecimalField()
            ), default=decimal.Decimal(0)),
            total_expected_expense=Sum(Case(
                When(transaction_type=TransactionType.EXPENSE.value, status=False, then='value'),
                output_field=DecimalField()
            ), default=decimal.Decimal(0))
        )

        balance = totals['total_income'] - totals['total_expense']
        expected_balance = totals['total_expected_income'] - totals['total_expected_expense']

        return {
            'total_income': totals['total_income'],
            'total_expense': totals['total_expense'],
            'balance': balance,
            'total_expected_income': totals['total_expected_income'] + totals['total_income'],
            'total_expected_expense': totals['total_expected_expense'] + totals['total_expense'],
            'expected_balance': balance + expected_balance
        }

    def get_totals_grouped_by_day(self, qs):
        return qs.values(
            'transaction_date'
        ).order_by(
            'transaction_date'
        ).annotate(
            total_income=Sum(Case(
                When(transaction_type=TransactionType.INCOME.value, status=True, then='value'),
                output_field=DecimalField()
            ), default=decimal.Decimal(0)),
            total_expense=Sum(Case(
                When(transaction_type=TransactionType.EXPENSE.value, status=True, then='value'),
                output_field=DecimalField()
            ), default=decimal.Decimal(0)),
            balance=Sum(Case(
                When(transaction_type=TransactionType.INCOME.value, status=True, then='value'),
                output_field=DecimalField()
            ), default=decimal.Decimal(0)) - Sum(Case(
                When(transaction_type=TransactionType.EXPENSE.value, status=True, then='value'),
                output_field=DecimalField()
            ), default=decimal.Decimal(0)),
            total_expected_income=Sum(Case(
                When(transaction_type=TransactionType.INCOME.value, status=False, then='value'),
                output_field=DecimalField()
            ), default=decimal.Decimal(0)),
            total_expected_expense=Sum(Case(
                When(transaction_type=TransactionType.EXPENSE.value, status=False, then='value'),
                output_field=DecimalField()
            ), default=decimal.Decimal(0)),
            expected_balance=Sum(Case(
                When(transaction_type=TransactionType.INCOME.value, status=False, then='value'),
                output_field=DecimalField()
            ), default=decimal.Decimal(0)) - Sum(Case(
                When(transaction_type=TransactionType.EXPENSE.value, status=False, then='value'),
                output_field=DecimalField()
            ), default=decimal.Decimal(0)),
        )

    def save(self, domain):
        model, created = self.model.stored.update_or_create(
            id=domain.id,
            defaults=dict(
                user_id=domain.user.id,
                category_id=domain.category.id,
                account_id=domain.account.id,
                recurrence_id=domain.recurrence.id if domain.recurrence else None,
                value=domain.value,
                description=domain.description,
                transaction_date=domain.transaction_date,
                transaction_type=domain.transaction_type,
                status=domain.status,
                observation=domain.observation
            )
        )

        if created:
            domain.set_id(model.id)

        return created, domain
