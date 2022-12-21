import Axios from 'axios'
import { AccountFactory } from '../factories/AccountFactory'
import { ENDPOINTS_CONSTANTS as URLS } from '../constants'

export default class accountRepository {
  constructor (requester = null, baseUri = null, factory = null) {
    this.requester = requester || Axios
    this.baseUri = baseUri || URLS.BASE_REST_URL
    this.factory = factory || new AccountFactory()
  }

  async getAccountList () {
    const uri = `${this.baseUri}/${URLS.GET_ACCOUNT_LIST_FOR_AUTHENTICATED_USER_URL}`
    return this.requester.get(uri).then(({ data: dtoList }) => {
      return dtoList.map(dto => this.factory.buildFromDTO(dto))
    })
  }

  async save (data) {
    const uri = `${this.baseUri}/${URLS.SAVE_ACCOUNT_URL}`
    const form = {
      id: data.id,
      financial_institution_id: data.financialInstitution,
      opening_balance: data.openingBalance,
      description: data.description,
      account_type: data.accountType,
      color: data.color,
      default: data.default,
      active: data.active
    }

    return this.requester.post(uri, form).then(({ data: dto }) => {
      return dto
    })
  }

  async deactivate (account) {
    const uri = `${this.baseUri}/${URLS.DEACTIVATE_ACCOUNT_URL}`.replace('<account-id>', account.id)
    return this.requester.post(uri)
  }

  async activate (account) {
    const uri = `${this.baseUri}/${URLS.ACTIVE_ACCOUNT_URL}`.replace('<account-id>', account.id)
    return this.requester.post(uri)
  }

  async delete (account) {
    const uri = `${this.baseUri}/${URLS.DELETE_ACCOUNT_URL}`.replace('<account-id>', account.id)
    return this.requester.post(uri)
  }
}
