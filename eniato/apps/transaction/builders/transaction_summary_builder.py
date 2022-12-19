from apps.transaction.repositories.transaction_repository import TransactionRepository
from apps.transaction.repositories.daily_balance_repository import DailyBalanceRepository

from apps.transaction.domain import TransactionSummary

from datetime import datetime, date

import calendar


class TransactionSummaryBuilder:

    def __init__(self, transaction_repository=None, daily_balance_repository=None):
        self.transaction_repository = transaction_repository or TransactionRepository()
        self.daily_balance_repository = daily_balance_repository or DailyBalanceRepository()

    def build(self, user, query_params):
        # base no último balanço
        # import ipdb; ipdb.set_trace()

        initial_date = query_params.get('initial_date')
        final_date = query_params.get('final_date')
        query = query_params.get('query')
        period = self._get_period(initial_date, final_date)

        # COM QUERY PRECISO CALCULAR
        # if query:
            # pass
        previus_daily_balance = self.daily_balance_repository.get_previous_daily_balance(user, initial_date)
        previus_final_date_daily_balance = self.daily_balance_repository.get_previous_daily_balance(user, final_date, same_day=True)

        print('previus_daily_balance', previus_final_date_daily_balance.id)
        print('previus_final_date_daily_balance', previus_final_date_daily_balance.id)

        if period == 'current':
            period_balance = previus_daily_balance.balance + 0 # soma das transações até a data atual

        daily_balance_totals = self.daily_balance_repository.get_totals_by_period(user, initial_date, final_date)

        total_income = daily_balance_totals['total_income']
        total_expense = daily_balance_totals['total_expense']
        balance = daily_balance_totals['balance']
        total_expected_income = daily_balance_totals['total_expected_income']
        total_expected_expense = daily_balance_totals['total_expected_expense']
        expected_balance = daily_balance_totals['expected_balance']

        daily_balances = self.daily_balance_repository.get_by_query_params(
            user,
            query_params
        )

        # data = self.get_serializer(transctions).data
        # daily_transaction = self.factory.create_from_query_params(request.user, query_params)

        # print('daily_transaction', daily_transaction)

        # print('data', data)

        """
        previous_month:
            - Final do mês = previous_balance.balance + Soma de todas as transações pagas do período
        current_month:
            - Saldo atual = previous_balance.balance + Soma das transações pagas até o dia atual
        next_month:
            - Saldo previsto = previous_balance.expected_balance + Soma de todas as transações do período

        Saldo do dia:
            >= today:
                - (dia) Saldo previsto do dia = balanço previsto do dia anterior + soma de todas as transações do dia
            < today:
                - (dia) Saldo final do dia = Soma de todas as transações pagas do dia
        """

        data = {}

        data['period'] = period
        data['daily_balances'] = daily_balances
        data['period_balance'] = period_balance
        data['total_income'] = total_income
        data['total_expense'] = total_expense
        data['balance'] = balance
        data['total_expected_income'] = total_expected_income
        data['total_expected_expense'] = total_expected_expense
        data['expected_balance'] = expected_balance

        return TransactionSummary(data)

    def _get_period(self, initial_date, final_date):
        first_day_month = date.today().replace(day=1)
        last_day_month = date.today().replace(day=calendar.monthrange(2022, 12)[1])

        initial_date = datetime.strptime(initial_date, '%Y-%m-%d').date()
        final_date = datetime.strptime(final_date, '%Y-%m-%d').date()

        
        print(first_day_month, last_day_month, initial_date, final_date)

        if initial_date >= first_day_month and final_date <= last_day_month:
            return 'current'
