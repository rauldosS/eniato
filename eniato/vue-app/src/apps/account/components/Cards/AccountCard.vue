<template>
  <div class="col-md-6">
    <div class="card shadow-sm border-0 mb-4">
      <div class="card-header d-flex bg-transparent border-0">
        <img :src="account.financialInstitution.logo" class='logo-financial-institution'>
        <div class="fs-5 ms-2">
          <span class="align-middle">{{ account.description }}</span>
        </div>
        <div class="ms-auto">
          <div class="dropdown">
            <a class="" id="dropdown-account" data-bs-toggle="dropdown" aria-expanded="false">
              <span class="align-middle">
                <svg xmlns="http://www.w3.org/2000/svg" width="18" height="18" fill="currentColor" class="bi bi-three-dots-vertical mt-2" viewBox="0 0 16 16">
                  <path d="M9.5 13a1.5 1.5 0 1 1-3 0 1.5 1.5 0 0 1 3 0zm0-5a1.5 1.5 0 1 1-3 0 1.5 1.5 0 0 1 3 0zm0-5a1.5 1.5 0 1 1-3 0 1.5 1.5 0 0 1 3 0z"/>
                </svg>
              </span>
            </a>
            <ul class="dropdown-menu" aria-labelledby="dropdown-account">
              <li>
                <button
                  class="dropdown-item"
                  href=""
                >
                  Detalhes
                </button>
              </li>
              <li>
                <button
                  class="dropdown-item"
                  @click.stop="openAccountFormModal(account)"
                >
                  Editar
                </button>
              </li>
              <li>
                <button
                  class="dropdown-item"
                  @click.stop="openDeleteAccountModal(account)"
                >
                  Apagar
                </button>
              </li>
            </ul>
          </div>
        </div>
      </div>
      <div class="card-body">
        <div class="d-flex justify-content-between align-items-center">
          <p class="text-muted">Saldo atual</p>
          <p class="text-muted" v-text="maskMoney(account.openingBalance)"></p>
        </div>
        <div class="d-flex justify-content-between align-items-center">
          <p class="text-muted">Tipo de conta</p>
          <p class="text-muted">NÃO ESTÁ EXIBINDO CORRETAMENTE!</p>
        </div>
      </div>
      <div class="account-default" v-if="account.default">
        Conta padrão
      </div>
    </div>
  </div>
</template>

<script>
import Mask from '@helpers/Mask'

export default {
  name: 'AccountCard',
  components: {
  },
  props: ['account'],
  methods: {
    maskMoney (money) {
      return Mask.money(money)
    },
    openAccountFormModal (account) {
      this.$emit('open-account-modal-form', account)
    },
    openDeleteAccountModal (account) {
      this.$emit('open-delete-account-modal', account)
    }
  }
}
</script>

<style scoped>
.account-default {
  position: absolute;
  left: 50%;
  bottom: 0;
  padding: 2px 0;
  width: 100%;
  transform: translate(-50%);
  background: linear-gradient(to right, #356B8D 0%, #E63888 100%);
  font-size: 12px;
  text-align: center;
  font-weight: lighter;
  color: var(--bright-color);
  border-radius: 0 0 18px 18px;
}
</style>
