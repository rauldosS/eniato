class Application(object):

    def __init__(self, attributes={}):
        self.id = attributes.get('id')
        self.user_id = attributes.get('user_id')
        self.client_type = attributes.get('client_type')
        self.authorization_grant_type = attributes.get('authorization_grant_type')
        self.client_id = attributes.get('client_id')
        self.client_secret = attributes.get('client_secret')
        self.name = attributes.get('name')
        self.created = attributes.get('created')
        self.updated = attributes.get('updated')

    @classmethod
    def build(cls, user_id, username):
        data = {
            'user_id': user_id,
            'name': username,
            'client_type': 'confidential',
            'authorization_grant_type': 'password'
        }
        return cls(data)

    def set_id(self, id):
        self.id = id

    def set_user_id(self, user_id):
        self.user_id = user_id

    def set_created(self, created):
        self.created = created

    def set_updated(self, updated):
        self.updated = updated

    def set_client_secret(self, client_secret):
        self.client_secret = client_secret

    def set_client_id(self, client_id):
        self.client_id = client_id
