import Vue from 'vue'
import VueRouter from 'vue-router'
import itemSearch from '../views/itemSearch.vue'
import Cart from '../views/Cart.vue'
import DetailView from '../views/detailView.vue'

Vue.use(VueRouter)

const routes = [
  {
    path: '/',
    name: 'home',
    component: itemSearch
  },
  {
    path: '/cart',
    name: 'cart',
    component: Cart
  },
  {
    path: '/detail',
    name: 'detail',
    component: DetailView
  }

]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router
