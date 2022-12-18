from ..domain.user import User
from ..domain.application import Application


class UserMapper(object):

    def map(self, framework_user, map_application=False):
        user = User(
            framework_user.id,
            framework_user.username,
            framework_user.email,
            framework_user.company_group_id
        )
        if map_application:
            user.set_application(self._get_appliction(framework_user))

        return user

    def _get_appliction(self, framework_user):
        application_model = framework_user.get_application()
        if application_model:
            application_data = {
                'id': application_model.id,
                'user_id': application_model.user_id,
                'client_type': application_model.client_type,
                'authorization_grant_type': application_model.authorization_grant_type,
                'client_id': application_model.client_id,
                'client_secret': application_model.client_secret,
                'name': application_model.name,
                'created': application_model.created,
                'updated': application_model.updated,

            }
            application = Application(application_data)
            return application
        return None
