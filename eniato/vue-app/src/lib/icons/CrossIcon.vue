<template>
    <svg :height="this.height" :width="this.width" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
      <path d="M18.707 6.70685L17.293 5.29285L12 10.5858L6.70697 5.29285L5.29297 6.70685L10.586 11.9998L5.29297 17.2928L6.70697 18.7068L12 13.4138L17.293 18.7068L18.707 17.2928L13.414 11.9998L18.707 6.70685Z"
        :fill="this.color"/>
    </svg>
</template>

<script>
export default {
  name: 'CrossIcon',
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
