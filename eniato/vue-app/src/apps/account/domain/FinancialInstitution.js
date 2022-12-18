export class FinancialInstitution {
  constructor (attributes) {
    this._id = attributes.id
    this._code = attributes.code
    this._name = attributes.name
    this._logo = attributes.logo
  }

  get id () { return this._id }
  get code () { return this._code }
  get name () { return this._name }
  get logo () { return this._logo }

  toDTO () {
    return {
      id: this._id,
      code: this._code,
      name: this._name,
      logo: this._logo
    }
  }
}
