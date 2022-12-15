export class Account {
  constructor (attributes) {
    this._id = attributes.id
    this._name = attributes.name
    this._color = attributes.color
    this._icon = attributes.icon
  }

  get id () { return this._id }
  get name () { return this._name }
  get color () { return this._color }
  get icon () { return this._icon }

  toDTO () {
    return {
      id: this._id,
      name: this._name,
      color: this._color,
      icon: this._icon
    }
  }
}
