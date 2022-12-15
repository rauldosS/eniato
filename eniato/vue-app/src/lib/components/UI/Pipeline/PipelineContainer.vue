<template>
  <div class="content-list-body">
    <div class="card-list">
      <div class="card-list-head">
        <slot name="title"></slot>
      </div>
      <div class="card-list-body">
        <slot></slot>
      </div>
    </div>
  </div>
</template>

<style scoped>
.card-list {
    margin-bottom: 0.75rem;
    border-radius: 0.5rem;
    padding: 1rem 0;
}

.card-list .card-list-head {
    display: flex;
    justify-content: space-between;
}
</style>
