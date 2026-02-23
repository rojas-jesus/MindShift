import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '../views/HomeView.vue'
import LoginView from '../views/LoginView.vue'
import RegisterView from '../views/RegisterView.vue'
import DashboardView from '../views/DashboardView.vue'

import { authService } from '../services/auth'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'home',
      component: HomeView
    },
    {
      path: '/login',
      name: 'login',
      component: LoginView
    },
    {
      path: '/register',
      name: 'register',
      component: RegisterView
    },
    {
      path: '/dashboard',
      name: 'dashboard',
      component: DashboardView
    },

    {
      path: '/about',
      name: 'about',
      component: () => import('../views/AboutView.vue')
    },
    {
      path: '/thoughts',
      name: 'thoughts',
      component: () => import('../views/ThoughtsView.vue')
    },
    {
      path: '/thought-raw/list',
      name: 'thought-raw-list',
      component: () => import('../views/RawThoughtsListView.vue')
    },
    {
      path: '/thought-raw/create',
      name: 'thought-raw-create',
      component: () => import('../views/ThoughtCreateView.vue')
    },
    {
      path: '/action-raw/create',
      name: 'action-raw-create',
      component: () => import('../views/ActionCreateView.vue')
    }
  ]
})

export default router
