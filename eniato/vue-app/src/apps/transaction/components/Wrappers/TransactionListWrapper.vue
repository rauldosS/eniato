<template>
  <div>
    <loading :active.sync="isLoading" />
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
      :transaction-list="transactionList"
    />
    <p v-show="emptyFilteredTransaction && !isLoading">Nenhuma transação encontrada para "{{ query }}".</p>
    <p v-show="emptyTransaction && !isLoading">Nenhuma transação encontrada.</p>

    <CreateTransactionFormModal ref="form-modal" />

    <!-- <fab-item color="green" @clickItem="showCreateTransactionFormModal" :idx="0" title="Receita" class="bi bi-plus-lg" /> -->

    <vue-fab
      :mainBtnColor="mainBtnColor"
      :icon="mainBtnIcon"
      :size="mainBtnSize"
      :scrollAutoHide="false"
    >
      <fab-item v-for="(item, idx) in menu" :key="idx"
        :idx="idx"
        :title="item.title"
        :color="item.color"
        :icon="item.icon"
        @clickItem="showCreateTransactionFormModal(item.transactionType)"
      />
    </vue-fab>
  </div>
</template>

<script>
import Loading from 'vue-loading-overlay'
import { mapActions, mapGetters } from 'vuex'
import AlertService from '@helpers/AlertService'
import TransactionList from '../List/TransactionList'
import CreateTransactionFormModal from '../Modals/CreateTransactionFormModal'
import {
  TRANSACTION_TYPE,
  TRANSACTION_STORE_CONSTANTS as C
} from '@transaction/constants'

export default {
  name: 'TransactionListWrapper',
  components: {
    Loading,
    TransactionList,
    CreateTransactionFormModal
  },
  computed: {
    ...mapGetters(C.MODULE_NAME, {
      transactionList: C.GETTERS.GET_LIST,
      isLoading: C.GETTERS.LIST_IS_LOADING
    }),
    emptyTransaction () {
      return !this.transactionList.length > 0 && !this.query
    },
    emptyFilteredTransaction () {
      return !this.transactionList.length > 0 && this.query.length > 0
    }
  },
  methods: {
    ...mapActions(C.MODULE_NAME, ['loadTransactionList']),
    loadTransaction (initialDate, finalDate = null, query = null) {
      this.loadTransactionList({ initialDate, finalDate, query }).catch(error => {
        console.warn(error)
        AlertService.error({})
      })
    },
    filteredTransactionList (query) {
      this.loadTransaction(query)
    },
    showCreateTransactionFormModal (transactionType) {
      this.$refs['form-modal'].show(transactionType)
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
        }
      ],
      mainBtnColor: '#356B8D',
      mainBtnIcon: 'fs-4 bi bi-plus-lg',
      mainBtnSize: 'big'
    }
  },
  created () {
    const date = new Date()
    this.initialDate = new Date(date.getFullYear(), date.getMonth(), 1)
    this.finalDate = new Date(date.getFullYear(), date.getMonth() + 1, 0)

    this.loadTransaction(this.initialDate, this.finalDate)
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

  .fab-item {
    padding-top: 10px;
  }
</style>
