import Vue from 'vue'
import Vuex from 'vuex'

import { AccountStore } from './apps/account/stores/AccountStore'
import { CategoryStore } from './apps/category/stores/CategoryStore'
import { TransactionStore } from './apps/transaction/stores/TransactionStore'

Vue.use(Vuex)

export default new Vuex.Store({
  state: {},
  mutations: {},
  actions: {},
  modules: {
    AccountStore,
    CategoryStore,
    TransactionStore
  }
})
