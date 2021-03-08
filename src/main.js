import { createApp } from "vue"
import App from "./app.vue"
import router from "./router"
import { store } from "./store"

export const app = createApp(App)
  .use(router)
  .use(store)
  .mount("#app")
