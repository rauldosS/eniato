<template>
  <b-modal
    ref="transaction-form-modal"
    :title="modalTitle()"
    ok-title="Fechar"
    @ok="hide"
    @close="hide"
    size="md"
    centered
  >
    <SimpleTransactionForm
      :transaction="transaction"
      :transactionType="transactionType"
      class="mx-4"
      ref="transaction-form"
      v-if="[transactionTypes.INCOME, transactionTypes.EXPENSE].includes(transactionType)"
    />
    <template v-slot:modal-footer>
      <button @click="hide" class="button alternative-button">Fechar</button>
      <button
        type="submit"
        class="button primary-button"
        @click.prevent="save"
      >
        Salvar
      </button>
    </template>
  </b-modal>
</template>

<script>
import SimpleTransactionForm from '../Forms/SimpleTransactionForm'
import { TRANSACTION_TYPE } from '@transaction/constants'

export default {
  components: {
    SimpleTransactionForm
  },
  methods: {
    open (transaction, transactionType) {
      this.transaction = transaction
      this.transactionType = transactionType
      this.show()
    },
    show () {
      this.$refs['transaction-form-modal'].show()
    },
    hide () {
      this.$refs['transaction-form-modal'].hide()
    },
    save () {
      this.$refs['transaction-form'].tryToSubmit().then(valid => {
        if (valid) {
          this.$emit('loadTransactionSummary')
          this.hide()
        }
        return null
      })
    },
    modalTitle () {
      const transactionTypeDisplayName = 'Transação'
      const action = this.transaction ? 'Editar' : 'Nova'
      return `${action} ${transactionTypeDisplayName}`
    }
  },
  data () {
    return {
      transaction: null,
      transactionType: null,
      transactionTypes: TRANSACTION_TYPE
    }
  }
}
</script>
