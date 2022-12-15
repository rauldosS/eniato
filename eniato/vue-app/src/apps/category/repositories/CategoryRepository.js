import Axios from 'axios'
import { CategoryFactory } from '../factories/CategoryFactory'
import { ENDPOINTS_CONSTANTS as URLS } from '../constants'

export default class CategoryRepository {
  constructor (requester = null, baseUri = null, factory = null) {
    this.requester = requester || Axios
    this.baseUri = baseUri || URLS.BASE_REST_URL
    this.factory = factory || new CategoryFactory()
  }

  async getCategoriesByTransactionType (transactionType) {
    const uri = `${this.baseUri}/${URLS.GET_CATEGORY_LIST_BY_TRANSACTION_TYPE_URL[transactionType]}`
    return this.requester.get(uri).then(({ data: dtoList }) => {
      return dtoList.map(dto => this.factory.buildFromDTO(dto))
    })
  }
}
