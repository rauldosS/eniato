from lib.users.factories import UserFactory

from apps.objective.domain import Objective
from apps.objective.constants import Status


class ObjectiveFactory:

    def __init__(self, user_factory=None):
        self.user_factory = user_factory or UserFactory()

    def create_from_data(self, data):
        attributes = {}

        print('data', data)

        attributes['id'] = data.get('id')
        attributes['user'] = data['user']
        attributes['value'] = data['value']
        attributes['balance'] = data.get('balance')
        attributes['objective_date'] = data['objective_date']
        attributes['name'] = data['name']
        attributes['color'] = data['color']
        attributes['icon'] = data['icon']
        attributes['status'] = Status.ACTIVE.value if data['status'] == True else data['status']
        attributes['description'] = data['description']

        return Objective(attributes)

    def create_from_model(self, model):
        return Objective({
            'id': model.id,
            'user': self.user_factory.create_from_user_model(model.user),
            'value': model.value,
            'balance': model.balance,
            'objective_date': model.objective_date,
            'name': model.name,
            'color': model.color,
            'icon': model.icon,
            'status': model.status,
            'description': model.description
        })
