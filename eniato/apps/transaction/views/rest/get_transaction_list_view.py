from rest_framework.generics import ListAPIView
from rest_framework.response import Response

from apps.transaction.repositories import DailyBalanceRepository
from apps.transaction.serializers import DailyBalanceSerializer


class GetTransactionListView(ListAPIView):
    repository = DailyBalanceRepository()
    serializer_class = DailyBalanceSerializer

    def get_queryset(self):
        query_params = self._get_query_params()

        """
            status: todos, efetuados, pendentes, ignorados
            categoria
            conta
            tag
            data
                dia
                mês/ano
                período
        """

        qs = self.repository.get_by_query_params(
            self.request.user,
            query_params
        )

        print('qs', qs)

        # data = self.get_serializer(transctions).data
        # daily_transaction = self.factory.create_from_query_params(request.user, query_params)

        # print('daily_transaction', daily_transaction)

        # print('data', data)

        return qs

    def _get_query_params(self):
        query_params = {}

        query_params['query'] = self.request.query_params.get('query')
        query_params['initial_date'] = self.request.query_params.get('initialDate')
        query_params['final_date'] = self.request.query_params.get('finalDate')

        return query_params
