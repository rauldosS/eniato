import Axios from 'axios'
import { ENDPOINTS_CONSTANTS as URLS } from '../constants'

export default class TransactionRepository {
  constructor (requester = null, baseUri = null) {
    this.requester = requester || Axios
    this.baseUri = baseUri || URLS.BASE_TRANSACTION_REST_URL
  }

  async getTransactionList (
    initialDate,
    finalDate,
    status = null,
    category_id = null,
    account_id = null,
    query = null
  ) {
    const params = {}

    params.initialDate = initialDate.toISOString().slice(0, 10)
    params.finalDate = finalDate.toISOString().slice(0, 10)

    if (query) {
      params.query = query
    }

    const uri = `${this.baseUri}/${URLS.GET_TRANSACTION_LIST_FOR_AUTHENTICATED_USER_URL}`
    return this.requester.get(uri, { params }).then(({ data: dtoList }) => {
      return dtoList
      // return dtoList.map(dto => this.factory.buildFromDTO(dto))
    })
  }

  async saveForm (data) {
    const uri = `${this.baseUri}/${URLS.CREATE_TRANSACTION_FORM_URL}`
    const form = {
      category_id: data.category,
      account_id: data.account,
      // credit_card
      // store
      // tag
      // recurrence
      // installment
      value: data.value,
      description: data.description,
      transaction_date: data.transactionDate,
      transaction_type: data.transactionType,
      status: data.status,
      ignore: data.ignore,
      observation: data.observation
    }

    return this.requester.post(uri, form).then(({ data: dto }) => {
      console.log(dto)
      return dto
    })
  }
}
