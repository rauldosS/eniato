<template>
  <div class="d-flex flex-column align-items-center mt-5">
    <b-button
      pill
      v-for="item in menu"
      :key="item.name"
      :variant="item.variant"
      :href="item.url"
      :disabled="item.disabled"
    >
      <b-icon
        :icon="item.icon"
        aria-hidden="true"
        variant="light">
      </b-icon> {{ item.name }}
    </b-button>
  </div>
</template>

<script>
export default {
  name: 'IndexWrapper',
  data () {
    return {
      menu: [
        {
          name: 'Contas',
          disabled: false,
          variant: 'primary',
          icon: 'wallet2',
          url: '/contas'
        },
        {
          name: 'Cartão de crédito',
          disabled: true,
          variant: 'primary',
          icon: 'credit-card',
          url: '/contas'
        },
        {
          name: 'Categorias',
          disabled: false,
          variant: 'primary',
          icon: 'bookmarks',
          url: '/categorias'
        },
        {
          name: 'Tags',
          disabled: true,
          variant: 'primary',
          icon: 'tags',
          url: '/contas'
        },
        {
          name: 'Sair',
          disabled: false,
          variant: 'danger',
          icon: 'box-arrow-left',
          url: '/accounts/logout'
        }
      ]
    }
  }
}
</script>

<style scoped>
a {
    width: 300px;
    height: 48px;
    margin-bottom: 8px;
    display: flex;
    align-items: center !important;
    justify-content: flex-start !important;
    padding: 0 2rem;
}

a svg {
    margin-right: 0.6rem;
}
</style>
