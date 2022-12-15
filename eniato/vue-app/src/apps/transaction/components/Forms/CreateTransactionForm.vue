<template>
  <div id="create-transaction-form">
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
        <label class="form-check-label" for="status" v-text="form.status ? 'Foi paga' : 'Não foi paga'"></label>
        <input
          class="form-check-input"
          type="checkbox"
          role="switch"
          id="status"
          v-model="form.status"
          :disabled="expectedTransaction"
        >
      </div>
    </b-input-group>

    <b-input-group size="sm" class="mb-2">
      <b-input-group-prepend is-text>
        <b-icon icon="file-earmark" variant="grey" scale="1.2"></b-icon>
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
        <b-icon icon="check2-circle" variant="grey" scale="1.2"></b-icon>
      </b-input-group-prepend>
      <div class="form-check form-switch">
        <label class="form-check-label" for="ignore">Ignorar transação</label>
        <input class="form-check-input" type="checkbox" role="switch" id="ignore" v-model="form.ignore">
      </div>
    </b-input-group>

    <div class="d-flex justify-content-center">
      <b-button pill variant="primary">
        Menos detalhes <b-icon icon="caret-up" variant="white"></b-icon>
      </b-button>
    </div>
  </div>
</template>

<script>
import { mapActions, mapState } from 'vuex'
import { validationMixin } from 'vuelidate'
import { required } from 'vuelidate/lib/validators'
// import Loading from 'vue-loading-overlay'
import AlertService from '@helpers/AlertService'
import { ACCOUNT_STORE_CONSTANTS } from '@account/constants'
import { CATEGORY_STORE_CONSTANTS } from '@category/constants'
import { TRANSACTION_STORE_CONSTANTS as C } from '@transaction/constants'

export default {
  name: 'CreateTransactionForm',
  components: {
  },
  mixins: [validationMixin],
  props: {
    transactionType: String
  },
  computed: {
    ...mapState(ACCOUNT_STORE_CONSTANTS.MODULE_NAME, ['accountList']),
    ...mapState(CATEGORY_STORE_CONSTANTS.MODULE_NAME, ['categoryList']),
    expectedTransaction () {
      const expectedTransaction = new Date(this.form.transactionDate) >= this.today
      this.changeStatus(expectedTransaction)
      return expectedTransaction
    }
  },
  methods: {
    ...mapActions(C.MODULE_NAME, ['save']),
    ...mapActions(ACCOUNT_STORE_CONSTANTS.MODULE_NAME, {
      loadAccounts: ACCOUNT_STORE_CONSTANTS.ACTIONS.LOAD_ACCOUNT_LIST
    }),
    ...mapActions(CATEGORY_STORE_CONSTANTS.MODULE_NAME, {
      loadCategories: CATEGORY_STORE_CONSTANTS.ACTIONS.LOAD_CATEGORY_LIST
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
      this.form.status = !expectedTransaction
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

    return {
      selectedCategory: null,
      selectedAccount: null,
      today,
      money: {
        decimal: ',',
        thousands: '.',
        prefix: 'R$ ',
        precision: 2,
        masked: false
      },
      form: {
        category: null,
        account: null,
        value: 0,
        description: '',
        transactionDate: today.toISOString().split('T')[0],
        transactionType: this.transactionType,
        status: true,
        ignore: false,
        observation: ''
      }
    }
  },
  validations: {
    form: {
      category: { required },
      account: { required },
      description: { required },
      transactionDate: { required },
      transactionType: { required },
      status: { required }
    }
  },
  mounted () {
    this.loadAccounts().then(() => {
      const defaultAccount = this.accountList.find(account => account.default)
      this.selectedAccount = defaultAccount
      this.form.account = defaultAccount.id
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

<style scoped>
.form-switch {
  display: flex;
  justify-content: space-between!important;
  width: calc(100% - 44px) !important;
  margin: 0;
  padding: 0;
  align-items: center;
}
</style>
