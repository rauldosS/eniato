from typing import Optional

from lib.users.domain import User

from apps.category.constants import CATEGORY_TYPE_DISPLAY_NAME


class Category:
    """
    """

    def __init__(self, attributes={}):
        self.id: Optional[int] = attributes.get('id')
        self.user: User = attributes['user']
        self.category_type: str = attributes['category_type']
        self.name: str = attributes['name']
        self.color: str = attributes['color']
        self.icon: str = attributes['icon']
        self.default: bool = attributes['default']

    def set_id(self, id):
        self.id = id

    @property
    def display_category_type(self):
        return dict(CATEGORY_TYPE_DISPLAY_NAME)[self.category_type]

    @property
    def display_default(self):
        return 'Sim' if self.default else 'Não'
