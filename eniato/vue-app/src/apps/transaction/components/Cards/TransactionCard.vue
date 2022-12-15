<template>
  <div @click="openTransactionDetailModal" class="card d-flex border-0 clickable-card">
    <div class="h2 m-0 d-flex justify-content-center align-items-center pe-2">
      <TransactionCategoryCircleFillIcon
        :transactionType="transaction.transactionType"
        :icon="transaction.category.icon"
        size="lg"
      />
    </div>
    <div class="first-column">
      <h3 class="fw-bold">
        {{ transaction.description }}
      </h3>
      <div class="">
        <b-icon :icon="transaction.category.icon"></b-icon> {{ transaction.category.name }}
        <span>| {{ transaction.account.name }} </span>
        <span v-if="transaction.fixed">| Fixa</span>
      </div>
    </div>
    <div class="second-column ms-auto m-0 justify-content-center align-items-end">
      <h4
        :class="transaction.isExpense
          ? 'text-danger fw-bold'
          : 'text-success fw-bold'"
      >
        R$ {{ transaction.value }}
      </h4>
      <div class="d-flex align-items-center justify-content-center">
        <b-badge pill class="text-muted" :variant="transaction.status ? 'light-sucess' : 'light-danger'" v-text="transaction.status ? 'Pago' : 'Não pago'"></b-badge>
        <b-icon icon="check2-circle" :width="16" :height="16" :color="'rgba(var(--bs-success-rgb)'" v-if="transaction.status"></b-icon>
        <b-icon icon="exclamation-circle" :width="16" :height="16" :color="'var(--danger)'" v-else></b-icon>
      </div>
    </div>

    <TransactionDetailModal
      ref="transaction-detail-modal"
      :transaction="transaction"
    />
  </div>
</template>

<script>
import TransactionDetailModal from '../Modals/TransactionDetailModal'
import TransactionCategoryCircleFillIcon from '../Icons/TransactionCategoryCircleFillIcon'

export default {
  name: 'TransactionCard',
  components: {
    TransactionDetailModal,
    TransactionCategoryCircleFillIcon
  },
  props: ['transaction'],
  methods: {
    openTransactionDetailModal () {
      this.$refs['transaction-detail-modal'].show()
    }
  }
}
</script>

<style scoped>
.card {
  border-radius: 18px;
}

.card-title {
  font-size: 1.5rem;
  font-weight: bold;
  margin: 0;
}

.first-column {
  display: flex;
  flex-direction: column;
}

.top-right-data {
  position: absolute;
  top: 0;
  right: 0;
  display: flex;
  flex-direction: row;
  justify-content: center;
  border-bottom-left-radius: 20px;
  border-top-right-radius: 8px;
}

.scheduled-icon {
  align-self: center;
  padding: 4px 14px;
  background-color: var(--elemental-color-2-light);
  color: #ffffff;
  font-weight: bold;
  border-bottom-left-radius: 18px;
  border-top-right-radius: 18px;
  font-size: 18px;
}

.status {
  align-self: center;
  font-weight: bold;
  color: white;
  padding: 4px 14px;
  text-transform: uppercase;
}

.card {
  display: flex;
  flex-direction: row;
  justify-content: space-between;
  color: inherit;
}

.second-column {
  display: flex;
  flex-direction: column;
  padding-top: 0px;
  align-items: flex-start;
}

.comment-notification {
  background-color: var(--highlight-color);
  border-radius: 100%;
  height: 8px;
  width: 8px;
  position: absolute;
  top: 4px;
  right: 2px;
}

.custom-number-tag-text {
  font-size: 14px;
  white-space: nowrap;
}

.custom-number-tag-number {
  width: 32px;
  height: 32px;
  font-size: 18px;
}
</style>
