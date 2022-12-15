<template>
    <svg :height="this.height" :width="this.width" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
        <g clip-path="url(#clip0_3376_8807)">
        <path d="M24 4.00024H0V6.00024H24V4.00024Z"
            :fill="this.color"/>
        <path d="M24.0001 9H8.00012V11H24.0001V9Z"
            :fill="this.color"/>
        <path d="M24 19.0002H0V21.0003H24V19.0002Z"
            :fill="this.color"/>
        <path d="M24.0001 14.0005H8.00012V16.0005H24.0001V14.0005Z"
            :fill="this.color"/>
        <path d="M0 8.00049V16.9675L4.17 13.2285C4.27459 13.1347 4.35824 13.0199 4.41551 12.8917C4.47278 12.7634 4.50238 12.6245 4.50238 12.484C4.50238 12.3435 4.47278 12.2046 4.41551 12.0763C4.35824 11.948 4.27459 11.8333 4.17 11.7395L0 8.00049Z"
            :fill="this.color"/>
        </g>
        <defs>
        <clipPath id="clip0_3376_8807">
        <rect width="24" height="24" fill="white"/>
        </clipPath>
        </defs>
    </svg>
</template>

<script>
export default {
  name: 'IndentIcon',
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
