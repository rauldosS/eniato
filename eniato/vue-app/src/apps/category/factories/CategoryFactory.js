import { Account } from '../domain/Category'

export class CategoryFactory {
  buildFromDTO (dto) {
    return new Account({
      id: dto.id,
      name: dto.name,
      color: dto.color,
      icon: dto.icon
    })
  }
}
