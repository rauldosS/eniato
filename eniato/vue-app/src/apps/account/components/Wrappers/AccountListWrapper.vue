<template>
  <div>
    <!-- <loading :active.sync="isLoading" /> -->
    teste
  </div>
</template>

<script>
import Loading from 'vue-loading-overlay'
import { mapGetters } from 'vuex';
import { mapActions, mapGetters } from 'vuex'
import AlertService from '@helpers/AlertService'
import AccountList from '../List/AccountList'
import AccountFormModal from '../Modals/AccountFormModal'
// import { ACCOUNT_STORE_CONSTANTS as C } from '@account/constants'


export default {
  name: 'AccountListWrapper',
  components: {
    Loading,
    AccountList
  },
  computed: {
    ...mapGetters(C.MODULE_NAME, {
        accountList: C.GETTERS.GET_LIST
    })
  },
  methods: {
    ...mapActions(C.MODULE_NAME, ['loadAccountList']),
    loadAccount (initialDate, finalDate = null, query = null) {
      this.loadAccountList({ initialDate, finalDate, query }).catch(error => {
        console.warn(error)
        AlertService.error({})
      })
    },
    // showCreateAccountFormModal (AccountType) {
    //   this.$refs['form-modal'].show(AccountType)
    // }
  },
  data () {
    return {
    }
  },
  created () {
    this.loadAccount()
  }
}
</script>
