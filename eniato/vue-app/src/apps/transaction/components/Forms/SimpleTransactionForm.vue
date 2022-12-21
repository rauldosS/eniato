<template>
  <div id="transaction-form">
    <loading :active.sync="isLoading" />
    <b-input-group size="sm" class="mb-2">
      <b-input-group-prepend is-text>
        <b-icon icon="calculator" variant="grey" scale="1.2"></b-icon>
      </b-input-group-prepend>
      <money v-model="form.value" v-bind="money"></money>
    </b-input-group>

    <b-input-group size="sm" class="mb-2">
      <b-input-group-prepend is-text>
        <b-icon icon="check2-circle" variant="grey" scale="1.2"></b-icon>
      </b-input-group-prepend>
      <div class="form-check form-switch">
        <label class="form-check-label" for="status" v-text="form.transactionStatus ? 'Foi paga' : 'Não foi paga'"></label>
        <input
          class="form-check-input"
          type="checkbox"
          role="switch"
          id="status"
          v-model="form.transactionStatus"
          :disabled="expectedTransaction"
        >
      </div>
    </b-input-group>

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

    <b-form-datepicker
      v-model="form.transactionDate"
      class="mb-2"
      placeholder="Data"
      autocomplete="on"
    ></b-form-datepicker>

    <b-dropdown variant="transparent" class="dropdown-icon">
      <template #button-content>
        <b-icon icon="bookmarks" aria-hidden="true" variant="grey"></b-icon>
        <div class="me-auto ms-3 d-flex align-items-center absolute" v-if="selectedCategory">
          <b-icon :icon="selectedCategory.icon" :variant="selectedCategory.color"></b-icon>
          <div class="ms-1">{{ selectedCategory.name }}</div>
        </div>
        <div class="me-auto ms-3" v-else>
          Categoria
        </div>
      </template>
      <b-dropdown-item-button
        v-for="category in categoryList"
        :key="category.id"
        @click="selectCategory(category)"
      >
        <div :class="`${ category.color } color`">
          <b-icon :icon="category.icon" variant="white"></b-icon>
        </div>
        <div class="ms-1">{{ category.name }}</div>
      </b-dropdown-item-button>
    </b-dropdown>

    <b-dropdown
      variant="transparent"
      class="dropdown-icon"
      v-model="form.account"
      :state="validateState('description')"
      invalid-feedback="Esse campo é obrigatório."
    >
      <template #button-content>
        <b-icon icon="bank" aria-hidden="true" variant="grey"></b-icon>
        <div class="me-auto ms-3 d-flex absolute" v-if="selectedAccount">
          <img :src="selectedAccount.financialInstitution.logo" class="logo-financial-institution-sm">
          <div class="ms-1">{{ selectedAccount.description }}</div>
        </div>
        <div class="me-auto ms-3" v-else>
          Conta
        </div>
      </template>
      <b-dropdown-item-button
        v-for="account in accountList"
        :key="account.id"
        @click="selectAccount(account)"
      >
        <img :src="account.financialInstitution.logo" class="logo-financial-institution-sm">
        <div class="ms-1">{{ account.description }}</div>
      </b-dropdown-item-button>
    </b-dropdown>

    <b-input-group size="sm" class="mb-2">
      <b-input-group-prepend is-text>
        <b-icon icon="pin-angle" variant="grey" scale="1.2"></b-icon>
      </b-input-group-prepend>
      <div class="form-check form-switch">
        <label class="form-check-label" for="fixed">Transferência fixa</label>
        <input
          class="form-check-input"
          type="checkbox"
          role="switch"
          id="fixed"
          v-model="form.fixed"
          :disabled="this.form.repeat"
        >
      </div>
    </b-input-group>

    <b-input-group size="sm" class="mb-2">
      <b-input-group-prepend is-text>
        <b-icon icon="arrow-repeat" variant="grey" scale="1.2"></b-icon>
      </b-input-group-prepend>
      <div class="form-check form-switch">
        <label class="form-check-label" for="repeat">Repetir</label>
        <input
          class="form-check-input"
          type="checkbox"
          role="switch"
          id="repeat"
          v-model="form.repeat"
          :disabled="this.form.fixed"
        >
      </div>
    </b-input-group>

    <div class="row repeat ms-3 mt-3" v-if="this.form.repeat">
      <p class="fw-bold">Como sua transação se repete?</p>
      <div class="col-5">
        <label for="repeat-amount">Quantidade</label>
        <b-input-group size="sm" class="mb-2 ms-2">
          <b-input-group-prepend is-text>
            <b-icon icon="list-ol" variant="grey" scale="1.2"></b-icon>
          </b-input-group-prepend>
          <treeselect
            v-model="form.repeatAmount"
            :options="repeatAmountOptions"
            placeholder="Situação"
            class="custom-vue-tree"
          />
        </b-input-group>
      </div>

      <div class="col-7">
        <label for="repeat-period">Período</label>
        <b-input-group size="sm" class="mb-2 ms-2">
          <b-input-group-prepend is-text>
            <b-icon icon="calendar-week" variant="grey" scale="1.2"></b-icon>
          </b-input-group-prepend>
          <treeselect
            v-model="form.repeatPeriod"
            :options="repeatPeriodOptions"
            placeholder="Situação"
            class="custom-vue-tree"
          />
        </b-input-group>
      </div>
    </div>
  </div>
</template>

<script>
import Loading from 'vue-loading-overlay'
import { mapActions, mapGetters } from 'vuex'
import { validationMixin } from 'vuelidate'
import { required } from 'vuelidate/lib/validators'
import Treeselect from '@riophae/vue-treeselect'
import AlertService from '@helpers/AlertService'
import { ACCOUNT_STORE_CONSTANTS } from '@account/constants'
import { CATEGORY_STORE_CONSTANTS } from '@category/constants'
import {
  REPEAT_PERIOD_OPTIONS,
  REPEAT_AMOUNT_OPTIONS,
  TRANSACTION_STORE_CONSTANTS as C
} from '@transaction/constants'

export default {
  name: 'SimpleTransactionForm',
  mixins: [validationMixin],
  components: {
    Loading,
    Treeselect
  },
  props: {
    transaction: Object,
    transactionType: String
  },
  computed: {
    ...mapGetters(ACCOUNT_STORE_CONSTANTS.MODULE_NAME, {
      accountList: ACCOUNT_STORE_CONSTANTS.GETTERS.GET_LIST,
      isLoading: ACCOUNT_STORE_CONSTANTS.GETTERS.IS_LOADING
    }),
    ...mapGetters(CATEGORY_STORE_CONSTANTS.MODULE_NAME, {
      categoryList: CATEGORY_STORE_CONSTANTS.GETTERS.GET_LIST,
      categoriesLoading: CATEGORY_STORE_CONSTANTS.GETTERS.IS_LOADING
    }),
    expectedTransaction () {
      const expectedTransaction = new Date(this.form.transactionDate) >= this.today
      this.changeStatus(expectedTransaction)
      return expectedTransaction
    }
  },
  methods: {
    ...mapActions(C.MODULE_NAME, ['save']),
    ...mapActions(ACCOUNT_STORE_CONSTANTS.MODULE_NAME, ['loadAccountList']),
    ...mapActions(CATEGORY_STORE_CONSTANTS.MODULE_NAME, {
      loadCategories: CATEGORY_STORE_CONSTANTS.ACTIONS.LOAD_LIST
    }),
    selectCategory (category) {
      this.form.category = category.id
      this.selectedCategory = category
    },
    selectAccount (account) {
      this.form.account = account.id
      this.selectedAccount = account
    },
    validateState (name) {
      const { $dirty, $error } = this.$v.form[name]
      return $dirty ? (!$error === false ? false : null) : null
    },
    changeStatus (expectedTransaction) {
      this.form.transactionStatus = !expectedTransaction
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
    const today = new Date()

    let id = null
    let recurrence = null
    let category = null
    let account = null
    let value = 0
    let description = ''
    let transactionDate = today.toISOString().split('T')[0]
    let transactionType = this.transactionType
    let installment = 1
    let transactionStatus = null
    let observation = ''
    let fixed = false
    let repeat = false
    let repeatAmount = 2
    let repeatPeriod = 'monthly'

    if (this.transaction) {
      id = this.transaction.id
      category = this.transaction.category.id
      account = this.transaction.account.id
      value = this.transaction.value
      description = this.transaction.description
      transactionDate = this.transaction.transactionDate
      transactionType = this.transaction.transactionType
      installment = this.transaction.installment
      transactionStatus = this.transaction.status
      observation = this.transaction.observation

      if (this.transaction.recurrence) {
        recurrence = this.transaction.recurrence.id
        fixed = this.transaction.recurrence.fixed
        repeat = !this.transaction.recurrence.fixed
        repeatAmount = this.transaction.recurrence.repeatAmount
        repeatPeriod = this.transaction.recurrence.repeatPeriod
      }
    }

    return {
      selectedCategory: this.transaction ? this.transaction.category : null,
      selectedAccount: this.transaction ? this.transaction.account : null,
      today,
      repeatPeriodOptions: REPEAT_PERIOD_OPTIONS,
      repeatAmountOptions: REPEAT_AMOUNT_OPTIONS,
      money: {
        decimal: ',',
        thousands: '.',
        prefix: 'R$ ',
        precision: 2,
        masked: false
      },
      form: {
        id,
        category,
        recurrence,
        account,
        value,
        description,
        transactionDate,
        transactionType,
        installment,
        transactionStatus,
        fixed,
        repeat,
        repeatAmount,
        repeatPeriod,
        observation
      }
    }
  },
  validations: {
    form: {
      category: { required },
      value: { required },
      account: { required },
      description: { required },
      transactionDate: { required },
      transactionType: { required }
    }
  },
  mounted () {
    this.loadAccountList().then(() => {
      if (!this.transaction) {
        const defaultAccount = this.accountList.find(account => account.default)
        if (defaultAccount) {
          this.selectedAccount = defaultAccount
          this.form.account = defaultAccount.id
        }
      }
    }).catch(error => {
      console.warn(error)
      AlertService.error({})
    })

    this.loadCategories(this.transactionType).catch(error => {
      console.warn(error)
      AlertService.error({})
    })
  }
}
</script>

<style>
.repeat group {
  margin: 6px 0 !important;
}
</style>
