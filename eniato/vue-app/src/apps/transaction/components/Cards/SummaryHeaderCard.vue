<template>
  <div>
    <b-card-group deck class="d-flex justify-content-between">
      <b-card>
        <div class="d-flex justify-content-between">
          <div class="">
            <span>Saldo atual</span>
            <div class="value" v-text="periodBalance"></div>
          </div>
          <div class="blue color">
            <b-icon icon="bank" variant="white"></b-icon>
          </div>
        </div>
      </b-card>
      <b-card
        v-b-tooltip.hover.html.bottom="totalExpectedIncome"
      >
        <div class="d-flex justify-content-between">
          <div class="">
            <span>Receitas</span>
            <div class="value" v-text="totalIncome"></div>
          </div>
          <div class="green color">
            <b-icon icon="arrow-up" variant="white"></b-icon>
          </div>
        </div>
      </b-card>
      <b-card
        v-b-tooltip.hover.html.bottom="totalExpectedExpense"
      >
        <div class="d-flex justify-content-between">
          <div class="">
            <span>Despesas</span>
            <div class="value" v-text="totalExpense"></div>
          </div>
          <div class="red color">
            <b-icon icon="arrow-down" variant="white"></b-icon>
          </div>
        </div>
      </b-card>
      <b-card
        v-b-tooltip.hover.html.bottom="expectedBalance"
      >
        <div class="d-flex justify-content-between">
          <div class="">
            <span>Balanço do período</span>
            <div class="value" v-text="balance"></div>
          </div>
          <div class="purple color">
            <b-icon icon="currency-dollar" variant="white"></b-icon>
          </div>
        </div>
      </b-card>
    </b-card-group>
  </div>
</template>

<script>
import Formatter from '@helpers/Formatter'

export default {
  props: {
    transactionSummary: Object
  },
  computed: {
    periodBalance () {
      return this.transactionSummary ? Formatter.currency(this.transactionSummary.periodBalance) : 'R$ 0,00'
    },
    totalIncome () {
      return this.transactionSummary ? Formatter.currency(this.transactionSummary.totalIncome) : 'R$ 0,00'
    },
    totalExpense () {
      return this.transactionSummary ? Formatter.currency(this.transactionSummary.totalExpense) : 'R$ 0,00'
    },
    balance () {
      return this.transactionSummary ? Formatter.currency(this.transactionSummary.balance) : 'R$ 0,00'
    },
    totalExpectedIncome () {
      return this.transactionSummary ? `<b>Receitas previstas:</b> ${Formatter.currency(this.transactionSummary.totalExpectedIncome)}` : 'R$ 0,00'
    },
    totalExpectedExpense () {
      return this.transactionSummary ? `<b>Despesas previstas:</b> ${Formatter.currency(this.transactionSummary.totalExpectedExpense)}` : 'R$ 0,00'
    },
    expectedBalance () {
      return this.transactionSummary ? `<b>Balanço previsto:</b> ${Formatter.currency(this.transactionSummary.expectedBalance)}` : 'R$ 0,00'
    }
  }
}
</script>

<style scoped>
.card {
  width: 24%;
  height: 85px;
  padding: 0 0 0 .5rem;
}

.card .value {
  font-size: 22px;
  font-weight: bold;
  color: var(--primary-color);
}

.color {
  width: 2.5rem;
  height: 2.5rem;
  font-size: 18px;
  margin-right: 0;
}
</style>
