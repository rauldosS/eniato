export const ENDPOINTS_CONSTANTS = {
  BASE_REST_URL: '/contas/rest',
  GET_ACCOUNT_LIST_FOR_AUTHENTICATED_USER_URL: 'contas/usuario',
  GET_ALL_FINANCIAL_INSTITUTIONS_URL: 'instituicoes-financeiras',
  SAVE_ACCOUNT_URL: 'salvar',
  DELETE_ACCOUNT_URL: 'apagar/<account-id>'
}

export const ACCOUNT_STORE_CONSTANTS = {
  MODULE_NAME: 'AccountStore',
  GETTERS: {
    IS_LOADING: 'IS_LOADING',
    GET_LIST: 'GET_LIST'
  },
  MUTATIONS: {
    SET_LOADING: 'SET_LOADING',
    SET_LIST: 'SET_LIST'
  },
  ACTIONS: {
    LOAD_LIST: 'LOAD_LIST'
  }
}

export const FINANCIAL_INSTITUTION_STORE_CONSTANTS = {
  MODULE_NAME: 'FinancialInstitutionStore',
  GETTERS: {
    IS_LOADING: 'IS_LOADING',
    GET_LIST: 'GET_LIST'
  },
  MUTATIONS: {
    SET_LOADING: 'SET_LOADING',
    SET_LIST: 'SET_LIST'
  },
  ACTIONS: {
    LOAD_LIST: 'LOAD_LIST'
  }
}

export const ACCOUNT_TYPE_OPTIONS = [
  { id: 'checking_account', label: 'Conta Corrente' },
  { id: 'money', label: 'Dinheiro' },
  { id: 'savings', label: 'Poupança' },
  { id: 'investments', label: 'Investimento' },
  { id: 'others', label: 'Outros' }
]
