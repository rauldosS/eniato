import Axios from 'axios'
import { FinancialInstitutionFactory } from '../factories/FinancialInstitutionFactory'
import { ENDPOINTS_CONSTANTS as URLS } from '../constants'

export default class accountRepository {
  constructor (requester = null, baseUri = null, factory = null) {
    this.requester = requester || Axios
    this.baseUri = baseUri || URLS.BASE_REST_URL
    this.factory = factory || new FinancialInstitutionFactory()
  }

  async getFinancialInstitutionList () {
    const uri = `${this.baseUri}/${URLS.GET_ALL_FINANCIAL_INSTITUTIONS_URL}`
    return this.requester.get(uri).then(({ data: dtoList }) => {
      return dtoList.map(dto => this.factory.buildFromDTO(dto))
    })
  }
}
