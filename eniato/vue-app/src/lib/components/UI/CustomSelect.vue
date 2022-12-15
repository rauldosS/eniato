<template>
  <treeselect
    v-bind="$attrs"
    :placeholder="placeholder"
    clearAllText="Remover tudo"
    clearValueText="Remover opção"
    :limitText="count => `e mais ${count}`"
    loadingText="Carregando..."
    noResultsText="Nenhum resultado encontrado..."
    searchPromptText="Digite para pesquisar..."
    :normalizer="mapOptionLabel"
    v-model="selectedValue"
    :loadOptions="loadOptions"
    :retry-text="retryText"
    :class="getTreeClass(state)"
    @input="$emit('change')"
  />
</template>

<script>
import Treeselect from '@riophae/vue-treeselect'
import '@riophae/vue-treeselect/dist/vue-treeselect.css'

export default {
  inheritAttrs: true,
  props: {
    state: {
      type: Boolean,
      default: null
    },
    loadOptions: {
      type: Function,
      default: () => {}
    },
    placeholder: {
      type: String,
      default: 'Selecione...'
    },
    label: {
      type: String,
      default: 'label'
    },
    retryText: {
      type: String,
      default: 'Recarregar?'
    },
    value: {}
  },
  computed: {
    selectedValue: {
      get () { return this.value },
      set (value) { this.$emit('input', value) }
    }
  },
  components: {
    Treeselect
  },
  methods: {
    mapOptionLabel (option) {
      return {
        id: option.id,
        label: option[this.label]
      }
    },
    getTreeClass (state) {
      return `custom-vue-tree ${state ? 'is-valid' : (state === false ? 'is-not-valid' : null)}`
    }
  }
}
</script>

<style>
  .vue-treeselect--disabled .vue-treeselect__control {
    background-color: #e9ecef !important;
    opacity: 1;
  }

  .vue-treeselect__placeholder {
    color: #636c72 !important;
  }

  .vue-treeselect__control {
    border: 1px solid #ced4da;
  }

  .is-valid .vue-treeselect__control,
  .is-valid .vue-treeselect__control:hover
   {
    border-color: #28a745 !important;
  }

  .is-not-valid .vue-treeselect__control,
  .is-not-valid .vue-treeselect__control:hover
   {
    border-color: #dc3545 !important;
  }
</style>
