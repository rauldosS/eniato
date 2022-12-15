<template>
  <div :class="`circle-fill circle-fill-${ size } bg-${ transactionType }`">
    <ArrowTrendUpIcon :width="22" :height="22" :color="'var(--bright-color)'" v-if="isIncome"/>
    <ArrowTrendDownIcon :width="22" :height="22" :color="'var(--bright-color)'" v-else-if="isExpense"/>
    <CreditCardIcon :width="18" :height="18" :color="'var(--bright-color)'" v-else-if="isCredit"/>
    <RepeatIcon :width="22" :height="22" :color="'var(--bright-color)'" v-else/>
  </div>
</template>

<script>
import {
  ArrowTrendUpIcon,
  ArrowTrendDownIcon,
  CreditCardIcon,
  RepeatIcon
} from '@eniato-icons'

export default {
  name: 'TransactionTypeCircleFillIcon',
  components: {
    ArrowTrendUpIcon,
    ArrowTrendDownIcon,
    CreditCardIcon,
    RepeatIcon
  },
  computed: {
    isIncome () { return this.transactionType === 'income' },
    isExpense () { return this.transactionType === 'expense' },
    isCredit () { return this.transactionType === 'credit' }
  },
  props: {
    transactionType: {
      required: true,
      type: String
    },
    size: {
      type: String,
      deafult: 'md'
    }
  }
}
</script>
