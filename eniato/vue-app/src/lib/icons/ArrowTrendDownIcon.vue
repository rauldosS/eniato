<template>
  <svg class="icon" :height="this.height" :width="this.width" viewBox="0 -1.5 18 18" fill="none" xmlns="http://www.w3.org/2000/svg">
    <path fill-rule="evenodd" d="M0 0h1Zm10 11.5a.5.5 0 0 0 .5.5h4a.5.5 0 0 0 .5-.5v-4a.5.5 0 1 0-1 0v2.6l-3.613-4.417a.5.5 0 0 0-.7-.037L7.06 8.231 3.40 3.206a.5.5 0 0 0-.808.588l4 5.5a.5.5 0 0 0 .758.06l2.609-2.61L13.445 11H10.5a.5.5 0 0 0-.5.5Z"
      :fill="this.color"/>
  </svg>
</template>

<script>
export default {
  name: 'ArrowTrendDown',
  props: {
    width: {
      type: Number,
      default: 24
    },
    height: {
      type: Number,
      default: 24
    },
    color: {
      type: String,
      default: '#01394c'
    }
  }
}
</script>

<style scoped>
  .icon {
    margin-top: -2px;
  }
</style>
