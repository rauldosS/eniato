import { TRANSACTION_SUMMARY_STORE_CONSTANTS as C } from '../constants'
import TransactionSummaryRepository from '../repositories/TransactionSummaryRepository'

const transactionSummaryRepository = new TransactionSummaryRepository()

export const TransactionSummaryStore = {
  namespaced: true,
  state: {
    loading: false,
    saving: false,
    transactionSummary: null
  },
  getters: {
    [C.GETTERS.IS_LOADING] ({ loading }) {
      return loading
    },
    [C.GETTERS.GET_TRANSACTION_SUMMARY] ({ transactionSummary }) {
      return transactionSummary
    }
  },
  actions: {
    async loadTransactionSummary ({ commit }, { initialDate, finalDate, query }) {
      commit(C.MUTATIONS.SET_LOADING, true)
      await transactionSummaryRepository.getTransactionSummary(initialDate, finalDate, query).then(transactionSummary => {
        commit(C.MUTATIONS.SET_TRANSACTION_SUMMARY, transactionSummary)
      }).finally(() => {
        commit(C.MUTATIONS.SET_LOADING, false)
      })
    }
  },
  mutations: {
    [C.MUTATIONS.SET_LOADING] (state, status) {
      state.loading = status
    },
    [C.MUTATIONS.SET_TRANSACTION_SUMMARY] (state, transactionSummary) {
      state.transactionSummary = transactionSummary
    }
  }
}
