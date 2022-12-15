<template>
  <button class="btn btn-round" @click="$emit('click')">
    <slot></slot>
  </button>
</template>

<style scoped>
.btn-round {
    display: inline !important;
    width: 2rem;
    height: 2rem;
    line-height: 2rem;
    border-radius: 50%;
    padding: 0;
    background: #dee2e6;
    display: flex;
    align-items: center;
    justify-content: center;
    margin-left: 0.2rem;
    font-weight: 600;
    vertical-align: middle;
}

.btn-round * {
    font-size: 14px;
    color: #6c757d;
}

.btn-round:hover {
    background: #cfd5db;
}
.btn:hover {
    color: #6c757d;
    text-decoration: none;
}
</style>
