from rest_framework.generics import ListAPIView

from apps.accounts.repositories import FinancialInstitutionRepository
from apps.accounts.serializers import FinancialInstitutionSerializer

class GetAllFinancialInstitutionsView(ListAPIView):
    repository = FinancialInstitutionRepository()
    serializer_class = FinancialInstitutionSerializer

    def get_queryset(self):
        return self.repository.get_all()
