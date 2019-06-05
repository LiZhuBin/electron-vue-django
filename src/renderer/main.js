import Vue from 'vue'
import axios from 'axios'
import ElementUI from 'element-ui'
import 'element-ui/lib/theme-chalk/index.css'
import App from './App'
import router from './router'
import store from './store'
import Global from '../Global'
import qs from 'qs'

Vue.use(ElementUI)
axios.defaults.baseURL = Global.URL_ROOT
Vue.prototype.qs = qs

axios.defaults.baseURL = 'https://api.example.com'
axios.defaults.headers.post['Content-Type'] = 'application/x-www-form-urlencoded'
// axios 配置

if (!process.env.IS_WEB) Vue.use(require('vue-electron'))
Vue.http = Vue.prototype.$http = axios
Vue.config.productionTip = false

/* eslint-disable no-new */
new Vue({
  components: { App },
  router,
  store,
  template: '<App/>'
}).$mount('#app')
