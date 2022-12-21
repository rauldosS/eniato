<template>
  <b-modal
    ref="filter-form-modal"
    title="Filtros"
    ok-title="Fechar"
    @ok="hide"
    @close="hide"
    size="md"
    centered
  >
    <FilterForm
      class="mx-4"
      ref="filter-form"
      :initial-date="this.initialDate"
      :final-date="this.finalDate"
      @update-dates="updateDates"
    />
    <template v-slot:modal-footer>
      <button @click="hide" class="button alternative-button">Fechar</button>
      <button
        type="submit"
        class="button primary-button"
        @click.prevent="filter"
      >
        Salvar
      </button>
    </template>
  </b-modal>
</template>

<script>
import FilterForm from '../Forms/FilterForm'

export default {
  components: {
    FilterForm
  },
  props: {
    initialDate: Date,
    finalDate: Date
  },
  methods: {
    show () {
      this.$refs['filter-form-modal'].show()
    },
    hide () {
      this.$refs['filter-form-modal'].hide()
    },
    filter () {
      this.$refs['filter-form'].tryToSubmit().then(valid => valid ? this.hide() : null)
    },
    updateDates (initialDate, finalDate) {
      this.$emit('updateDates', initialDate, finalDate)
    }
  }
}
</script>
