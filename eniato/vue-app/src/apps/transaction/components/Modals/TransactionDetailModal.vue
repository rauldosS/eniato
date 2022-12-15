<template>
  <div>
    <b-modal
      ref="transaction-detail-modal"
      header-bg-variant="light"
      header-text-variant="dark"
      size="md"
      centered
      hide-header
      hide-footer
    >
      <!-- Header -->
      <div class="detail d-flex justify-content-around">
        <b-button variant="white" v-if="true">
          <div class="circle-fill bg-success">
            <CheckIcon :width="20" :height="20" :color="'var(--bright-color)'"/>
          </div>
          <span>Foi pago</span>
        </b-button>
        <b-button variant="white" v-else>
          <div class="circle-fill bg-danger">
            <PinAngleIcon :width="18" :height="18" :color="'var(--bright-color)'"/>
          </div>
          <span>Não foi pago</span>
        </b-button>

        <b-button variant="white">
          <TransactionTypeCircleFillIcon
            :transactionType="transaction.transactionType"
          />
          <span>{{ transaction.transactionTypeDisplayName }}</span>
        </b-button>
      </div>

      <hr>

      <!-- Detalhes -->
      <div class="details row">
        <div class="col-6 detail">
          <b-icon icon="file-earmark-text" class="fs-5"></b-icon>
          <div>
            <label>Descrição</label>
            <span>{{ this.transaction.description }}</span>
          </div>
        </div>
        <div class="col-6 detail">
          <b-icon icon="wallet2" class="fs-5"></b-icon>
          <div>
            <label>Valor</label>
            <span>{{ transaction.value }}</span>
          </div>
        </div>

        <div class="col-6 detail">
          <b-icon icon="calendar-check" class="fs-5"></b-icon>
          <div>
            <label>Data</label>
            <span>{{ transaction.description }}</span>
          </div>
        </div>
        <div class="col-6 detail">
          <img :src="transaction.account.financialInstitution.logo" class="logo-financial-institution-sm">
          <div>
            <label>Conta</label>
            <span>{{ transaction.account.description }}</span>
          </div>
        </div>

        <div class="col-6 detail">
          <b-icon icon="pin-angle" class="fs-5"></b-icon>
          <div>
            <label>Categoria</label>
            <span>{{ transaction.category.name }}</span>
          </div>
        </div>
        <div class="col-6 detail">
          <b-icon icon="tags" class="fs-5"></b-icon>
          <div>
            <label>Tags</label>
            <span>Nenhuma atg</span>
          </div>
        </div>

        <div class="col-6 detail">
          <b-icon icon="pencil" class="fs-5"></b-icon>
          <div>
            <label>Observações</label>
            <span>Nenhuma</span>
          </div>
        </div>
      </div>

      <div class="btn-group">
        <b-button pill class="shadow" variant="primary">EDITAR</b-button>
        <b-button pill class="shadow" variant="success" v-if="!transaction.status">PAGAR</b-button>
      </div>
    </b-modal>
  </div>
</template>

<script>
import {
  CheckIcon,
  PinAngleIcon
} from '@eniato-icons'
import TransactionTypeCircleFillIcon from '../Icons/TransactionTypeCircleFillIcon'

export default {
  name: 'TransactionDetailModal',
  components: {
    // Loading,
    TransactionTypeCircleFillIcon,
    CheckIcon,
    PinAngleIcon
  },
  props: {
    transaction: {
      type: Object,
      required: true
    }
  },
  data () {
    return {
      isLoading: false
    }
  },
  methods: {
    show (transaction) {
      this.$refs['transaction-detail-modal'].show()
    },
    hide () {
      this.$refs['transaction-detail-modal'].hide()
    }
  }
}
</script>

<style scoped>
label {
  opacity: .65;
  font-size: 14px;
}

.detail {
  display: flex;
  margin-bottom: 12px;
}

.detail label {
  width: 100%;
}

.details svg, .details img {
  margin: 6px 8px;
}

.block-button {
  width: 100%;
}

.btn-group {
  display: flex;
}

.btn-group button {
  margin: 12px;
}
</style>
