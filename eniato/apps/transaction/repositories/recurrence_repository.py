from lib.framework.models.base_repository import BaseRepository

from apps.transaction.factories import RecurrenceFactory
from apps.transaction.models.recurrence import Recurrence
from apps.transaction.domain import Recurrence as RecurrenceDomain


class RecurrenceRepository(BaseRepository):

    def __init__(self, model=None, domain_object=None, factory=None):
        self.model = model or Recurrence
        self.domain_object = domain_object or RecurrenceDomain
        self.factory = factory or RecurrenceFactory()

    def create(self, domain):
        model = self.model.stored.create(
            fixed=domain.fixed,
            repeat_amount=domain.repeat_amount,
            repeat_period=domain.repeat_period
        )

        domain.set_id(model.id)

        return domain
