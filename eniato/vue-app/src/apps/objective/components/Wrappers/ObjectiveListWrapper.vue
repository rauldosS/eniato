<template>
  <div>
    <loading :active.sync="isLoading" />
    <div class="py-3 text-center" v-if="objectiveList.length > 0">
      <h1 class="display-4">Objetivos</h1>
      <p class="lead">Organize-se com seus objetivos de curto, médio e longo prazo.</p>
    </div>
    <div class="container-centered" v-else>
      <h3>Ops!</h3>
      <p>Sem objetivos criadas até o momento.</p>
      <b-button
        pill
        variant="purple"
        size="lg"
        @click.stop="openObjectiveFormModal(null)"
      >ADICIONAR OBJETIVO</b-button>
    </div>

    <ObjectiveList
      :objective-list="objectiveList"
      v-on:openObjectiveFormModal="openObjectiveFormModal"
      v-on:openDeleteObjectiveModal="openDeleteObjectiveModal"
    />

    <ObjectiveFormModal ref="objective-form-modal" />

    <b-button
      size="lg"
      variant="primary"
      class="btn-float"
      @click.stop="openObjectiveFormModal(null)"
    >
      <b-icon icon="plus"></b-icon>
    </b-button>
  </div>
</template>

<script>
import Loading from 'vue-loading-overlay'
import { mapGetters, mapActions } from 'vuex'
import AlertService from '@helpers/AlertService'
import ObjectiveList from '../List/ObjectiveList'
import ObjectiveFormModal from '../Modals/ObjectiveFormModal'
import { OBJECTIVE_STORE_CONSTANTS as C } from '@objective/constants'

export default {
  name: 'ObjectiveListWrapper',
  components: {
    Loading,
    ObjectiveList,
    ObjectiveFormModal
  },
  computed: {
    ...mapGetters(C.MODULE_NAME, {
      objectiveList: C.GETTERS.GET_LIST,
      isLoading: C.GETTERS.IS_LOADING
    })
  },
  methods: {
    ...mapActions(C.MODULE_NAME, ['loadObjectiveList']),
    openObjectiveFormModal (objective) {
      this.$refs['objective-form-modal'].open(objective)
    },
    openDeleteObjectiveModal (objective) {
      this.$refs['delete-objective-modal'].open(objective)
    }
  },
  created () {
    this.loadObjectiveList().catch(error => {
      console.warn(error)
      AlertService.error({})
    })
  }
}
</script>
