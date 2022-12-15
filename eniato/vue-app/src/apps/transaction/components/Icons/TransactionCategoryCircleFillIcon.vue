<template>
  <div :class="`circle-fill circle-fill-${ size } bg-${ isCredit || isTransfer ? transactionType : 'link'}`">
    <CreditCardIcon :width="18" :height="18" :color="'var(--bright-color)'" v-if="isCredit" />
    <RepeatIcon :width="22" :height="22" :color="'var(--bright-color)'" v-else-if="isTransfer" />
    <b-icon :icon="icon" :width="20" :height="20" :color="'var(--bright-color)'" v-else></b-icon>
  </div>
</template>

<script>
import {
  CreditCardIcon,
  RepeatIcon
} from '@eniato-icons'

export default {
  name: 'TransactionCategoryCircleFillIcon',
  components: {
    CreditCardIcon,
    RepeatIcon
  },
  computed: {
    isCredit () { return this.transactionType === 'credit' },
    isTransfer () { return this.transactionType === 'transfer' }
  },
  props: {
    transactionType: {
      required: true,
      type: String
    },
    size: {
      type: String,
      deafult: 'md'
    },
    icon: {
      type: String
    }
  }
}
</script>
