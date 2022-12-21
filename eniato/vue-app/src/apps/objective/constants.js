export const ENDPOINTS_CONSTANTS = {
  BASE_REST_URL: '/objetivos/rest',
  GET_OBJECTIVE_LIST_FOR_AUTHENTICATED_USER_URL: 'objetivos/usuario',
  SAVE_OBJECTIVE_URL: 'salvar',
  ACTIVE_OBJECTIVE_URL: 'ativar/<objective-id>',
  DEACTIVATE_OBJECTIVE_URL: 'desativar/<objective-id>',
  DELETE_OBJECTIVE_URL: 'apagar/<objective-id>'
}

export const OBJECTIVE_STORE_CONSTANTS = {
  MODULE_NAME: 'ObjectiveStore',
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
