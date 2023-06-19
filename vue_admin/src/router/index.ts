import { createRouter, createWebHistory } from 'vue-router'
import Layout from '@/views/Layout.vue'
import Login from '@/views/Login.vue'
import Register from '@/views/Register.vue'
import Users from '@/views/Users.vue'
import Links from '@/views/Links.vue'
import Products from '@/views/Products/Products.vue'
import ProductForm from '@/views/Products/ProductForm.vue'
import Orders from '@/views/Orders.vue'
import Profile from '@/views/Profile.vue'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'layout',
      component: Layout,
      children: [
        {
          path: '/users',
          name: 'users',
          component: Users
        },
        {
          path: '/users/:id/links',
          name: 'user_links',
          component: Links
        },
        {
          path: '/products',
          name: 'products',
          component: Products
        },
        {
          path: '/products/create',
          component: ProductForm
        },
        {
          path: '/products/:id/edit',
          component: ProductForm
        },
        {
          path: '/orders',
          component: Orders
        },
        {
          path: '/profile',
          component: Profile
        }
      ]
    },
    {
      path: '/login',
      name: 'login',
      component: Login
    },
    {
      path: '/register',
      name: 'register',
      component: Register
    },
    {
      path: '',
      redirect: '/users'
    }
  ]
})

export default router
