import { createRouter, createWebHistory } from "vue-router"
import { store } from "./store"

const routes = [
  {
    path: "/",
    name: "home",
    component: () => import("./views/home"),
  },
  {
    path: "/debug",
    name: "debug",
    component: () => import("./views/debug"),
  },
  {
    path: "/about",
    name: "about",
    component: () => import("./views/about"),
  },
  {
    path: "/login",
    name: "login",
    component: () => import("./views/login"),
  },
  {
    path: "/logout",
    name: "logout",
    component: () => import("./views/logout"),
  },
  {
    path: "/register",
    name: "register",
    component: () => import("./views/register"),
  },
  {
    path: "/devices",
    name: "devices",
    component: () => import("./views/devices"),
  },
  {
    path: "/devices/register",
    name: "register-device",
    component: () => import("./views/register-device"),
  },
  {
    path: "/devices/@:deviceId",
    name: "device-stats",
    component: () => import("./views/device-stats"),
  },
]

export const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes,
  linkActiveClass: "active",
  linkExactActiveClass: "active-exact",
  linkExactPathActiveClass: "active-exact-path",
})

// these routes are only accessible when the user is not authenticated
// others are only accessible when the user is authenticated
const unauthenticatedRoutes = ["login", "register"]

router.beforeEach((to, from, next) => {
  const { isAuthenticated } = store.getters

  if (to.name === "debug") {
    next()
    return
  }

  if (unauthenticatedRoutes.includes(to.name) && isAuthenticated) {
    next({
      name: "logout",
      query: {
        next: to.fullPath,
      },
    })
    return
  }

  if (!unauthenticatedRoutes.includes(to.name) && !isAuthenticated) {
    next({
      name: "login",
      query: {
        next: to.fullPath,
      },
    })
    return
  }

  next()
})

store.watch(
  (state, getters) => getters.isAuthenticated,
  () => {
    router.push(router.currentRoute.value.query.next || { name: "home" })
  },
)
