import random
import string

from apps.core.users.domain.application import Application


class User(object):
    def __init__(self, id, username, email, group_id):
        self.id = id
        self.username = username
        self.email = email
        self.group_id = int(group_id) if group_id else None
        self.password = None
        self.application = None

    @classmethod
    def build(cls, id, username, email, group_id):
        return cls(id, username, email, group_id)

    @classmethod
    def build_new(cls, group_id, username):
        instance = cls(None, username, None, group_id)
        instance.set_new_password()
        instance.set_application(Application.build(instance.id, username))
        return instance

    def set_new_password(self):
        self.password = "".join(random.choice(string.ascii_uppercase + string.digits + string.ascii_lowercase) for _ in range(32))

    def set_application(self, application):
        self.application = application

    def set_id(self, id):
        self.id = id
        if self.application:
            self.application.set_user_id(id)

    def __eq__(self, user):
        if isinstance(user, User):
            return self.id == user.id
        else:
            raise TypeError("{} is not a {} instance.".format(user, User))
