export class Account {
  constructor (attributes) {
    this._id = attributes.id
    this._user = attributes.user
    this._financialInstitution = attributes.financialInstitution
    this._openingBalance = attributes.openingBalance
    this._currentBalance = attributes.currentBalance
    this._description = attributes.description
    this._accountType = attributes.accountType
    this._displayAccountType = attributes.displayAccountType
    this._color = attributes.color
    this._default = attributes.default
    this._active = attributes.active
  }

  get id () { return this._id }
  get user () { return this._user }
  get financialInstitution () { return this._financialInstitution }
  get openingBalance () { return this._openingBalance }
  get currentBalance () { return this._currentBalance }
  get description () { return this._description }
  get accountType () { return this._accountType }
  get displayAccountType () { return this._displayAccountType }
  get color () { return this._color }
  get default () { return this._default }
  get active () { return this._active }

  toDTO () {
    return {
      id: this._id,
      user: this._user,
      financialInstitution: this._financialInstitution,
      openingBalance: this._openingBalance,
      currentBalance: this._currentBalance,
      description: this._description,
      accountType: this._accountType,
      displayAccountType: this._displayAccountType,
      color: this._color,
      default: this._default,
      active: this._active
    }
  }
}
