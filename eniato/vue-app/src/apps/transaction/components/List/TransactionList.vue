<template>
  <div>
    <!-- <loading :active.sync="isLoading" /> -->
    <div
      v-for="referenceDate in dailyBalanceList"
      :key="referenceDate.day"
    >
      <div v-if="referenceDate.transactions.length > 0">
        <div class="d-flex">
          <DayTransactionList
            :day="referenceDate.day"
            :dayOfTheWeek="referenceDate.dayOfTheWeek"
          />
          <hr>
          <list-transition class="ms-3 w-100 transaction-list">
            <TransactionCard
              v-for="transaction in referenceDate.transactions"
              :key="transaction.id"
              :transaction="transaction"
            />
          </list-transition>
        </div>
        <div class="balance">
          <div class="d-flex justify-content-between" v-if="expectedBalance(referenceDate.referenceDate)">
            <span>Saldo previsto do dia</span>
            <span v-text="currencyFormat(referenceDate.expectedBalance)"></span>
          </div>
          <div class="d-flex justify-content-between" v-else>
            <span>Saldo final do dia</span>
            <span v-text="currencyFormat(referenceDate.balance)"></span>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import { ListTransition } from '@eniato-ui'
// import Loading from 'vue-loading-overlay'
import DayTransactionList from '../List/DayTransactionList'
import TransactionCard from '../Cards/TransactionCard'
import Formatter from '@helpers/Formatter'

export default {
  name: 'TransactionList',
  components: {
    // Loading,
    ListTransition,
    TransactionCard,
    DayTransactionList
  },
  props: {
    transactionSummary: Object
  },
  computed: {
    dailyBalanceList () {
      return this.transactionSummary ? this.transactionSummary.dailyBalances : []
    }
  },
  methods: {
    currencyFormat (money) {
      return Formatter.currency(money)
    },
    expectedBalance (referenceDate) {
      return new Date(`${referenceDate}T10:20:30`) >= this.currentDay
    }
  },
  data () {
    return {
      currentDay: new Date()
    }
  }
}
</script>

<style scoped>
  .clickable-card {
    margin: 0 0 16px 0;
  }

  .actions .btn {
    background-color: transparent;
  }

  .balance div {
    margin: 0 0 0 4rem !important;
    padding: 0.4rem 1rem;
  }

  .transaction-list {
    padding: 1rem 0 0 0!important;
  }
</style>
