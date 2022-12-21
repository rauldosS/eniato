export const ENDPOINTS_CONSTANTS = {
  BASE_TRANSACTION_REST_URL: '/transacoes/rest',
  GET_TRANSACTION_LIST_FOR_AUTHENTICATED_USER_URL: 'transacoes',
  SAVE_TRANSACTION_FORM_URL: 'salvar',
  DELETE_TRANSACTION_URL: 'apagar/<transaction-id>'
}

export const TRANSACTION_TYPE = {
  INCOME: 'income',
  EXPENSE: 'expense',
  CREDIT: 'credit',
  TRANSFER: 'transfer',
  OBJECTIVE: 'objective'
}

export const TRANSACTION_TYPE_DISPLAY_NAME = {
  TRANSACTION_TYPE: 'Receita',
  EXPENSE: 'Despesa',
  CREDIT: 'Crédito',
  TRANSFER: 'Transferência',
  OBJECTIVE: 'Objetivo'
}

export const REPEAT_AMOUNT_OPTIONS = Array(63).fill(0).map((_, i) => (
  {
    id: i + 2,
    label: i + 2
  }
))

export const REPEAT_PERIOD_OPTIONS = [
  { id: 'everyday', label: 'Todos os dias' },
  { id: 'weekly', label: 'Semanalmente' },
  { id: 'monthly', label: 'Mensalmente' },
  { id: 'annually', label: 'Anualmente' }
]

export const TRANSACTION_STORE_CONSTANTS = {
  MODULE_NAME: 'TransactionStore',
  GETTERS: {
    IS_LOADING: 'IS_LOADING',
    GET_TRANSACTION: 'GET_TRANSACTION',
    GET_LIST: 'GET_LIST'
  },
  MUTATIONS: {
    SET_LOADING: 'SET_LOADING',
    SET_TRANSACTION: 'SET_TRANSACTION',
    SET_LIST: 'SET_LIST'
  }
}

export const TRANSACTION_SUMMARY_STORE_CONSTANTS = {
  MODULE_NAME: 'TransactionSummaryStore',
  GETTERS: {
    IS_LOADING: 'IS_LOADING',
    IS_FILTERED: 'IS_FILTERED',
    GET_TRANSACTION_SUMMARY: 'GET_TRANSACTION_SUMMARY'
  },
  MUTATIONS: {
    SET_LOADING: 'SET_LOADING',
    SET_FILTERED: 'SET_FILTERED',
    SET_TRANSACTION_SUMMARY: 'SET_TRANSACTION_SUMMARY'
  }
}

export const TRANSACTION_STATUS_OPTIONS = [
  { id: false, label: 'Pagas' },
  { id: true, label: 'Não pagas' }
]
