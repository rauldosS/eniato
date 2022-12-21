import { OBJECTIVE_STORE_CONSTANTS as C } from '../constants'
import ObjectiveRepository from '../repositories/ObjectiveRepository'

const objectiveRepository = new ObjectiveRepository()

export const ObjectiveStore = {
  namespaced: true,
  state: {
    loading: false,
    objectiveList: []
  },
  getters: {
    [C.GETTERS.IS_LOADING] ({ loading }) {
      return loading
    },
    [C.GETTERS.GET_LIST] ({ objectiveList }) {
      return objectiveList
    }
  },
  actions: {
    async loadObjectiveList ({ commit }) {
      commit(C.MUTATIONS.SET_LOADING, true)
      return objectiveRepository.getObjectiveList().then(objectiveList => {
        commit(C.MUTATIONS.SET_LIST, objectiveList)
      }).finally(() => {
        commit(C.MUTATIONS.SET_LOADING, false)
      })
    },
    async save ({ commit, dispatch }, form) {
      commit(C.MUTATIONS.SET_LOADING, true)
      return objectiveRepository.save(form).then(() => {
        dispatch('loadObjectiveList')
      }).finally(() => {
        commit(C.MUTATIONS.SET_LOADING, false)
      })
    },
    async deactivate ({ commit, dispatch }, objective) {
      commit(C.MUTATIONS.SET_LOADING, true)
      return objectiveRepository.deactivate(objective).then(() => {
        dispatch('loadObjectiveList')
      }).finally(() => {
        commit(C.MUTATIONS.SET_LOADING, false)
      })
    },
    async activate ({ commit, dispatch }, objective) {
      commit(C.MUTATIONS.SET_LOADING, true)
      return objectiveRepository.activate(objective).then(() => {
        dispatch('loadObjectiveList')
      }).finally(() => {
        commit(C.MUTATIONS.SET_LOADING, false)
      })
    },
    async delete ({ commit, dispatch }, objective) {
      commit(C.MUTATIONS.SET_LOADING, true)
      return objectiveRepository.delete(objective).then(() => {
        dispatch('loadObjectiveList')
      }).finally(() => {
        commit(C.MUTATIONS.SET_LOADING, false)
      })
    }
  },
  mutations: {
    [C.MUTATIONS.SET_LOADING] (state, status) {
      state.loading = status
    },
    [C.MUTATIONS.SET_LIST] (state, objectiveList) {
      state.objectiveList = objectiveList
    }
  }
}
