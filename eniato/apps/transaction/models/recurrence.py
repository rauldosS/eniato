from django.db import models
from lib.framework.models.base_model import BaseModel
from django.core.validators import MaxValueValidator, MinValueValidator

from apps.transaction.constants import RepeatPeriod


class Recurrence(BaseModel):
    fixed = models.BooleanField(verbose_name='Fixa', default=False)
    repeat_amount = models.IntegerField(
        verbose_name='Vezes',
        default=2,
        validators=[
            MaxValueValidator(100, message='Deve ser um valor menor que 100'),
        ]
    )
    repeat_period = models.CharField(
        choices=[(repeat_period.value, repeat_period.name) for repeat_period in RepeatPeriod],
        default='monthly',
        max_length=50,
        verbose_name='Período'
    )
