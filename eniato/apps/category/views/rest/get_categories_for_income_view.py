from rest_framework.generics import ListAPIView
from apps.category.repositories import CategoryRepository

from apps.category.serializers import CategorySerializer
from apps.transaction.constants import TransactionType


class GetCatoriesForIncomeView(ListAPIView):
    category_repository = CategoryRepository()
    serializer_class = CategorySerializer

    def get_queryset(self):
        return self.category_repository.get_by_transaction_type(TransactionType.INCOME.value)
