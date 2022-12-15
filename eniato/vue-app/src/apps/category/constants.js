export const TRANSACTIO_TYPE_INCOME = 'income'
export const TRANSACTIO_TYPE_EXPENSE = 'expense'
export const TRANSACTIO_TYPE_CREDIT = 'credit'

export const ENDPOINTS_CONSTANTS = {
  BASE_REST_URL: '/categoria/rest',
  GET_CATEGORY_LIST_BY_TRANSACTION_TYPE_URL: {
    [TRANSACTIO_TYPE_INCOME]: 'categorias/receita',
    [TRANSACTIO_TYPE_EXPENSE]: 'categorias/despesa',
    [TRANSACTIO_TYPE_CREDIT]: 'categorias/despesa'
  }
}

export const CATEGORY_STORE_CONSTANTS = {
  MODULE_NAME: 'CategoryStore',
  GETTERS: {
    GET_CATEGORY_LIST: 'GET_CATEGORY_LIST'
  },
  MUTATIONS: {
    SET_CATEGORY_LIST: 'SET_CATEGORY_LIST'
  },
  ACTIONS: {
    LOAD_CATEGORY_LIST: 'LOAD_CATEGORY_LIST'
  }
}
