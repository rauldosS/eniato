import { ACCOUNT_STORE_CONSTANTS as C } from '../constants'
import AccountRepository from '../repositories/AccountRepository'

const accountRepository = new AccountRepository()

export const AccountStore = {
  namespaced: true,
  state: {
    loading: false,
    accountList: []
  },
  getters: {
    [C.GETTERS.IS_LOADING] ({ loading }) {
      return loading
    },
    [C.GETTERS.GET_LIST] ({ accountList }) {
      return accountList.map(c => c.toDTO())
    }
  },
  actions: {
    async loadAccountList ({ commit }) {
      commit(C.MUTATIONS.SET_LOADING, true)
      return accountRepository.getAccountList().then(accountList => {
        commit(C.MUTATIONS.SET_LIST, accountList)
      }).finally(() => {
        commit(C.MUTATIONS.SET_LOADING, false)
      })
    },
    async save ({ commit, dispatch }, form) {
      commit(C.MUTATIONS.SET_LOADING, true)
      return accountRepository.save(form).then(() => {
        dispatch('loadAccountList')
      }).finally(() => {
        commit(C.MUTATIONS.SET_LOADING, false)
      })
    },
    async deactivate ({ commit, dispatch }, account) {
      commit(C.MUTATIONS.SET_LOADING, true)
      return accountRepository.deactivate(account).then(() => {
        dispatch('loadAccountList')
      }).finally(() => {
        commit(C.MUTATIONS.SET_LOADING, false)
      })
    },
    async activate ({ commit, dispatch }, account) {
      commit(C.MUTATIONS.SET_LOADING, true)
      return accountRepository.activate(account).then(() => {
        dispatch('loadAccountList')
      }).finally(() => {
        commit(C.MUTATIONS.SET_LOADING, false)
      })
    },
    async delete ({ commit, dispatch }, account) {
      commit(C.MUTATIONS.SET_LOADING, true)
      return accountRepository.delete(account).then(() => {
        dispatch('loadAccountList')
      }).finally(() => {
        commit(C.MUTATIONS.SET_LOADING, false)
      })
    }
  },
  mutations: {
    [C.MUTATIONS.SET_LOADING] (state, status) {
      state.loading = status
    },
    [C.MUTATIONS.SET_LIST] (state, accountList) {
      state.accountList = accountList
    }
  }
}
