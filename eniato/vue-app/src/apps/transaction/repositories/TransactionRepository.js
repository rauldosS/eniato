import Axios from 'axios'
import { ENDPOINTS_CONSTANTS as URLS } from '../constants'

export default class TransactionRepository {
  constructor (requester = null, baseUri = null) {
    this.requester = requester || Axios
    this.baseUri = baseUri || URLS.BASE_TRANSACTION_REST_URL
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
      return dto
    })
  }
}
