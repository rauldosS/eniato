import Vue from 'vue'
import Vuex from 'vuex'

import { AccountStores } from './apps/account/stores'
import { CategoryStore } from './apps/category/stores/CategoryStore'
import TransactionStores from './apps/transaction/stores'

Vue.use(Vuex)

export default new Vuex.Store({
  modules: {
    ...AccountStores,
    ...TransactionStores,
    CategoryStore
  },
  state: {},
  mutations: {},
  actions: {}
})
