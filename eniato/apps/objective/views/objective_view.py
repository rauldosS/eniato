from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin


class ObjectiveView(TemplateView, LoginRequiredMixin):
    template_name = 'objective/objective.html'
