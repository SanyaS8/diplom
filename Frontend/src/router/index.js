import { createRouter, createWebHistory } from 'vue-router'
import Index from "@/pages/Index.vue";
import Login from "@/pages/Login.vue";
import Profile from "@/pages/Profile.vue";
import Ticket from "@/pages/Ticket.vue";

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'home',
      component: Index,
    },
    {
      path: '/login',
      name: 'login',
      component: Login,
    },
    {
      path: '/profile',
      name: 'profile',
      component: Profile,
    },
    {
      path: '/ticket',
      name: 'ticket',
      component: Ticket,
    },
  ],
})

export default router
