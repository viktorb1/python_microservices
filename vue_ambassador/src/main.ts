import 'bootstrap/dist/css/bootstrap.css'
import vuetify from './plugins/vuetify'

import { createApp } from 'vue'
import { createPinia } from 'pinia'

import App from './App.vue'
import router from './router'

import axios from 'axios'
axios.defaults.baseURL = 'http://localhost:8000/api/ambassador'
axios.defaults.withCredentials = true

const app = createApp(App)

app.use(createPinia())
app.use(router)
app.use(vuetify)

app.mount('#app')

import 'bootstrap/dist/js/bootstrap.js'
