<template>
  <div v-if="accountList.length > 0">
    <loading :active.sync="isLoading" />

    <div class="d-flex justify-content-end mb-3">
      <b-button
        size="lg"
        class="filter"
        v-b-tooltip.hover.left="'Filtrar'"
        variant="light"
        @click="openFilterFormModal"
      >
        <b-icon icon="funnel" aria-label="Help"></b-icon>
      </b-button>
    </div>

    <FilterFormModal
      ref="filter-form-modal"
      :initial-date="this.initialDate"
      :final-date="this.finalDate"
      v-on:updateDates="updateDates"
    />

    <SummaryHeaderCard
      v-show="transactionSummary"
      :transaction-summary="transactionSummary"
    />

    <header>
      <div class="d-flex d-flex justify-content-evenly align-items-center month">
        <button class="btn" @click="previousMonth">
          <i class="bi bi-chevron-left fs-5"></i>
        </button>
        <h4 :class="`text-primary text-capitalize fw-bold m-0 ${isFiltered ? 'fs-5' : ''}`" v-text="periodText()"></h4>
        <button class="btn" @click="nextMonth">
          <i class="bi bi-chevron-right fs-5"></i>
        </button>
      </div>
    </header>

    <TransactionList
      :transaction-summary="transactionSummary"
      v-on:openTransactionFormModal="openTransactionFormModal"
      v-on:reloadTransactionSummary="reloadTransactionSummary"
    />

    <!-- <p v-show="emptyFilteredTransaction && !isLoading">Nenhuma transação encontrada para "{{ query }}".</p> -->
    <p v-show="emptyTransaction && !isLoading" class="text-center">Nenhuma transação encontrada para o período.</p>

    <TransactionFormModal
      ref="transaction-form-modal"
      v-on:loadTransactionSummary="reloadTransactionSummary"
    />

    <vue-fab
      :mainBtnColor="mainBtnColor"
      :icon="mainBtnIcon"
      :size="mainBtnSize"
      :scrollAutoHide="false"
      :class="mainBtnClass"
    >
      <fab-item v-for="(item, idx) in menu" :key="idx"
        :idx="idx"
        :title="item.title"
        :color="item.color"
        :icon="item.icon"
        @clickItem="openTransactionFormModal(null, item.transactionType)"
      />
    </vue-fab>
  </div>
  <div class="container-centered" v-else>
    <h3>Ops!</h3>
    <p>Nenhuma conta registrada ou todas estão desativadas.</p>
    <b-button
      pill
      variant="purple"
      size="lg"
      @click.stop="redirectToAccount"
    >VERIFICAR CONTAS</b-button>
  </div>
</template>

<script>
import Loading from 'vue-loading-overlay'
import { mapActions, mapGetters } from 'vuex'
import AlertService from '@helpers/AlertService'
import SummaryHeaderCard from '../Cards/SummaryHeaderCard'
import TransactionList from '../List/TransactionList'
import FilterFormModal from '../Modals/FilterFormModal'
import TransactionFormModal from '../Modals/TransactionFormModal'
import {
  ACCOUNT_URLS_CONSTANTS,
  ACCOUNT_STORE_CONSTANTS
} from '@account/constants'
import {
  TRANSACTION_TYPE,
  TRANSACTION_SUMMARY_STORE_CONSTANTS as C
} from '@transaction/constants'

export default {
  name: 'TransactionListWrapper',
  components: {
    Loading,
    SummaryHeaderCard,
    TransactionList,
    TransactionFormModal,
    FilterFormModal
  },
  computed: {
    ...mapGetters(ACCOUNT_STORE_CONSTANTS.MODULE_NAME, {
      accountList: ACCOUNT_STORE_CONSTANTS.GETTERS.GET_LIST,
      IsLoadingAccountList: ACCOUNT_STORE_CONSTANTS.GETTERS.IS_LOADING
    }),
    ...mapGetters(C.MODULE_NAME, {
      transactionSummary: C.GETTERS.GET_TRANSACTION_SUMMARY,
      isFiltered: C.GETTERS.IS_FILTERED,
      isLoading: C.GETTERS.IS_LOADING
    }),
    emptyTransaction () {
      return this.transactionSummary ? !this.transactionSummary.dailyBalances.length > 0 && !this.query : false
    },
    emptyFilteredTransaction () {
      return this.transactionSummary ? !this.transactionSummary.dailyBalances.length > 0 && this.query.length > 0 : null
    }
  },
  methods: {
    ...mapActions(ACCOUNT_STORE_CONSTANTS.MODULE_NAME, ['loadAccountList']),
    ...mapActions(C.MODULE_NAME, ['loadTransactionSummary']),
    loadTransaction (initialDate, finalDate = null, query = null) {
      this.loadTransactions({ initialDate, finalDate, query }).catch(error => {
        console.warn(error)
        AlertService.error({})
      })
    },
    filteredTransactionSummary (query) {
      // this.resetExamRequestList()
      // if (filterQuery) this.loadExamRequest(this.profile, this.campaignId, null, filterQuery)
      this.loadTransactionSummary(query)
    },
    reloadTransactionSummary () {
      this.loadTransactionSummary({ initialDate: this.initialDate, finalDate: this.finalDate })
    },
    previousMonth () {
      this.initialDate = new Date(this.initialDate.getFullYear(), this.initialDate.getMonth() - 1, 1)
      this.finalDate = new Date(this.finalDate.getFullYear(), (this.finalDate.getMonth() + 1) - 1, 0)

      this.loadTransactionSummary({ initialDate: this.initialDate, finalDate: this.finalDate })
    },
    nextMonth () {
      this.initialDate = new Date(this.initialDate.getFullYear(), this.initialDate.getMonth() + 1, 1)
      this.finalDate = new Date(this.finalDate.getFullYear(), (this.finalDate.getMonth() + 1) + 1, 0)

      this.loadTransactionSummary({ initialDate: this.initialDate, finalDate: this.finalDate })
    },
    openTransactionFormModal (transaction, transactionType) {
      this.$refs['transaction-form-modal'].open(transaction, transactionType)
    },
    openFilterFormModal () {
      this.$refs['filter-form-modal'].show()
    },
    updateDates (initialDate, finalDate) {
      this.initialDate = initialDate
      this.finalDate = finalDate
    },
    periodText () {
      if (this.isFiltered) {
        return `${this.initialDate.toLocaleString('pt-BR', { dateStyle: 'short' })} - ${this.finalDate.toLocaleString('pt-BR', { dateStyle: 'short' })}`
      }
      if (this.initialDate.getYear() === this.today.getYear()) {
        return this.initialDate.toLocaleString('pt-BR', { month: 'long' })
      } else {
        return this.initialDate.toLocaleString('pt-BR', { month: 'long', year: 'numeric' })
      }
    },
    // isLoading () {
    // return false // this.IsLoadingAccountList || this.isLoadingTransactionSummary
    // },
    redirectToAccount () {
      window.location.href = ACCOUNT_URLS_CONSTANTS.ACCOUNT_LIST_URL
    }
  },
  data () {
    return {
      query: '',
      initialDate: null,
      finalDate: null,
      today: new Date(),
      menu: [
        {
          icon: 'fs-5 bi bi-graph-up-arrow',
          title: 'Receita',
          color: '#198754',
          transactionType: TRANSACTION_TYPE.INCOME
        },
        {
          icon: 'fs-5 bi bi-graph-down-arrow',
          title: 'Despesa',
          color: '#ab3c3a',
          transactionType: TRANSACTION_TYPE.EXPENSE
        },
        {
          icon: 'fs-5 bi bi-credit-card',
          title: 'Cartão de Crédito',
          color: '#7d48fc',
          transactionType: TRANSACTION_TYPE.CREDIT
        },
        {
          icon: 'fs-5 bi bi-repeat',
          title: 'Transferência',
          color: '#356B8D',
          transactionType: TRANSACTION_TYPE.TRANSFER
        },
        {
          icon: 'fs-5 bi bi-record-circle',
          title: 'Objetivo',
          color: '#EB8F66',
          transactionType: TRANSACTION_TYPE.OBJECTIVE
        }
      ],
      mainBtnColor: '#356B8D',
      mainBtnIcon: 'fs-4 bi bi-plus-lg',
      mainBtnSize: 'big',
      mainBtnClass: 'btn-float'
    }
  },
  created () {
    const date = new Date()
    this.initialDate = new Date(date.getFullYear(), date.getMonth(), 1)
    this.finalDate = new Date(date.getFullYear(), date.getMonth() + 1, 0)

    this.loadAccountList()
    this.loadTransactionSummary({ initialDate: this.initialDate, finalDate: this.finalDate })
  }
}
</script>

<style scoped>
  header {
    margin: 26px 0;
  }

  header .month {
    max-width: 500px;
    left: 50%;
    position: relative;
    transform: translateX(-50%);
  }

  .filter {
    border: 1px solid #ccc !important;
    border-radius: 50% !important;
    width: 50px;
    height: 50px;
  }

  .filter svg {
    position: relative;
    left: 50%;
    transform: translateX(-50%);
  }

  .filter:hover {
    border: 1px solid #ccc !important;
    background-color: #ccc;
  }
</style>
