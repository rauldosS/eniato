from django.views.generic import TemplateView

from django.shortcuts import render


class TransactionView(TemplateView):
    template_name = 'transaction/transaction.html'

    # def get(self, request):
    #     data = {}
    #     return render(request, self.template_name, context=data)
