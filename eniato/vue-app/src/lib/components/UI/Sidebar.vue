<template>
  <div class="navbar navbar-expand-lg bg-light navbar-light sticky-top">
    <slot name="header"></slot>
    <div class="d-flex align-items-center">
      <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbar-collapse" aria-controls="navbar-collapse" aria-expanded="false" aria-label="Toggle navigation">
        <span class="navbar-toggler-icon"></span>
      </button>
    </div>
    <div class="collapse navbar-collapse flex-column" id="navbar-collapse">
      <slot name="body"></slot>
    </div>
  </div>
</template>

<script>
export default {
  props: {
    title: {
      type: String,
      required: false
    }
  }
}
</script>

<style scoped>
.navbar {
  position:relative;
}

@media (min-width: 992px) {
  .navbar .navbar-collapse {
      align-items: flex-start;
      width: 100%;
      flex-shrink: 0;
      padding-bottom: 1.5rem;
  }

  .navbar-expand-lg .navbar-collapse {
      display: flex !important;
      flex-basis: auto;
    }

  .navbar {
      box-shadow: inset -1px 0 0 rgba(0, 0, 0, .1);
      padding: 1.5rem;
      padding-top: .5rem;
      min-width: 420px;
      max-width: 420px;
      min-height: calc(100vh - 67px);
      -ms-overflow-style: none;
      flex-direction: column;
      align-items: flex-start;
      position: sticky;
      max-height: 100vh;
      overflow: auto;
  }
}

@media (max-width: 991px) {
  .navbar {
    box-shadow: inset 0 -1px 0 rgba(0, 0, 0, .1);
  }
}
</style>
