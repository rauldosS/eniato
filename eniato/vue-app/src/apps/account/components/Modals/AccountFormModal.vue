<template>
  <b-modal
    ref="account-form-modal"
    :title="account ? 'Editar Conta' : 'Nova Conta'"
    ok-title="Fechar"
    @ok="hide"
    @close="hide"
    size="md"
    centered
  >
    <AccountForm
      class="mx-4"
      ref="account-form"
      :account="account"
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
import AccountForm from '../Forms/AccountForm'

export default {
  components: {
    AccountForm
  },
  methods: {
    open (account) {
      this.account = account
      this.show()
    },
    show () {
      this.$refs['account-form-modal'].show()
    },
    hide () {
      this.$refs['account-form-modal'].hide()
    },
    save () {
      this.$refs['account-form'].tryToSubmit().then(valid => valid ? this.hide() : null)
    }
  },
  data () {
    return {
      account: null
    }
  }
}
</script>
