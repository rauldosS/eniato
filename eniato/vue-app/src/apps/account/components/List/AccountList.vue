<template>
  <div class="row">
    <AccountCard
      v-for="account in accountList"
      :key="account.id"
      :account="account"
      @open-account-modal-form="openAccountFormModal"
      @open-delete-account-modal="openDeleteAccountModal"
    />
  </div>
</template>

<script>
import AccountCard from '../Cards/AccountCard'

export default {
  name: 'AccountList',
  components: {
    AccountCard
  },
  props: {
    accountList: Array
  },
  methods: {
    openAccountFormModal (account) {
      this.$emit('openAccountFormModal', account)
    },
    openDeleteAccountModal (account) {
      this.$emit('openDeleteAccountModal', account)
    }
  }
}
</script>

<style scoped>
</style>
