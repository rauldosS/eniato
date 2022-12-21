import Vue from 'vue'
import Vuex from 'vuex'

import { AccountStores } from './apps/account/stores'
import { CategoryStore } from './apps/category/stores/CategoryStore'
import { ObjectiveStore } from './apps/objective/stores/ObjectiveStore'
import TransactionStores from './apps/transaction/stores'

Vue.use(Vuex)

export default new Vuex.Store({
  modules: {
    ...AccountStores,
    ...TransactionStores,
    CategoryStore,
    ObjectiveStore
  },
  state: {},
  mutations: {},
  actions: {}
})
