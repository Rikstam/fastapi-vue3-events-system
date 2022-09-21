import { createRouter, createWebHashHistory } from 'vue-router'
import EventList from './views/EventList.vue'
import EventDetails from './views/EventDetails.vue'
import EventCreate from './views/EventCreate.vue'
import ErrorDisplay from './views/ErrorDisplay.vue'
import About from './views/About.vue'
import LoginForm from './views/LoginForm.vue'
import RegistrationForm from './views/RegistrationForm.vue'
import Dashboard from './views/Dashboard.vue'

const routes = [
  {
    path: '/',
    name: 'EventList',
    component: EventList
  },
  {
    path: '/event/:id',
    name: 'EventDetails',
    props: true,
    component: EventDetails
  },
  {
    path: '/event/create',
    name: 'EventCreate',
    component: EventCreate,
    meta: {
      requiresAuth: true
    }
  },
  {
    path: '/about',
    name: 'About',
    component: About
  },
  {
    path: '/error/:error',
    name: 'ErrorDisplay',
    props: true,
    component: ErrorDisplay
  },
  {
    path: '/login',
    name: 'Login',
    component: LoginForm
  },
  {
    path: '/sign-up',
    name: 'Signup',
    component: RegistrationForm
  },
  {
    path: '/dashboard',
    name: 'Dashboard',
    component: Dashboard,
    meta: {
      requiresAuth: true
    }
  },
]

const router = createRouter({
  history: createWebHashHistory(),
  routes
})

router.beforeEach((to, from, next) => {
  const loggedIn = localStorage.getItem('user')
  if (to.matched.some((record) => record.meta.requiresAuth)) {
    if (!loggedIn) {
      next('/')
    } else {
      next()
    }
  } else {
    next()
  }
})

export default router
