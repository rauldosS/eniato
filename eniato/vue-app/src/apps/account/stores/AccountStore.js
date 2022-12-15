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
    [C.GETTERS.GET_ACCOUNT_LIST] ({ accountList }) {
      return accountList.map(c => c.toDTO())
    }
  },
  actions: {
    async [C.ACTIONS.LOAD_ACCOUNT_LIST] ({ commit }) {
      await accountRepository.getAccountList().then(
        (accountList) => {
          commit(C.MUTATIONS.SET_ACCOUNT_LIST, accountList)
        }
      )
    }
  },
  mutations: {
    [C.MUTATIONS.SET_ACCOUNT_LIST] (state, accountList) {
      state.accountList = accountList
    }
  }
}
