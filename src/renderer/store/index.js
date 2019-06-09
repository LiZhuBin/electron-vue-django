import Vue from 'vue'
import Vuex from 'vuex'

import { createPersistedState, createSharedMutations } from 'vuex-electron'

import modules from './modules'

Vue.use(Vuex)
export const strict = false
export default new Vuex.Store({
  modules,
  plugins: [
    createPersistedState(),
    createSharedMutations()
  ],
  state: {
    cities :['广州市','深圳市','佛山市','东莞市','中山市','珠海市','江门市','肇庆市','惠州市'],
    goods :  ['面包','奶类','零食','酒类','方便面','水果'],
    cities_select: [],
    date_select:[],
    goods_select: []
  },
  strict: process.env.NODE_ENV !== 'production'
})
