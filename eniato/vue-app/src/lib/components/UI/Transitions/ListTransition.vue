<!-- https://br.vuejs.org/v2/guide/transitions.html#Escalonamento-de-Transicoes-de-Lista -->

<template>
  <transition-group
    :css="false"
    :tag="tag"
    @before-enter="beforeEnter"
    @before-leave="beforeLeave"
    @enter="enter"
    @leave="leave"
  >
    <slot></slot>
  </transition-group>
</template>

<script>
import Velocity from 'velocity-animate'

export default {
  props: {
    duration: {
      type: Number,
      default: 500
    },
    tag: {
      type: String,
      default: 'span'
    }
  },
  methods: {
    beforeEnter (el) {
      el.style.opacity = 0
    },
    beforeLeave (el) {
      el.style.opacity = 1
    },
    enter (el, done) {
      Velocity(
        el,
        { opacity: 1 },
        {
          complete: done,
          duration: 500
        }
      )
    },
    leave (el, done) {
      Velocity(
        el,
        { opacity: 0 },
        {
          complete: done,
          duration: 300
        }
      )
    }
  }
}
</script>
