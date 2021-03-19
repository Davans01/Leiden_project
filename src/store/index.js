import { createStore } from "vuex"
import { auth } from "./modules/auth"
import { devices } from "./modules/devices"

export const store = createStore({
  modules: {
    auth,
    devices,
  },
})
