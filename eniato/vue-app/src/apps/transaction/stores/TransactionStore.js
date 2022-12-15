import { TRANSACTION_STORE_CONSTANTS as C } from '../constants'
import TransactionRepository from '../repositories/TransactionRepository'

const transactionRepository = new TransactionRepository()

export const TransactionStore = {
  namespaced: true,
  state: {
    loading: false,
    saving: false,
    transaction: false,
    transactionList: []
  },
  getters: {
    [C.GETTERS.GET_TRANSACTION] ({ transaction }) {
      return transaction
    },
    [C.GETTERS.GET_LIST] ({ transactionList }) {
      return transactionList
    },
    [C.GETTERS.LIST_IS_LOADING] ({ loading }) {
      return loading
    },
    [C.GETTERS.IS_SAVING] ({ saving }) {
      return saving
    }
  },
  actions: {
    async loadTransactionList ({ commit }, { initialDate, finalDate, query }) {
      commit(C.MUTATIONS.SET_LOADING, true)
      return transactionRepository.getTransactionList(initialDate, finalDate, query).then(transactionList => {
        commit(C.MUTATIONS.SET_TRANSACTION_LIST, transactionList)
      }).finally(() => {
        commit(C.MUTATIONS.SET_LOADING, false)
      })
    },
    async save ({ state, commit }, form) {
      commit(C.MUTATIONS.SET_SAVING, true)
      return transactionRepository.saveForm(form).then(event => {
        commit(C.MUTATIONS.SET_TRANSACTION, event)
      }).finally(() => {
        commit(C.MUTATIONS.SET_SAVING, false)
      })
    }
  },
  mutations: {
    [C.MUTATIONS.SET_LOADING] (state, status) {
      state.loading = status
    },
    [C.MUTATIONS.SET_TRANSACTION] (state, transaction) {
      state.transaction = transaction
    },
    [C.MUTATIONS.SET_TRANSACTION_LIST] (state, transactionList) {
      state.transactionList = transactionList
    },
    [C.MUTATIONS.SET_SAVING] (state, status) {
      state.saving = status
    }
  }
}
