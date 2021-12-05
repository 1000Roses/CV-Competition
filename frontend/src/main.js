import { createApp } from 'vue'
import App from './App.vue'
import router from './router'
import store from './store'
import './tailwind.css'



import { library } from '@fortawesome/fontawesome-svg-core'
import { faCode } from '@fortawesome/free-solid-svg-icons'
import { faBirthdayCake } from '@fortawesome/free-solid-svg-icons'
import { faEnvelope } from '@fortawesome/free-solid-svg-icons'
import { faMapMarkerAlt } from '@fortawesome/free-solid-svg-icons'
import { faPhoneAlt } from '@fortawesome/free-solid-svg-icons'

import { FontAwesomeIcon } from '@fortawesome/vue-fontawesome'

library.add(faCode)
library.add(faBirthdayCake)
library.add(faEnvelope)
library.add(faMapMarkerAlt)
library.add(faPhoneAlt)

createApp(App).use(store).use(router).component('font-awesome-icon', FontAwesomeIcon).mount('#app')
