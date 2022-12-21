import { Account } from '../domain/Account'

export class AccountFactory {
  buildFromDTO (dto) {
    return new Account({
      id: dto.id,
      user: dto.user,
      financialInstitution: dto.financialInstitution,
      openingBalance: dto.openingBalance,
      currentBalance: dto.currentBalance,
      description: dto.description,
      accountType: dto.accountType,
      displayAccountType: dto.displayAccountType,
      color: dto.color,
      default: dto.default,
      active: dto.active
    })
  }
}
