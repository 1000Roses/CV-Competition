import { createApp } from 'vue'
import App from './App.vue'
import router from './router'
import store from './store'
import './tailwind.css'



import { library } from '@fortawesome/fontawesome-svg-core'
import { faCode } from '@fortawesome/free-solid-svg-icons'
import { FontAwesomeIcon } from '@fortawesome/vue-fontawesome'

library.add(faCode)

createApp(App).use(store).use(router).component('font-awesome-icon', FontAwesomeIcon).mount('#app')