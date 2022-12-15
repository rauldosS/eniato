<template>
  <form :action="action" :method="method" ref="form" enctype="multipart/form-data">
    <input type="text" name="csrfmiddlewaretoken" :value="token" hidden>
    <slot></slot>
  </form>
</template>

<script>
export default {
  props: {
    action: {
      type: String,
      default: '.'
    },
    method: {
      type: String,
      default: 'GET'
    },
    token: {
      type: String,
      required: true
    }
  },
  inheritAttrs: true,
  methods: {
    submit () {
      this.$refs.form.submit()
    }
  },
  data () {
    return {}
  }
}
</script>

<style scoped>
</style>
