from apps.objective.domain import Objective as ObjectiveDomain

from apps.objective.repositories import ObjectiveRepository
from apps.objective.factories import ObjectiveFactory
from lib.users.repositories import UserRepository


class SaveObjectiveUseCase(object):

    def __init__(self, repository=None, factory=None, user_repository=None):
        self.repository = repository or ObjectiveRepository()
        self.factory = factory or ObjectiveFactory()
        self.user_repository = user_repository or UserRepository()

    def execute(self, user, form) -> ObjectiveDomain:
        user_domain = self.user_repository.get_by_id(user.id)

        print('form', form)

        objective_domain = self.factory.create_from_data({
            'id': form['id'],
            'user': user_domain,
            'value': form['value'],
            'balance': form['balance'],
            'objective_date': form['objective_date'],
            'name': form['name'],
            'color': form['color'],
            'icon': form['icon'],
            'status': form['status'],
            'description': form['description'],
        })

        self.repository.save(objective_domain)

        return objective_domain
