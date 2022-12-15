from django.http import HttpResponseRedirect
from django.urls import reverse
from apps.core.services.user_permission_service import UserPermissionService
from apps.nps.services.nps_permission_service import NPSPermissionService


class UserPermissionMixin(object):
    allowed_groups = set([])
    user_permission_service = UserPermissionService()
    nps_permission_service = NPSPermissionService()

    def dispatch(self, request, *args, **kwargs):
        if self.user_permission_service.request_has_permission(request, self.allowed_groups):
            return super(UserPermissionMixin, self).dispatch(request, *args, **kwargs)
        elif self.nps_permission_service.request_has_permission(request):
            return HttpResponseRedirect(reverse('nps:form'))
        return HttpResponseRedirect(reverse('core:not_authorized'))
