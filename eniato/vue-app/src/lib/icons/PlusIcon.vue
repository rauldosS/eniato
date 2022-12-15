<template>
    <svg class="icon" :height="this.height" :width="this.width" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
        <path d="M13 11V6H11V11H6V13H11V18H13V13H18V11H13Z" :fill="this.color"/>
    </svg>
</template>

<script>
export default {
  name: 'PlusIcon',
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
    margin-left: -5px;
    margin-right: -5px;
  }
</style>
