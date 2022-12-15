from django.db import models
from lib.framework.models.base_model import BaseModel
from django.core.validators import MaxValueValidator, MinValueValidator

from apps.transaction.constants import RepeatPeriod


class Recurrence(BaseModel):
    fixed = models.BooleanField(verbose_name='Fixa', default=False)
    repeat = models.BooleanField(verbose_name='Repetir', default=False)
    repeat_amount = models.IntegerField(
        verbose_name='Vezes',
        default=2,
        validators=[
            MaxValueValidator(100, message='Deve ser um valor menor que 100'),
            MinValueValidator(2, message='Deve ser um valor maior que 2')
        ]
    )
    repeat_period = models.CharField(
        choices=[(repeat_period.value, repeat_period.name) for repeat_period in RepeatPeriod],
        max_length=50,
        verbose_name='Período'
    )
    amout = models.DecimalField(verbose_name='Valor Total', max_digits=10, decimal_places=2, default=0.00)
