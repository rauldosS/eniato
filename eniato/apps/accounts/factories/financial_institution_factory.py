from apps.accounts.domain import FinancialInstitution


class FinancialInstitutionFactory:

    def create_from_data(self, data):
        attributes = {}
        return FinancialInstitution(attributes)

    def create_from_model(self, model):
        return FinancialInstitution(
            {
                'id': model.id,
                'code': model.code,
                'name': model.name,
                'logo': model.logo.url,
            }
        )
