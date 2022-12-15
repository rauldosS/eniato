<template>
  <div>
    <!-- <loading :active.sync="isLoading" /> -->
    <div
      v-for="referenceDate in transactionList"
      :key="referenceDate.day"
    >
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
      <div class="d-flex justify-content-between alert">
        <span>Saldo previsto final do dia</span>
        <span >R$ {{ referenceDate.balance }}</span>
      </div>
    </div>
  </div>
</template>

<script>
import { ListTransition } from '@eniato-ui'
// import Loading from 'vue-loading-overlay'
import DayTransactionList from '../List/DayTransactionList'
import TransactionCard from '../Cards/TransactionCard'

export default {
  name: 'TransactionList',
  components: {
    // Loading,
    ListTransition,
    TransactionCard,
    DayTransactionList
  },
  props: {
    transactionList: Array
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

  .alert {
    margin-left: 4rem !important;
  }

  .transaction-list {
    padding: 1rem 0 0 0!important;
  }
</style>
