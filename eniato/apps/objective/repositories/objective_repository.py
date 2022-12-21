from lib.framework.models.base_repository import BaseRepository

from apps.objective.factories import ObjectiveFactory
from apps.objective.models.objective import Objective
from apps.objective.domain import Objective as ObjectiveDomain


class ObjectiveRepository(BaseRepository):

    def __init__(self, model=None, domain_object=None, factory=None):
        self.model = model or Objective
        self.domain_object = domain_object or ObjectiveDomain
        self.factory = factory or ObjectiveFactory()

    def get_all_by_user(self, user):
        objectives = self.model.stored.filter(
            user=user
        ).order_by('-name', 'objective_date')
        return [
            self.factory.create_from_model(account)
            for account in objectives
        ]

    def save(self, domain):
        model, created = self.model.stored.update_or_create(
            id=domain.id,
            defaults=dict(
                user_id=domain.user.id,
                value=domain.value,
                balance=domain.balance,
                objective_date=domain.objective_date,
                name=domain.name,
                color=domain.color,
                icon=domain.icon,
                status=domain.status,
                description=domain.description
            )
        )

        if created:
            domain.set_id(model.id)

        return created, domain
