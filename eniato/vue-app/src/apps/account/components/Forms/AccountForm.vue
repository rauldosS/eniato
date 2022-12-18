<template>
  <div id="account-form">
    <div class="opening-balance">
      <label for="">Saldo atual da conta</label>
      <b-input-group size="sm">
        <b-input-group-prepend is-text>
          <b-icon icon="piggy-bank" variant="grey" scale="1.2"></b-icon>
        </b-input-group-prepend>
        <money v-model="form.openingBalance" :disabled="this.account" v-bind="money"></money>
      </b-input-group>
    </div>

    <b-dropdown variant="transparent" class="dropdown-icon">
      <template #button-content>
        <b-icon icon="bank" aria-hidden="true" variant="grey"></b-icon>
        <div class="me-auto ms-3 d-flex align-items-center absolute" v-if="selectedfinancialInstitution">
          <img :src="selectedfinancialInstitution.logo" class="logo-financial-institution-sm">
          <div class="ms-1">{{ selectedfinancialInstitution.name }}</div>
        </div>
        <div class="me-auto ms-3" v-else>
          Instituição Financeira
        </div>
      </template>
      <b-dropdown-item-button
        v-for="financialInstitution in financialInstitutionList"
        :key="financialInstitution.id"
        @click="selectFinancialInstitution(financialInstitution)"
      >
        <img :src="financialInstitution.logo" class="logo-financial-institution-sm">
        <div class="ms-1">{{ financialInstitution.name }}</div>
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

    <b-input-group size="sm" class="mb-2"
      :state="validateState('accountType')"
      invalid-feedback="Esse campo é obrigatório."
    >
      <b-input-group-prepend is-text>
        <b-icon icon="wallet2" variant="grey" scale="1.2"></b-icon>
      </b-input-group-prepend>
      <treeselect
        v-model="form.accountType"
        :options="accountTypeOptions"
        placeholder="Selecione o tipo da conta"
        :required="true"
        class="custom-vue-tree"
      />
    </b-input-group>

    <b-dropdown variant="transparent" class="dropdown-icon">
      <template #button-content>
        <b-icon icon="bank" aria-hidden="true" variant="grey"></b-icon>
        <div class="me-auto ms-3 d-flex align-items-center absolute" v-if="selectedColor">
          <div :class="`color ${selectedColor.value}`" :color="selectedColor.value"></div>
          {{ selectedColor.name }}
        </div>
        <div class="me-auto ms-3" v-else>
          Cor da conta
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

    <b-input-group size="sm" class="mb-2">
      <b-input-group-prepend is-text>
        <b-icon icon="check2-circle" variant="grey" scale="1.2"></b-icon>
      </b-input-group-prepend>
      <div class="form-check form-switch">
        <label class="form-check-label" for="default">Conta padrão</label>
        <input
          class="form-check-input"
          type="checkbox"
          role="switch"
          id="default"
          v-model="form.default"
          :disabled="this.account && this.account.default"
        >
      </div>
    </b-input-group>
  </div>
</template>

<script>
import { mapActions, mapState } from 'vuex'
import { validationMixin } from 'vuelidate'
import { required } from 'vuelidate/lib/validators'
import Treeselect from '@riophae/vue-treeselect'
// import Loading from 'vue-loading-overlay'
import AlertService from '@helpers/AlertService'
import {
  ACCOUNT_STORE_CONSTANTS as C,
  ACCOUNT_TYPE_OPTIONS,
  FINANCIAL_INSTITUTION_STORE_CONSTANTS
} from '@account/constants'
import { COLOR_OPTIONS } from '@core/constants'

export default {
  name: 'AccountForm',
  mixins: [validationMixin],
  components: { Treeselect },
  props: {
    account: {
      type: Object,
      default: null
    }
  },
  computed: {
    ...mapState(FINANCIAL_INSTITUTION_STORE_CONSTANTS.MODULE_NAME, ['financialInstitutionList'])
  },
  methods: {
    ...mapActions(C.MODULE_NAME, ['save']),
    ...mapActions(FINANCIAL_INSTITUTION_STORE_CONSTANTS.MODULE_NAME, {
      loadFinancialInstitutions: FINANCIAL_INSTITUTION_STORE_CONSTANTS.ACTIONS.LOAD_LIST
    }),
    selectFinancialInstitution (financialInstitution) {
      this.form.financialInstitution = financialInstitution.id
      this.selectedfinancialInstitution = financialInstitution
    },
    selectColor (color) {
      this.form.color = color.value
      this.selectedColor = color
    },
    validateState (name) {
      const { $dirty, $error } = this.$v.form[name]
      return $dirty ? (!$error === false ? false : null) : null
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
    let financialInstitution = null
    let openingBalance = null
    let description = null
    let accountType = null
    let color = { value: 'blue', name: 'Azul' }
    let accountDefault = null

    if (this.account) {
      id = this.account.id
      financialInstitution = this.account.financialInstitution.id
      openingBalance = this.account.openingBalance
      description = this.account.description
      accountType = this.account.accountType
      color = COLOR_OPTIONS.find(color => color.value === this.account.color)
      accountDefault = this.account.default
    }

    return {
      selectedfinancialInstitution: this.account ? this.account.financialInstitution : null,
      selectedColor: color,
      money: {
        decimal: ',',
        thousands: '.',
        prefix: 'R$ ',
        precision: 2,
        masked: false
      },
      colorOptions: COLOR_OPTIONS,
      accountTypeOptions: ACCOUNT_TYPE_OPTIONS,
      form: {
        id,
        financialInstitution,
        openingBalance,
        description,
        accountType,
        color,
        default: accountDefault
      }
    }
  },
  validations: {
    form: {
      financialInstitution: { required },
      openingBalance: { required },
      description: { required },
      accountType: { required },
      color: { required },
      default: { required }
    }
  },
  created () {
    this.loadFinancialInstitutions().catch(error => {
      console.warn(error)
      AlertService.error({})
    })
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
