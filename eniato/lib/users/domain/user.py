class User:

    def __init__(self, username, email, first_name, last_name, id=None, groups=None):
        self.username = username
        self.email = email
        self.first_name = first_name
        self.last_name = last_name
        self.groups = list(groups) if groups else []
        self.id = id

    def full_name(self):
        if not self.first_name:
            return self.last_name

        if not self.last_name:
            return self.first_name

        return '{} {}'.format(self.first_name, self.last_name).strip()

    def set_id(self, id):
        self.id = id

    def has_permissions(self, obj):
        return obj.allows(self)
