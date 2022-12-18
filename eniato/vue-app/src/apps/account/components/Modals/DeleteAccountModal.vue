<template>
  <b-modal
    ref="delete-account-modal"
    title="Apagar conta"
    ok-title="Fechar"
    @ok="hide"
    @close="hide"
    size="md"
    centered
  >
    <div>
      <p>Ao apagar sua conta todas as transações vinculadas à mesma serão deletadas.</p>
      <p class="text-center">
        <b>Lembra-se, esta ação é irreversível.</b>
      </p>
    </div>
    <template v-slot:modal-footer>
      <button @click="hide" class="button alternative-button">Fechar</button>
      <button
        type="submit"
        class="button danger-button"
        @click.prevent="deleteAccount"
      >
        Apagar
      </button>
    </template>
  </b-modal>
</template>

<script>
import { mapActions } from 'vuex'
import { ACCOUNT_STORE_CONSTANTS as C } from '@account/constants'

export default {
  methods: {
    ...mapActions(C.MODULE_NAME, ['delete']),
    open (account) {
      this.account = account
      this.show()
    },
    show () {
      this.$refs['delete-account-modal'].show()
    },
    hide () {
      this.$refs['delete-account-modal'].hide()
    },
    deleteAccount () {
      this.delete(this.account)
    }
  }
}
</script>
