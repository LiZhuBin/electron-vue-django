import Vue from 'vue'
import Router from 'vue-router'

Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/',
      name: 'landing-page',
      component: require('@/components/LandingPage').default,
      children: [{
        path: 'apriori',
        name: 'apriori',
        component: require('@/components/apriori/AprioriPage').default
      },
        {
          path: 'analyse',
          name: 'analyse',
          component: require('@/components/apriori/AnalysePage').default,

        },
        {
          path: 'dbshow',
          name: 'dbshow',
          component: require('@/components/apriori/DbShowPage').default,
        }
      ]


    },
    {
      path: '*',
      redirect: '/'
    }
  ]
})
