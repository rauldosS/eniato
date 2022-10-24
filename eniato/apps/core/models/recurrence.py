from django.db import models
from lib.framework.models.base_model import BaseModel

from apps.core.models.transaction import Transaction

from apps.core.constants import TransactionType



class Recurrence(BaseModel):
    recurrence_type = ''

    class Meta:
        verbose_name = 'Recorrência'

"""
    recurrence_type
        every_day                   todos os dias
        weekly                      semanal
        monthly                     mensal
        Yearly                      anual
        every_day_week              todos os dias da semana
        custom                      personalizado
        
    Transação
        Recorrente
            - Vezes
            - Tipo
                Diária
                Semanal
                Mensal
                Anual
                    Default
                        - Mensal


"""

""""
    
        

    Setembro -> Mês inicial
        Recorrência
            Transação       Receita     Salário
            Transação       Despesa     Aluguel         R$  1.000,00
            Transação       Despesa     Alimentação     R$    800,00
        Não recorrente
        -> Receita: 2.000,00
        -> Despesas: 1800,00
        -> Balanço: 200,00
    Outubro
    Novembro
    Dezembro
"""

"""
    Se uma transação com recorrência for alterada
        - Apenas a mesma
        - A mesma e as seguintes
        - Todas as transações
"""

