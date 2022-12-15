from lib.framework.models.base_repository import BaseRepository

from apps.category.factories import CategoryFactory
from apps.category.models.category import Category
from apps.category.domain import Category as CategoryDomain

from django.db.models import Q


class CategoryRepository(BaseRepository):

    def __init__(self, model=None, domain_object=None, factory=None):
        self.model = model or Category
        self.domain_object = domain_object or CategoryDomain
        self.factory = factory or CategoryFactory()

    def get_by_user(self, user):
        categories = self.model.objects.filter(Q(user=user) | Q(default=True)).order_by('name', 'default')
        return [
            self.factory.create_from_model(category)
            for category in categories
        ]

    def get_by_transaction_type(self, category_type):
        return self.model.objects.filter(category_type=category_type).order_by('name', 'default')

    """
    def get_by_type(self, category_type):
        return self.model.objects.filter(
            Q(category_type=category_type),
            Q(
                user=user
            ) | Q(
                default=True
            )
        ).order_by('name', 'default')
    """
