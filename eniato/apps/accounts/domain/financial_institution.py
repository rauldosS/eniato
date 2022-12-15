class FinancialInstitution:
    def __init__(self, attributes=None):
        attributes = attributes or {}
        self.id: int = attributes.get('id')
        self.code: int = attributes['code']
        self.name: str = attributes['name']
        self.logo: str = attributes['logo']
