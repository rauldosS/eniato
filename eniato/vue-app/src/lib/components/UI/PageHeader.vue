<template>
  <div class="page-header">
    <slot name="alert"></slot>
    <slot name="title"></slot>
    <slot name="subtitle"></slot>
  </div>
</template>

<style scoped>
  .page-header {
    padding-top: 1.5rem;
    margin-bottom: 1.5rem;
  }

  p {
    margin-bottom: 1.5rem;
    color: #6c757d;
    font-size: 1.25rem;
    font-weight: 400;
  }

  @media (min-width: 992px) {
    .page-header {
        padding-top: 1.3rem;
    }
  }
</style>
