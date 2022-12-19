from rest_framework.generics import RetrieveAPIView

from apps.transaction.builders import TransactionSummaryBuilder
from apps.transaction.serializers import TransactionSummarySerializer


class GetTransactionListView(RetrieveAPIView):
    builder = TransactionSummaryBuilder()
    serializer_class = TransactionSummarySerializer

    def get_object(self):
        data = self.builder.build(
            self.request.user,
            self.request.query_params
        )

        print('data', data.__dict__)

        return data
