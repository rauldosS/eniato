<template>
  <div>
    <loading :active.sync="isLoading" />
    <div class="py-3 text-center" v-if="accountList.length > 0">
      <h1 class="display-4">Todas as contas</h1>
      <p class="lead">Cadastre todas as suas contas bancárias aqui.</p>
    </div>
    <div class="container-centered" v-else>
      <h3>Ops!</h3>
      <p>Sem contas criadas até o momento.</p>
      <b-button
        pill
        variant="purple"
        size="lg"
        @click.stop="openAccountFormModal(null)"
      >ADICIONAR CONTA</b-button>
    </div>

    <AccountList
      :account-list="accountList"
      v-on:openAccountFormModal="openAccountFormModal"
      v-on:openDeleteAccountModal="openDeleteAccountModal"
    />

    <AccountFormModal ref="account-form-modal"/>
    <DeleteAccountModal ref="delete-account-modal"/>

    <b-button
      size="lg"
      variant="primary"
      class="btn-float"
      @click.stop="openAccountFormModal(null)"
    >
      <b-icon icon="plus"></b-icon>
    </b-button>
  </div>
</template>

<script>
import Loading from 'vue-loading-overlay'
import { mapGetters, mapActions } from 'vuex'
import AlertService from '@helpers/AlertService'
import AccountList from '../List/AccountList'
import AccountFormModal from '../Modals/AccountFormModal'
import DeleteAccountModal from '../Modals/DeleteAccountModal'
import { ACCOUNT_STORE_CONSTANTS as C } from '@account/constants'

export default {
  name: 'AccountListWrapper',
  components: {
    Loading,
    AccountList,
    AccountFormModal,
    DeleteAccountModal
  },
  computed: {
    ...mapGetters(C.MODULE_NAME, {
      accountList: C.GETTERS.GET_LIST,
      isLoading: C.GETTERS.IS_LOADING
    })
  },
  methods: {
    ...mapActions(C.MODULE_NAME, ['loadAccountList']),
    openAccountFormModal (account) {
      this.$refs['account-form-modal'].open(account)
    },
    openDeleteAccountModal (account) {
      this.$refs['delete-account-modal'].open(account)
    }
  },
  created () {
    this.loadAccountList().catch(error => {
      console.warn(error)
      AlertService.error({})
    })
  }
}
</script>
