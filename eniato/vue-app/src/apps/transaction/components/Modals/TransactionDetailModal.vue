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
        <b-button variant="white" v-if="transaction.status">
          <div class="circle-fill bg-success">
            <CheckIcon :width="20" :height="20" :color="'var(--bright-color)'"/>
          </div>
          <span>Foi paga</span>
        </b-button>
        <b-button variant="white" v-else>
          <div class="circle-fill bg-danger">
            <PinAngleIcon :width="18" :height="18" :color="'var(--bright-color)'"/>
          </div>
          <span>Não foi paga</span>
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
            <span v-text="currencyFormat(transaction.value)"></span>
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
            <span>Nenhuma tag</span>
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
        <b-button pill class="shadow" variant="danger" @click.stop="deleteTransaction" v-text="confirmDelete ? 'CLIQUE PARA CONFIRMAR' : 'APAGAR'"></b-button>
        <b-button pill class="shadow" variant="primary" @click.stop="openTransactionFormModal">EDITAR</b-button>
      </div>
    </b-modal>
  </div>
</template>

<script>
import { mapActions } from 'vuex'
import {
  CheckIcon,
  PinAngleIcon
} from '@eniato-icons'
import TransactionTypeCircleFillIcon from '../Icons/TransactionTypeCircleFillIcon'
import Formatter from '@helpers/Formatter'
import { TRANSACTION_STORE_CONSTANTS as C } from '@transaction/constants'

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
      isLoading: false,
      confirmDelete: false
    }
  },
  methods: {
    ...mapActions(C.MODULE_NAME, ['delete']),
    open (transaction) {
      this.transaction = transaction
      this.show()
    },
    show () {
      this.$refs['transaction-detail-modal'].show()
    },
    hide () {
      this.$refs['transaction-detail-modal'].hide()
    },
    openTransactionFormModal () {
      this.$emit('open-transaction-modal-form')
    },
    currencyFormat (money) {
      return Formatter.currency(money)
    },
    deleteTransaction () {
      if (this.confirmDelete) {
        this.delete(this.transaction).then(() => {
          this.$emit('reload-transacton-summary')
          this.hide()
        })
      } else {
        this.confirmDelete = true
        setTimeout(() => {
          this.confirmDelete = false
        }, 2000)
      }
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
