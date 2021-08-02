import Vue from 'vue'
import App from './App.vue'
import VueSmoothScroll from 'vue2-smooth-scroll'
import VueRouter from 'vue-router'
import {routes} from './routes'

Vue.config.productionTip = false

Vue.use(VueSmoothScroll, {
  duration: 700,
  updateHistory:true,
})

Vue.use(VueRouter)

const router=new VueRouter({
  routes
})

new Vue({
  render: h => h(App),
  router,
}).$mount('#app')
