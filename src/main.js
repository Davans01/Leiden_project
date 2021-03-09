import { createApp } from "vue"
import App from "./app.vue"
import { request } from "./request"
import router from "./router"
import { store } from "./store"

export const app = createApp(App)
  .use(router)
  .use(store)

request("GET /auth/me").then(response => {
  store.commit("setAuthUserData", response.ok ? response.data : null)
  app.mount("#app")
})
