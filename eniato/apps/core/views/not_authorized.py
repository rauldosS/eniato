from django.views.generic import TemplateView


class NotAuthorizedView(TemplateView):
    template_name = 'base-error.html'
    status = 403

    def render_to_response(self, context, **kwargs):
        kwargs['status'] = self.status
        context['status_code'] = self.status
        context['message'] = 'Acesso negado.'
        return super(TemplateView, self).render_to_response(context, **kwargs)
