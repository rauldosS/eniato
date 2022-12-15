import Vue from 'vue'
import components from './components'
import store from './store'

import './dependencies.js'

import 'vue-loading-overlay/dist/vue-loading.css'
// import 'bootstrap/dist/css/bootstrap.css'
import 'bootstrap-vue/dist/bootstrap-vue.css'
import 'bs-stepper/dist/css/bs-stepper.min.css'

Vue.config.productionTip = false

new Vue({
  store,
  components
}).$mount('#app')
