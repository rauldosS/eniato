import Axios from 'axios'
import { ENDPOINTS_CONSTANTS as URLS } from '../constants'

export default class TransactionSummaryRepository {
  constructor (requester = null, baseUri = null) {
    this.requester = requester || Axios
    this.baseUri = baseUri || URLS.BASE_TRANSACTION_REST_URL
  }

  async getTransactionSummary (
    initialDate,
    finalDate,
    status,
    categoryId,
    accountId,
    query
  ) {
    const params = {}

    params.initial_date = typeof initialDate === 'string' ? initialDate : initialDate.toISOString().slice(0, 10)
    params.final_date = typeof finalDate === 'string' ? finalDate : finalDate.toISOString().slice(0, 10)

    if (query) {
      params.query = query
    }

    if (status) {
      params.status = status
    }

    if (categoryId) {
      params.category_id = categoryId
    }

    if (accountId) {
      params.account_id = accountId
    }

    const uri = `${this.baseUri}/${URLS.GET_TRANSACTION_LIST_FOR_AUTHENTICATED_USER_URL}`
    return this.requester.get(uri, { params }).then(({ data: dto }) => {
      return dto
    })
  }
}
