import Vue from 'vue'
import App from './App.vue'
import VueSmoothScroll from 'vue2-smooth-scroll'
import VueRouter from 'vue-router'
import {routes} from './routes'
import {store} from './store/store.js'
import Vuelidate from 'vuelidate'

Vue.config.productionTip = false

Vue.use(VueSmoothScroll, {
  duration: 700,
  updateHistory:true,
})

Vue.use(VueRouter)
Vue.use(Vuelidate)

const router=new VueRouter({
  routes,
  mode:'history'
})

new Vue({
  render: h => h(App),
  router,
  store,
}).$mount('#app')
