<template>
  <div class="card">
    <slot name="card-header" v-if=has_header>
      <div class="card-header py-3 d-flex flex-row align-items-center justify-content-between">
          <h6 class="card-title">{{ title }}</h6>
          <slot name="header-actions">
          </slot>
      </div>
    </slot>
    <slot name="card-body">
      <div class="card-body">
        <slot></slot>
      </div>
    </slot>
  </div>
</template>

<script>
export default {
  props: {
    title: String,
    has_header: {
      default: true,
      type: Boolean
    }
  },
  inheritAttrs: true,
  data () {
    return {}
  }
}
</script>

<style scoped>
  .card-title {
    margin: 0;
    font-weight: 500;
  }
</style>
