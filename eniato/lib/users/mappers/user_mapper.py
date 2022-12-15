from ..domain.user import User


class UserMapper:

    def map(self, framework_user, map_groups=False):
        fu = framework_user
        groups = []
        if map_groups:
            groups = fu.groups.all() if hasattr(fu.groups, 'all') else fu.groups

        return User(
            fu.username,
            fu.email,
            fu.first_name,
            fu.last_name,
            fu.id,
            groups
        )
