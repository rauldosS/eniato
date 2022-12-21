import { TRANSACTION_SUMMARY_STORE_CONSTANTS as C } from '../constants'
import TransactionSummaryRepository from '../repositories/TransactionSummaryRepository'

const transactionSummaryRepository = new TransactionSummaryRepository()

export const TransactionSummaryStore = {
  namespaced: true,
  state: {
    loading: false,
    filtered: false,
    transactionSummary: null
  },
  getters: {
    [C.GETTERS.IS_LOADING] ({ loading }) {
      return loading
    },
    [C.GETTERS.IS_FILTERED] ({ filtered }) {
      return filtered
    },
    [C.GETTERS.GET_TRANSACTION_SUMMARY] ({ transactionSummary }) {
      return transactionSummary
    }
  },
  actions: {
    async loadTransactionSummary ({ commit }, { initialDate, finalDate, status = null, categoryId = null, accountId = null, query = null, filtered = false }) {
      commit(C.MUTATIONS.SET_LOADING, true)
      await transactionSummaryRepository.getTransactionSummary(initialDate, finalDate, status, categoryId, accountId, query).then(transactionSummary => {
        commit(C.MUTATIONS.SET_TRANSACTION_SUMMARY, transactionSummary)
        commit(C.MUTATIONS.SET_FILTERED, filtered)
      }).finally(() => {
        commit(C.MUTATIONS.SET_LOADING, false)
      })
    }
  },
  mutations: {
    [C.MUTATIONS.SET_LOADING] (state, status) {
      state.loading = status
    },
    [C.MUTATIONS.SET_FILTERED] (state, status) {
      state.filtered = status
    },
    [C.MUTATIONS.SET_TRANSACTION_SUMMARY] (state, transactionSummary) {
      state.transactionSummary = transactionSummary
    }
  }
}
