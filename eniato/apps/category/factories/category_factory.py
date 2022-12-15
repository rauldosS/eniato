from lib.users.factories import UserFactory

from apps.category.domain import Category


class CategoryFactory:

    def __init__(self, user_factory=None):
        self.user_factory = user_factory or UserFactory()

    def create_from_data(self, data):
        attributes = {}

        attributes['id'] = data.get('id')
        attributes['user'] = data['user']
        attributes['category_type'] = data['category_type']
        attributes['name'] = data['name']
        attributes['color'] = data['color']
        attributes['icon'] = data['icon']
        attributes['default'] = data['default']

        return Category(attributes)

    def create_from_model(self, model):
        return Category({
            'id': model.id,
            'user': self.user_factory.create_from_user_model(model.user),
            'category_type': model.category_type,
            'name': model.name,
            'color': model.color,
            'icon': model.icon,
            'default': model.default,
        })
