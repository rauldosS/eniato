from lib.framework.models.base_repository import BaseRepository

from apps.accounts.factories import FinancialInstitutionFactory
from apps.accounts.models.account import FinancialInstitution
from apps.accounts.domain import FinancialInstitution as FinancialInstitutionDomain


class FinancialInstitutionRepository(BaseRepository):

    def __init__(self, model=None, domain_object=None, factory=None):
        self.model = model or FinancialInstitution
        self.domain_object = domain_object or FinancialInstitutionDomain
        self.factory = factory or FinancialInstitutionFactory()
