<template>
  <div>
    <b-card-group deck class="d-flex justify-content-between">
      <b-card v-for="card in cards" :key="card.title">
        <div class="d-flex justify-content-between">
          <div class="">
            <span>{{ card.title }}</span>
            <div class="value">{{ card.value }}</div>
          </div>
          <div :class="`${ card.variant } color`">
            <b-icon :icon="card.icon" variant="white"></b-icon>
          </div>
        </div>
      </b-card>
    </b-card-group>
  </div>
</template>

<script>
export default {
  props: {
  },
  data () {
    return {
      cards: [
        {
          title: 'Saldo atual',
          value: 'R$ 692,72',
          icon: 'bank',
          variant: 'blue'
        },
        {
          title: 'Receitas',
          value: 'R$ 2.210,95',
          icon: 'arrow-up',
          variant: 'green'
        },
        {
          title: 'Despesas',
          value: 'R$ 1.554,18',
          icon: 'arrow-down',
          variant: 'red'
        },
        {
          title: 'Balanço mensal',
          value: 'R$ 656,78',
          icon: 'currency-dollar',
          variant: 'purple'
        }
      ]
    }
  }
}
</script>

<style scoped>
.card {
  width: 24%;
  height: 85px;
  padding: 0 0 0 .5rem;
}

.card .value {
  font-size: 22px;
  font-weight: bold;
  color: var(--primary-color);
}

.color {
  width: 2.5rem;
  height: 2.5rem;
  font-size: 18px;
  margin-right: 0;
}
</style>
