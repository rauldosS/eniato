from rest_framework.generics import ListAPIView

from apps.accounts.repositories import AccountRepository
from apps.accounts.serializers import AccountSerializer


class GetAllAccountsByUserView(ListAPIView):
    repository = AccountRepository()
    serializer_class = AccountSerializer

    def get_queryset(self):
        return self.repository.get_all_by_user(self.request.user)
