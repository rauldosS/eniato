<template>
  <div class="row">
    <ObjectiveCard
      v-for="objective in objectiveList"
      :key="objective.id"
      :objective="objective"
      @open-objective-modal-form="openObjectiveFormModal"
      @open-delete-objective-modal="openDeleteObjectiveModal"
    />
  </div>
</template>

<script>
import ObjectiveCard from '../Cards/ObjectiveCard'

export default {
  name: 'ObjectiveList',
  components: {
    ObjectiveCard
  },
  props: {
    objectiveList: Array
  },
  methods: {
    openObjectiveFormModal (objective) {
      this.$emit('openObjectiveFormModal', objective)
    },
    openDeleteObjectiveModal (objective) {
      this.$emit('openDeleteObjectiveModal', objective)
    }
  }
}
</script>

<style scoped>
</style>
