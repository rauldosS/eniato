import { FinancialInstitution } from '../domain/FinancialInstitution'

export class FinancialInstitutionFactory {
  buildFromDTO (dto) {
    return new FinancialInstitution({
      id: dto.id,
      name: dto.name,
      code: dto.code,
      logo: dto.logo
    })
  }
}
