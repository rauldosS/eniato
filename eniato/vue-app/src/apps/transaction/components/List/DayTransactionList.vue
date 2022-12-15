<template>
  <div class="d-flex flex-column text-center me-3">
    <div
      class="mt-3 fw-bold"
      :class="currentDate()
        ? 'text-link'
        : 'text-black-50'"
    >
      {{ dayOfTheWeek }}
    </div>
    <div
      class="fs-4 day"
      :class="currentDate()
        ? 'bg-link text-white shadow rounded-circle d-flex justify-content-center align-items-center'
        : ''"
    >
      {{ day }}
    </div>
  </div>
</template>

<script>
export default {
  props: {
    day: {
      type: Number,
      required: true
    },
    dayOfTheWeek: {
      type: String,
      required: true
    }
  },
  methods: {
    currentDate () {
      return this.currentDay === this.day
    }
  },
  data () {
    return {
      currentDay: new Date().getDate()
    }
  }
}
</script>

<style scoped>
  .day {
    width: 40px;
    height: 40px;
  }
</style>
