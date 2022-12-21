from enum import Enum


class Status(Enum):
    STOPPED = 'stopped'
    ACTIVE = 'active'
    CONCLUDED = 'concluded'

STATUS_DISPLAY_NAME = (
    (Status.STOPPED.value, 'Parado'),
    (Status.ACTIVE.value, 'Ativo'),
    (Status.CONCLUDED.value, 'Concluído')
)
