from lib.users.factories import UserFactory

from apps.transaction.domain import Recurrence


class RecurrenceFactory:

    def create_from_data(self, data):
        attributes = {}

        attributes['id'] = data.get('id')

        attributes['fixed'] = data['fixed']
        attributes['repeat_amount'] = data['repeat_amount']
        attributes['repeat_period'] = data['repeat_period']

        return Recurrence(attributes)

    def create_from_model(self, model):
        return Recurrence({
            'id': model.id,
            'fixed': model.fixed,
            'repeat_amount': model.repeat_amount,
            'repeat_period': model.repeat_period
        })
