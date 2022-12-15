from django.db import models
from lib.framework.models.base_model import BaseModel
from django.contrib.auth import get_user_model

User = get_user_model()


class DailyBalance(BaseModel):
    user = models.ForeignKey(User, on_delete=models.PROTECT, verbose_name='Usuário')
    reference_date = models.DateField(verbose_name='Data de referência', blank=False, null=False)

    balance = models.DecimalField(verbose_name='Balanço', max_digits=10, decimal_places=2, default=0)
    income = models.DecimalField(verbose_name='Receitas', max_digits=10, decimal_places=2, default=0)
    expense = models.DecimalField(verbose_name='Despesas', max_digits=10, decimal_places=2, default=0)
    credit = models.DecimalField(verbose_name='Crédito', max_digits=10, decimal_places=2, default=0)

    expected_balance = models.DecimalField(verbose_name='Balanço previsto', max_digits=10, decimal_places=2, default=0)
    expected_income = models.DecimalField(verbose_name='Receitas Previstas', max_digits=10, decimal_places=2, default=0)
    expected_expense = models.DecimalField(verbose_name='Despesas Previstas', max_digits=10, decimal_places=2, default=0)
    expected_credit = models.DecimalField(verbose_name='Crédito Previsto', max_digits=10, decimal_places=2, default=0) 

    """
        Consulta por período

        - Limite de range de consulta
        - Tipo de consulta: monthly/range/daily
            Irá definir o tipo de exibição dos dados

        novembro = DailyBalance("2022-11-01", balance=100, income=200, expense=100, expected_balance=0, expected_income=0, expected_expense=0)
        dezembro = DailyBalance("2022-12-01", balance=200, income=200, expense=100, expected_balance=0, expected_income=0, expected_expense=0)
        janeiro = DailyBalance("2023-01-01", balance=300, income=200, expense=100, expected_balance=0, expected_income=0, expected_expense=0)

        daily_balance_sheets = get_daily_balance(start_day='2022-12-01', last_day='2023-01-01')
        previous_balance = get_previous_daily_balance(reference_date)
            balance: transações pagas
            expected_balance: balance + transações não pagas

        Tipo de consulta "Mensal":

            - Balanço Mensal = soma de todas as transações do período

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

        Tipo de consulta "Período":
            - Balanço período = soma de todas as transações do período

            - Final do período = Soma de todas as transações pagas do período
            - Saldo previsto do dia = balanço previsto do dia anterior + soma de todas as transações do dia

        daily_balance in daily_balance_sheets:
            balance

    """

    """
        Registro de transação

        Ao atualizar ou registrar uma despesa

        Balanço do dia:
            recalcular balanço (balance/expected_balance)

        balance = balance (reference_date)
        expected_balance = expected_balance (reference_date)

        Balanços futuros:
            balance += balance
            expected_balance += expected_balance

            balance = balance
            expected_balance = expected_balance
    """
