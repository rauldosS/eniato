<template>
  <div>
    <loading :active.sync="isLoading" />

    <SummaryHeaderCard
      v-show="transactionSummary"
      :transaction-summary="transactionSummary"
    />

    <header>
      <div class="d-flex d-flex justify-content-evenly align-items-center month">
        <div class="">
          <i class="bi bi-chevron-left fs-5"></i>
        </div>
        <h4 class="text-primary text-capitalize fw-bold m-0">{{ initialDate.toLocaleString('pt-BR', { month: 'long' }) }}</h4>
        <div class="">
          <i class="bi bi-chevron-right fs-5"></i>
        </div>
      </div>
    </header>

    <TransactionList
      :transaction-summary="transactionSummary"
    />
    <!-- transactionSummary.dailyBalances -->

    <!-- <p v-show="emptyFilteredTransaction && !isLoading">Nenhuma transação encontrada para "{{ query }}".</p> -->
    <!-- <p v-show="emptyTransaction && !isLoading">Nenhuma transação encontrada para o período.</p> -->

    <TransactionFormModal ref="form-modal" />

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
</template>

<script>
import Loading from 'vue-loading-overlay'
import { mapActions, mapGetters } from 'vuex'
import AlertService from '@helpers/AlertService'
import SummaryHeaderCard from '../Cards/SummaryHeaderCard'
import TransactionList from '../List/TransactionList'
import TransactionFormModal from '../Modals/TransactionFormModal'
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
    TransactionFormModal
  },
  computed: {
    ...mapGetters(C.MODULE_NAME, {
      transactionSummary: C.GETTERS.GET_TRANSACTION_SUMMARY,
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
    openTransactionFormModal (transaction, transactionType) {
      this.$refs['form-modal'].open(transaction, transactionType)
    }
  },
  data () {
    return {
      query: '',
      initialDate: null,
      finalDate: null,
      dateFilterType: 'monthly',
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
</style>
