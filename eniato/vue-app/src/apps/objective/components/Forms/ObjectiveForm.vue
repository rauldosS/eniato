<template>
  <div id="objective-form">
    <div class="opening-balance">
      <label for="">Valor do objetivo</label>
      <b-input-group size="sm">
        <b-input-group-prepend is-text>
          <b-icon icon="piggy-bank" variant="grey" scale="1.2"></b-icon>
        </b-input-group-prepend>
        <money v-model="form.value" v-bind="money"></money>
      </b-input-group>
    </div>

    <b-input-group size="sm" class="mb-2">
      <b-input-group-prepend is-text>
        <b-icon icon="card-text" variant="grey" scale="1.2"></b-icon>
      </b-input-group-prepend>
      <b-form-input
        type="text"
        placeholder="Nome"
        v-model="form.name"
        :state="validateState('name')"
        invalid-feedback="Esse campo é obrigatório."
      ></b-form-input>
    </b-input-group>

    <b-form-datepicker
      v-model="form.objectiveDate"
      class="mb-2"
      placeholder="Data final do objetivo"
      autocomplete="on"
    ></b-form-datepicker>

    <b-dropdown variant="transparent" class="dropdown-icon">
      <template #button-content>
        <b-icon icon="palette" aria-hidden="true" variant="grey" scale="1.2"></b-icon>
        <div class="me-auto ms-3 d-flex align-items-center absolute" v-if="selectedColor">
          <div :class="`color ${selectedColor.value}`" :color="selectedColor.value"></div>
          {{ selectedColor.name }}
        </div>
        <div class="me-auto ms-3" v-else>
          Cor do objetivo
        </div>
      </template>
      <b-dropdown-item-button
        v-for="color in colorOptions"
        :key="color.value"
        @click="selectColor(color)"
      >
        <div :class="`color ${color.value}`" :color="color.value"></div>
        {{ color.name }}
      </b-dropdown-item-button>
    </b-dropdown>

    <b-dropdown variant="transparent" class="dropdown-icon">
      <template #button-content>
        <b-icon icon="image" aria-hidden="true" variant="grey"></b-icon>
        <div class="me-auto ms-3 d-flex align-items-center absolute" v-if="selectedIcon">
          <b-icon :icon="selectedIcon.value" aria-hidden="true" variant="primary" class="me-2"></b-icon>
          (Ícone selecionado)
        </div>
        <div class="me-auto ms-3" v-else>
          Ícone
        </div>
      </template>
      <b-dropdown-item-button
        v-for="icon in iconOptions"
        :key="icon.value"
        @click="selectIcon(icon)"
      >
        <b-icon :icon="icon.value" aria-hidden="true" variant="grey"></b-icon>
      </b-dropdown-item-button>
    </b-dropdown>

    <b-input-group size="sm" class="mb-2">
      <b-input-group-prepend is-text>
        <b-icon icon="card-text" variant="grey" scale="1.2"></b-icon>
      </b-input-group-prepend>
      <b-form-input
        type="text"
        placeholder="Descrição"
        v-model="form.description"
        :state="validateState('description')"
        invalid-feedback="Esse campo é obrigatório."
      ></b-form-input>
    </b-input-group>
  </div>
</template>

<script>
import { mapActions } from 'vuex'
import { validationMixin } from 'vuelidate'
import { required } from 'vuelidate/lib/validators'
import AlertService from '@helpers/AlertService'
import {
  OBJECTIVE_STORE_CONSTANTS as C
} from '@objective/constants'
import {
  COLOR_OPTIONS,
  ICON_OPTIONS
} from '@core/constants'

export default {
  name: 'ObjectiveForm',
  mixins: [validationMixin],
  components: {},
  props: {
    objective: {
      type: Object,
      default: null
    }
  },
  methods: {
    ...mapActions(C.MODULE_NAME, ['save']),
    selectColor (color) {
      this.form.color = color.value
      this.selectedColor = color
    },
    selectIcon (icon) {
      this.form.icon = icon.value
      this.selectedIcon = icon
    },
    validateState (name) {
      // const { $dirty, $error } = this.$v.form[name]
      // return $dirty ? (!$error === false ? false : null) : null
    },
    tryToSubmit () {
      this.$v.form.$touch()
      return new Promise((resolve, reject) => {
        if (this.$v.form.$anyError) {
          return resolve(false)
        }
        return this.save(this.form).catch(error => {
          console.warn(error)
          AlertService.error({})
          reject(error)
        }).then(() => resolve(true))
      })
    }
  },
  data () {
    let id = null
    let value = 0
    let balance = 0
    let name = null
    let objectiveDate = null
    let color = { value: 'blue', name: 'Azul' }
    let icon = null
    let objectiveStatus = true
    let description = null

    if (this.objective) {
      id = this.objective.id
      value = this.objective.value
      balance = this.objective.balance
      name = this.objective.name
      objectiveDate = this.objective.objectiveDate
      color = COLOR_OPTIONS.find(color => color.value === this.objective.color)
      icon = this.objective.icon
      objectiveStatus = this.objective.objectiveStatus
      description = this.objective.description
    }

    return {
      selectedColor: color,
      selectedIcon: icon,
      money: {
        decimal: ',',
        thousands: '.',
        prefix: 'R$ ',
        precision: 2,
        masked: false
      },
      colorOptions: COLOR_OPTIONS,
      iconOptions: ICON_OPTIONS,
      form: {
        id,
        value,
        balance,
        name,
        objectiveDate,
        description,
        color: color.value,
        icon,
        objectiveStatus
      }
    }
  },
  validations: {
    form: {
      value: { required },
      name: { required },
      objectiveDate: { required },
      color: { required },
      icon: { required }
    }
  }
}
</script>

<style scoped>
.opening-balance label {
  margin-left: 44px;
}

.opening-balance .input-group {
  margin-top: 0;
  margin-bottom: 0.5rem!important;
}
</style>
