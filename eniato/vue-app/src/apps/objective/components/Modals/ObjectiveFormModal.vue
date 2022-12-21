<template>
  <b-modal
    ref="objective-form-modal"
    :title="objective ? 'Editar Objetivo' : 'Novo Objetivo'"
    ok-title="Fechar"
    @ok="hide"
    @close="hide"
    size="md"
    centered
  >
    <ObjectiveForm
      class="mx-4"
      ref="objective-form"
      :objective="objective"
    />
    <template v-slot:modal-footer>
      <button @click="hide" class="button alternative-button">Fechar</button>
      <button
        type="submit"
        class="button primary-button"
        @click.prevent="save"
      >
        Salvar
      </button>
    </template>
  </b-modal>
</template>

<script>
import ObjectiveForm from '../Forms/ObjectiveForm'

export default {
  components: {
    ObjectiveForm
  },
  methods: {
    open (objective) {
      this.objective = objective
      this.show()
    },
    show () {
      this.$refs['objective-form-modal'].show()
    },
    hide () {
      this.$refs['objective-form-modal'].hide()
    },
    save () {
      this.$refs['objective-form'].tryToSubmit().then(valid => valid ? this.hide() : null)
    }
  },
  data () {
    return {
      objective: null
    }
  }
}
</script>
