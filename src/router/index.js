import { createRouter, createWebHistory } from "vue-router"

const routes = [
  {
    path: "/",
    name: "home",
    component: () => import("../views/home"),
  },
  {
    path: "/debug",
    name: "debug",
    component: () => import("../views/debug"),
  },
  {
    path: "/about",
    name: "about",
    component: () => import("../views/about.vue"),
  },
  {
    path: "/auth",
    name: "auth",
    component: () => import("../views/auth.vue"),
  },
]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes,
  linkActiveClass: "active",
  linkExactActiveClass: "active-exact",
  linkExactPathActiveClass: "active-exact-path",
})

export default router
