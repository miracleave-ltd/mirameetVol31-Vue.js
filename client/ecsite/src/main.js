import Vue from 'vue'
import App from './App.vue'
import router from './router'
import store from './store'
import './filter/index.js'
import { BootstrapVue, IconsPlugin } from 'bootstrap-vue'
import 'bootstrap/dist/css/bootstrap.css' // add
import 'bootstrap-vue/dist/bootstrap-vue.css' // add
import 'sweetalert2/dist/sweetalert2.min.css'
import VueSweetalert2 from 'vue-sweetalert2' // add
import axios from 'axios' // 追記
import VueAxios from 'vue-axios' // 追記
axios.defaults.baseURL = 'http://localhost:8040/product' // add
axios.defaults.withCredentials = true // 追加
axios.defaults.xsrfHeaderName = 'X-CSRF-Token'

Vue.use(VueSweetalert2) // add
Vue.use(BootstrapVue)
Vue.use(IconsPlugin) // add
Vue.config.productionTip = false
Vue.use(VueAxios, axios) // 追記
new Vue({
  router,
  store,
  render: h => h(App)
}).$mount('#app')
