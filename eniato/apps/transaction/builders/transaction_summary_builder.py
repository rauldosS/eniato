from apps.transaction.repositories.transaction_repository import TransactionRepository
from apps.transaction.factories import DailyBalanceFactory

from apps.transaction.domain import TransactionSummary

from datetime import datetime, date

import calendar


class TransactionSummaryBuilder:

    def __init__(self, transaction_repository=None, daily_balance_factory=None):
        self.transaction_repository = transaction_repository or TransactionRepository()
        self.daily_balance_factory = daily_balance_factory or DailyBalanceFactory()

    def build(self, user, query_params):
        self.query_params = query_params
        period = self._get_period()

        totals_by_period, totals_grouped_by_day = self.transaction_repository.get_totals(user, query_params)

        data = {}

        data['period'] = period
        data['daily_balances'] = [
            self.daily_balance_factory.create_from_data({
                'reference_date': day['transaction_date'],
                'balance': day['balance'],
                'income': day['total_income'],
                'expense': day['total_expense'],
                'expected_balance': day['expected_balance'],
                'expected_income': day['total_expected_income'],
                'expected_expense': day['total_expected_expense'],
                'transactions': self.transaction_repository.get_list_by_query_params(user, day['transaction_date'])
            })
            for day in totals_grouped_by_day
        ]

        period_balance = self._get_period_balance(user, period)

        data['period'] = period
        data['period_balance'] = period_balance['balance']
        data['expected_period_balance'] = period_balance['expected_balance']
        data['total_income'] = totals_by_period['total_income']
        data['total_expense'] = totals_by_period['total_expense']
        data['balance'] = totals_by_period['balance']
        data['total_expected_income'] = totals_by_period['total_expected_income']
        data['total_expected_expense'] = totals_by_period['total_expected_expense']
        data['expected_balance'] = totals_by_period['expected_balance']

        return TransactionSummary(data)

    def _get_period(self):
        first_day_month = date.today().replace(day=1)
        last_day_month = date.today().replace(day=calendar.monthrange(2022, 12)[1])

        initial_date = datetime.strptime(self.query_params.get('initial_date'), '%Y-%m-%d').date()
        final_date = datetime.strptime(self.query_params.get('final_date'), '%Y-%m-%d').date()

        if initial_date >= first_day_month and final_date <= last_day_month:
            return 'current'

    def _get_period_balance(self, user, period):
        if period == 'current':
            final_date = datetime.today().strftime('%Y-%m-%d')
            return self.transaction_repository.get_balance_by_params(user, final_date, self.query_params)
        
        return self.transaction_repository.get_balance_by_params(user, self.query_params.get('final_date'), self.query_params)
