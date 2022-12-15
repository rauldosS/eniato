<template>
  <div class="card card-task" @click="$emit('click')">
      <Progress :progress="progress" />
      <div class="card-body">
          <div class="card-title">
            <slot name="title"></slot>
          </div>
          <div class="card-meta">
            <slot name="meta"></slot>
            <div class="card-options" v-if="hasDropdownActions">
              <b-dropdown
                size="lg"
                variant="link"
                toggle-class="text-decoration-none card-options-btn"
                class="overflow-none"
                offset="-100"
                no-caret>
                <template v-slot:button-content>
                  <i class="material-icons">more_vert</i>
                </template>
                <slot name="dropdown-actions"></slot>
              </b-dropdown>
            </div>
          </div>
      </div>
  </div>
</template>

<script>
import Progress from './Progress'

export default {
  inheritAttrs: true,
  props: {
    tasksDone: Number,
    tasksTotal: Number
  },
  components: {
    Progress
  },
  computed: {
    progress () {
      return (this.tasksDone / this.tasksTotal) * 100
    },
    hasDropdownActions () {
      return !!this.$slots['dropdown-actions']
    }
  }
}
</script>

<style scoped>
.card-task {
  cursor: pointer;
}

.card-body {
    flex: 1 1 auto;
    padding: 1.25rem;
}

.card .card-title {
    margin-bottom: 1.5rem;
    max-width: 50%;
}

@media (min-width: 1200px) {
  .card .card-title {
      margin: 0;
  }
}

@media (max-width: 1200px) {
  .card .card-title {
    max-width: 90%;
  }
}

.card-task .card-meta {
    display: flex;
    align-items: center;
    justify-content: space-between;
}

@media (min-width: 1200px) {
  .card-task .card-body {
      justify-content: space-between;
  }
}

@media (min-width: 1200px) {
  .card-task .card-body, .card-task .card-meta {
      display: flex;
      align-items: center;
  }
}

.card-task .card-meta i.check-icon {
  margin-right: 0.25rem;
  font-size: 24px;
}

.card-body .card-options {
    position: absolute;
    top: 1.5rem;
    right: 0.75rem;
}

@media (min-width: 1200px) {
  .card-task .card-options {
      margin-left: .5rem;
      position: relative;
      top: 0;
      right: 0;
  }
}

.card-options i.material-icons {
  font-size: 24px;
  margin-right: 0.25rem;
  margin-bottom: .1rem;
}

.card {
    position: relative;
    display: flex;
    flex-direction: column;
    min-width: 0;
    word-wrap: break-word;
    background-color: #fff;
    background-clip: border-box;
    border: none;
    border-radius: 0.5rem;
    box-shadow: 0 0.1875rem 0.375rem rgba(33, 37, 41, 0.05);
    margin-bottom: 0.75rem;
}

.card:last-child {
    margin-bottom: 0;
}
</style>
