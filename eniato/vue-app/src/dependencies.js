import Vue from 'vue'

import { BootstrapVue, BootstrapVueIcons } from 'bootstrap-vue'
import 'vue-material-design-icons/styles.css'
import VueTheMask from 'vue-the-mask'
import money from 'v-money'
import { FontAwesomeIcon } from '@fortawesome/vue-fontawesome'
import { library as FontAwesomeIconLibrary } from '@fortawesome/fontawesome-svg-core'
import VueFab from 'vue-float-action-button'
import Dropdown from 'vue-simple-search-dropdown'

import {
  faCheck,
  faFileUpload,
  faUpload,
  faPlus,
  faSearchPlus,
  faExclamationTriangle,
  faTrash,
  faSave,
  faTimes,
  faPen
} from '@fortawesome/free-solid-svg-icons'

FontAwesomeIconLibrary.add(
  faCheck,
  faPlus,
  faUpload,
  faFileUpload,
  faSearchPlus,
  faExclamationTriangle,
  faTrash,
  faSave,
  faTimes,
  faPen
)

Vue.component('font-awesome-icon', FontAwesomeIcon)

Vue.use(BootstrapVue)
Vue.use(BootstrapVueIcons)
Vue.use(VueTheMask)
Vue.use(Dropdown)
Vue.use(money, { precision: 2 })
Vue.use(VueFab, {
  iconType: 'iconfont'
})
