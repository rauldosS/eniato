from django.views.generic import TemplateView
from django.shortcuts import render
from django.shortcuts import redirect


from django.contrib.auth.decorators import login_required


class IndexView(TemplateView):
    template_name = 'core/index.html'

    def get(self, request, *args, **kwargs):
        print('get')
        return super().get(request, *args, **kwargs)


class Http404View(TemplateView):
    template_name = 'base-error.html'
    status = 404

    def render_to_response(self, context, **kwargs):
        kwargs['status'] = self.status
        context['status_code'] = self.status
        context['message'] = 'Página não encontrada.'
        return super(TemplateView, self).render_to_response(context, **kwargs)


def error_500(request):
    data = {
        'status_code': '500',
        'message': 'Erro inesperado.',
        'text_error': 'Nossa equipe de desenvolvedores já foi notificada e trabalhará nele o mais rápido possível.'
    }
    return render(request, 'base-error.html', context=data, status=500)
