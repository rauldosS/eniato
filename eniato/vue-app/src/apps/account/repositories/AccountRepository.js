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
}
