<template>
  <div class="progress">
    <div
      class="progress-bar bg-brmed"
      role="progressbar"
      :style="{ width: `${progress}%` }"
      :aria-valuenow="progress"
      aria-valuemin="0"
      aria-valuemax="100"
    >
    </div>
  </div>
</template>

<script>
export default {
  props: {
    progress: Number
  }
}
</script>

<style scoped>
.progress {
  display: flex;
  overflow: hidden;
  font-size: 0.75rem;
  background-color: #dee2e6;
  border-radius: 20rem;
  height: 0.1875rem;
  background: none;
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  z-index: 1;
}

.progress-bar {
  display: flex;
  flex-direction: column;
  justify-content: center;
  color: #fff;
  text-align: center;
  white-space: nowrap;
  transition: width 0.6s ease;
  height: 1rem;
  border-radius: .5rem 0 0 0;
}
</style>
