from typing import Optional

from lib.users.domain import User


class Objective:
    """"
    Objective for a specific user

    Attrs:
        - 
    """

    def __init__(self, attributes={}):
        self.id: Optional[int] = attributes.get('id')
        self.user: User = attributes['user']
        self.value: float = attributes['value']
        self.balance: float = attributes.get('balance')
        self.objective_date = attributes['objective_date']
        self.name: str = attributes['name']
        self.color: str = attributes['color']
        self.icon: str = attributes['icon']
        self.status: str = attributes['status']
        self.description: str = attributes.get('description')

    def set_id(self, id):
        self.id = id
