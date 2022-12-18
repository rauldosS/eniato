from apps.core.models import APIUser
from apps.core.users.domain.application import Application as ApplicationDomain
from apps.core.users.mappers.user_mapper import UserMapper
from oauth2_provider.models import Application


class UserRepository(object):
    model = APIUser

    def __init__(self, user_mapper=None):
        self.user_mapper = user_mapper or UserMapper()

    def get_by_id(self, id):
        return self.model.stored.get(id=id)

    def get_by_company_group(self, company_group_id, username):
        try:
            return self.model.stored.get(company_group_id=company_group_id, username=username)
        except self.model.DoesNotExist:
            return None

    def get_by_brnet_group_id_and_user_name(self, brnet_group_id, username):
        try:
            api_user = self.model.stored.get(company_group_id=brnet_group_id, username=username)
            return self.user_mapper.map(api_user, map_application=True)
        except self.model.DoesNotExist:
            return None

    def save(self, user_domain):
        api_user_model, created = self.model.stored.update_or_create(
            id=user_domain.id,
            defaults=dict(
                company_group_id=user_domain.group_id,
                username=user_domain.username
            )
        )

        api_user_model.set_password(user_domain.password)
        api_user_model.save()
        user_domain.set_id(api_user_model.id)
        self._save_application(user_domain, api_user_model)
        return user_domain, created

    def _save_application(self, user_domain, api_user):
        application = api_user.get_application()
        if not application:
            if not user_domain.application:
                application_domain = ApplicationDomain.build(user_domain.id, user_domain.username)
                user_domain.set_application(application_domain)

            application = Application()
            application.user_id = user_domain.application.user_id
            application.name = user_domain.application.name
            application.client_type = user_domain.application.client_type
            application.authorization_grant_type = user_domain.application.authorization_grant_type
            application.save()
            user_domain.application.set_id(application.id)
            user_domain.application.set_created(application.created)
            user_domain.application.set_updated(application.updated)
            user_domain.application.set_client_id(application.client_id)
            user_domain.application.set_client_secret(application.client_secret)
