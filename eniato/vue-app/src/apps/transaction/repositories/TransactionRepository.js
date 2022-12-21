import Axios from 'axios'
import { ENDPOINTS_CONSTANTS as URLS } from '../constants'

export default class TransactionRepository {
  constructor (requester = null, baseUri = null) {
    this.requester = requester || Axios
    this.baseUri = baseUri || URLS.BASE_TRANSACTION_REST_URL
  }

  async save (data) {
    const uri = `${this.baseUri}/${URLS.SAVE_TRANSACTION_FORM_URL}`
    const form = {
      id: data.id,
      category_id: data.category,
      recurrence_id: data.recurrence,
      account_id: data.account,
      value: data.value,
      description: data.description,
      transaction_date: data.transactionDate,
      transaction_type: data.transactionType,
      installment: data.installment,
      status: data.transactionStatus,
      ignore: data.ignore,
      fixed: data.fixed,
      repeat: data.repeat,
      repeatAmount: data.repeatAmount,
      repeatPeriod: data.repeatPeriod,
      observation: data.observation
    }

    return this.requester.post(uri, form).then(({ data: dto }) => {
      return dto
    })
  }

  async delete (transaction) {
    const uri = `${this.baseUri}/${URLS.DELETE_TRANSACTION_URL}`.replace('<transaction-id>', transaction.id)
    return this.requester.post(uri)
  }
}
