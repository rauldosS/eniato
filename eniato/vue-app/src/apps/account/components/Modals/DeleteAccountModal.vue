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
      <p class="text-center">Ao apagar uma conta, todas as despesas, receitas, cartões e transferências associadas serão apagadas juntamente.</p>
    </div>
    <template v-slot:modal-footer>
      <button @click="hide" class="button alternative-button">Fechar</button>
      <button
        type="submit"
        class="button danger-button"
        @click.prevent="deleteAccount"
        v-text="confirmDelete ? 'CLIQUE PARA CONFIRMAR' : 'Apagar'"
      ></button>
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
      if (this.confirmDelete) {
        this.delete(this.account).then(() => {
          this.hide()
        })
      } else {
        this.confirmDelete = true
        setTimeout(() => {
          this.confirmDelete = false
        }, 2000)
      }
    }
  },
  data () {
    return {
      confirmDelete: false
    }
  }
}
</script>
