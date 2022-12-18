import { FINANCIAL_INSTITUTION_STORE_CONSTANTS as C } from '../constants'
import FinancialInstitutionRepository from '../repositories/FinancialInstitutionRepository'

const financialInstitutionRepository = new FinancialInstitutionRepository()

export const FinancialInstitutionStore = {
  namespaced: true,
  state: {
    loading: false,
    financialInstitutionList: []
  },
  getters: {
    [C.GETTERS.GET_LIST] ({ financialInstitutionList }) {
      return financialInstitutionList
    },
    [C.GETTERS.IS_LOADING] ({ loading }) {
      return loading
    }
  },
  actions: {
    async [C.ACTIONS.LOAD_LIST] ({ commit }) {
      commit(C.MUTATIONS.SET_LOADING, true)
      await financialInstitutionRepository.getFinancialInstitutionList().then(financialInstitutionList => {
        commit(C.MUTATIONS.SET_LIST, financialInstitutionList)
      }).finally(() => {
        commit(C.MUTATIONS.SET_LOADING, false)
      })
    }
  },
  mutations: {
    [C.MUTATIONS.SET_LOADING] (state, status) {
      state.loading = status
    },
    [C.MUTATIONS.SET_LIST] (state, financialInstitutionList) {
      state.financialInstitutionList = financialInstitutionList
    }
  }
}
