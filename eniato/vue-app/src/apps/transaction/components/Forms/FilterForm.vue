<template>
  <div id="filter-form">
    <b-input-group size="sm" class="mb-2">
      <b-input-group-prepend is-text>
        <b-icon icon="check2-circle" variant="grey" scale="1.2"></b-icon>
      </b-input-group-prepend>
      <treeselect
        v-model="form.status"
        :options="statusOptions"
        placeholder="Situação"
        class="custom-vue-tree"
      />
    </b-input-group>

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

    <p class="mt-4 fw-bold">Filtro por período</p>

    <div class="">
      <label for="">Data inicial</label>
      <b-form-datepicker
        v-model="form.initialDate"
        class="mb-2 mt-0"
        placeholder="Data"
        autocomplete="on"
      ></b-form-datepicker>
    </div>

    <div class="">
      <label for="">Data final</label>
      <b-form-datepicker
        v-model="form.finalDate"
        class="mb-2 mt-0"
        placeholder="Data"
        autocomplete="on"
      ></b-form-datepicker>
    </div>
  </div>
</template>

<script>
// import Loading from 'vue-loading-overlay'
import { mapActions, mapGetters } from 'vuex'
import { validationMixin } from 'vuelidate'
import { required } from 'vuelidate/lib/validators'
import Treeselect from '@riophae/vue-treeselect'
import AlertService from '@helpers/AlertService'
import { ACCOUNT_STORE_CONSTANTS } from '@account/constants'
import { CATEGORY_STORE_CONSTANTS } from '@category/constants'
import {
  TRANSACTION_STATUS_OPTIONS,
  TRANSACTION_SUMMARY_STORE_CONSTANTS as C
} from '@transaction/constants'

export default {
  name: 'FilterForm',
  mixins: [validationMixin],
  components: { Treeselect },
  props: {
    initialDate: Date,
    finalDate: Date
  },
  computed: {
    ...mapGetters(ACCOUNT_STORE_CONSTANTS.MODULE_NAME, {
      accountList: ACCOUNT_STORE_CONSTANTS.GETTERS.GET_LIST,
      isLoading: ACCOUNT_STORE_CONSTANTS.GETTERS.IS_LOADING
    }),
    ...mapGetters(CATEGORY_STORE_CONSTANTS.MODULE_NAME, {
      categoryList: CATEGORY_STORE_CONSTANTS.GETTERS.GET_LIST,
      categoriesLoading: CATEGORY_STORE_CONSTANTS.GETTERS.IS_LOADING
    })
  },
  methods: {
    ...mapActions(C.MODULE_NAME, ['loadTransactionSummary']),
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
    tryToSubmit () {
      this.$v.form.$touch()
      return new Promise((resolve, reject) => {
        if (this.$v.form.$anyError) {
          return resolve(false)
        }

        this.loadTransactionSummary({
          initialDate: this.form.initialDate,
          finalDate: this.form.finalDate,
          status: this.form.status,
          categoryId: this.form.category,
          accountId: this.form.account,
          filtered: true
        }).catch(error => {
          console.warn(error)
          AlertService.error({})
          reject(error)
        }).then(() => {
          const initiaDate = typeof this.form.initialDate !== 'string' ? this.form.initialDate : new Date(this.form.initialDate)
          const finalDate = typeof this.form.finalDate !== 'string' ? this.form.finalDate : new Date(this.form.finalDate)
          this.$emit('update-dates', initiaDate, finalDate)
          resolve(true)
        })
      })
    }
  },
  data () {
    return {
      selectedCategory: null,
      selectedAccount: null,
      statusOptions: TRANSACTION_STATUS_OPTIONS,
      form: {
        status: null,
        category: null,
        account: null,
        initialDate: null,
        finalDate: null
      }
    }
  },
  validations: {
    form: {
      initialDate: { required },
      finalDate: { required }
    }
  },
  mounted () {
    this.form.initialDate = this.initialDate
    this.form.finalDate = this.finalDate

    this.loadAccountList().catch(error => {
      console.warn(error)
      AlertService.error({})
    })

    this.loadCategories('all').catch(error => {
      console.warn(error)
      AlertService.error({})
    })
  }
}
</script>
