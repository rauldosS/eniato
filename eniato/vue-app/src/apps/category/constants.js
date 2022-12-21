export const TRANSACTIO_TYPE_ALL = 'all'
export const TRANSACTIO_TYPE_INCOME = 'income'
export const TRANSACTIO_TYPE_EXPENSE = 'expense'
export const TRANSACTIO_TYPE_CREDIT = 'credit'

export const ENDPOINTS_CONSTANTS = {
  BASE_REST_URL: '/categorias/rest',
  GET_CATEGORY_LIST_BY_TRANSACTION_TYPE_URL: {
    [TRANSACTIO_TYPE_ALL]: 'categorias/todas',
    [TRANSACTIO_TYPE_INCOME]: 'categorias/receita',
    [TRANSACTIO_TYPE_EXPENSE]: 'categorias/despesa',
    [TRANSACTIO_TYPE_CREDIT]: 'categorias/despesa'
  }
}

export const CATEGORY_STORE_CONSTANTS = {
  MODULE_NAME: 'CategoryStore',
  GETTERS: {
    GET_LIST: 'GET_LIST'
  },
  MUTATIONS: {
    SET_LIST: 'SET_LIST'
  },
  ACTIONS: {
    LOAD_LIST: 'LOAD_LIST'
  }
}
