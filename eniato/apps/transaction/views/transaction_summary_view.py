from django.views.generic import TemplateView


class TransactionSummaryView(TemplateView):
    template_name = 'transaction/transaction-summary.html'

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        return context
