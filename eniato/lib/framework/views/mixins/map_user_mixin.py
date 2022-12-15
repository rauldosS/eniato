from apps.core.users.mappers.user_mapper import UserMapper


class MapUserMixin(object):
    user = None

    def __init__(self, *args, **kwargs):
        super(MapUserMixin, self).__init__(*args, **kwargs)
        self.load_user_mapper()

    def map_user(self, framework_user):
        self.user = self.user_mapper.map(framework_user)

    def load_user_mapper(self):
        self.user_mapper = UserMapper()
