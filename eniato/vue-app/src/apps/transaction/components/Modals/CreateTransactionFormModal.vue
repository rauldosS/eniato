<template>
  <b-modal
    ref="form-modal"
    title="Nova Transação"
    ok-title="Fechar"
    @ok="hide"
    @close="hide"
    size="lg"
    centered
  >
    <CreateTransactionForm
      :transactionType="transactionType"
      class="mx-4"
      ref="create-transaction-form"
    />
    <template v-slot:modal-footer>
      <button @click="hide" class="button alternative-button">Fechar</button>
      <button
        type="submit"
        form="change-responsible-for-the-task-form"
        class="button primary-button"
        @click.prevent="save"
      >
        Salvar
      </button>
    </template>
  </b-modal>
</template>

<script>
import CreateTransactionForm from '../Forms/CreateTransactionForm'

export default {
  props: {
  },
  components: {
    CreateTransactionForm
  },
  methods: {
    show (transactionType) {
      this.transactionType = transactionType
      this.$refs['form-modal'].show()
    },
    hide () {
      this.$refs['form-modal'].hide()
    },
    save () {
      this.$refs['create-transaction-form'].tryToSubmit().then(valid => valid ? this.hide() : null)
    }
  },
  data () {
    return {
      transactionType: null
    }
  }
}
</script>
