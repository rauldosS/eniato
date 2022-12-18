import Vue from 'vue'
import Vuex from 'vuex'

import { AccountStores } from './apps/account/stores'
import { CategoryStore } from './apps/category/stores/CategoryStore'
import { TransactionStore } from './apps/transaction/stores/TransactionStore'

Vue.use(Vuex)

export default new Vuex.Store({
  modules: {
    ...AccountStores,
    CategoryStore,
    TransactionStore
  },
  state: {},
  mutations: {},
  actions: {}
})
