from rest_framework.generics import ListAPIView

from apps.accounts.repositories import AccountRepository
from apps.accounts.serializers import AccountSerializer


class GetAccountListByUserView(ListAPIView):
    repository = AccountRepository()
    serializer_class = AccountSerializer

    def get_queryset(self):
        accounts = self.repository.get_by_user(self.request.user)
        return accounts
