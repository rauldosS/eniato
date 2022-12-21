<template>
  <div class="col-md-12">
    <div :class="`card shadow-sm border-0 mb-4 ${ !objective.active ? 'opacity-80' : '' }`">
      <div class="card-header d-flex bg-transparent border-0">
        <div :class="`circle-fill circle-fill-lg ${ objective.color }`">
          <b-icon :icon="objective.icon" :width="24" :height="24" :color="'var(--bright-color)'"></b-icon>
        </div>
        <div class="fs-5 ms-2 d-flex align-items-center">
          <span class="align-middle">{{ objective.name }}</span>
        </div>
        <div class="ms-auto">
          <div class="dropdown">
            <a class="" id="dropdown-objective" data-bs-toggle="dropdown" aria-expanded="false">
              <span class="align-middle">
                <svg xmlns="http://www.w3.org/2000/svg" width="18" height="18" fill="currentColor" class="bi bi-three-dots-vertical mt-2" viewBox="0 0 16 16">
                  <path d="M9.5 13a1.5 1.5 0 1 1-3 0 1.5 1.5 0 0 1 3 0zm0-5a1.5 1.5 0 1 1-3 0 1.5 1.5 0 0 1 3 0zm0-5a1.5 1.5 0 1 1-3 0 1.5 1.5 0 0 1 3 0z"/>
                </svg>
              </span>
            </a>
            <ul class="dropdown-menu" aria-labelledby="dropdown-objective">
              <li>
                <button
                  class="dropdown-item"
                  @click.stop="openObjectiveFormModal(objective)"
                  :disabled="['stopped'].includes(objective.status)"
                >
                  Editar
                </button>
              </li>
              <li v-if="['active'].includes(objective.status)">
                <button
                  class="dropdown-item"
                  @click.stop="deactivateObjective(objective)"
                >
                  Parar
                </button>
              </li>
              <li v-else>
                <button
                  class="dropdown-item"
                  @click.stop="activateObjective(objective)"
                >
                  Ativar
                </button>
              </li>
              <li>
                <button
                  class="dropdown-item"
                  @click.stop="openDeleteObjectiveModal(objective)"
                >
                  Apagar
                </button>
              </li>
            </ul>
          </div>
        </div>
      </div>
      <div class="card-body pb-0">
        <b-progress :max="objective.value" class="mb-3" height="2rem">
          <b-progress-bar :variant="objective.color" :value="objective.balance" :label="`${((objective.balance / objective.value) * 100).toFixed(2)}%`"></b-progress-bar>
        </b-progress>
        <div class="d-flex justify-content-between align-items-center">
          <p class="text-muted" v-text="`${currencyFormat(objective.balance)} de ${currencyFormat(objective.value)}`"></p>
          <p class="text-muted" v-text="`Restam: ${daysRemaining(objective.objectiveDate)} dias`"></p>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import Formatter from '@helpers/Formatter'
import { mapActions } from 'vuex'
import { OBJECTIVE_STORE_CONSTANTS as C } from '@objective/constants'

export default {
  name: 'ObjectiveCard',
  components: {
  },
  props: ['objective'],
  methods: {
    ...mapActions(C.MODULE_NAME, ['deactivate', 'activate']),
    currencyFormat (money) {
      return Formatter.currency(money)
    },
    openObjectiveFormModal (objective) {
      this.$emit('open-objective-modal-form', objective)
    },
    openDeleteObjectiveModal (objective) {
      this.$emit('open-delete-objective-modal', objective)
    },
    deactivateObjective (objective) {
      this.deactivate(objective)
    },
    activateObjective (objective) {
      this.activate(objective)
    },
    daysRemaining (date) {
      const ONE_DAY = 24 * 60 * 60 * 1000
      const firstDate = new Date()
      const secondDate = new Date(date)

      return Math.round(Math.abs((firstDate - secondDate) / ONE_DAY))
    }
  }
}
</script>

<style scoped>

.dropdown-menu {
  opacity: 100% !important;
}

.circle-fill {
  left: 0;
  transform: none;
}

.progress {
  border-radius: 18px !important;
}
</style>
