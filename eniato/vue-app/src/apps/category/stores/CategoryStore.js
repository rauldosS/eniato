import { CATEGORY_STORE_CONSTANTS as C } from '../constants'
import CategoryRepository from '../repositories/CategoryRepository'

const categoryRepository = new CategoryRepository()

export const CategoryStore = {
  namespaced: true,
  state: {
    loading: false,
    categoryList: []
  },
  getters: {
    [C.GETTERS.GET_LIST] ({ categoryList }) {
      return categoryList.map(c => c.toDTO())
    }
  },
  actions: {
    async [C.ACTIONS.LOAD_LIST] ({ commit }, transactionType) {
      await categoryRepository.getCategoriesByTransactionType(transactionType).then(
        (categoryList) => {
          commit(C.MUTATIONS.SET_LIST, categoryList)
        }
      )
    }
  },
  mutations: {
    [C.MUTATIONS.SET_LIST] (state, categoryList) {
      state.categoryList = categoryList
    }
  }
}
