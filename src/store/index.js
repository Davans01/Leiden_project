import { createStore } from "vuex"
import { auth } from "./modules/auth"
import { devices } from "./modules/devices"
import { meta } from "./modules/meta"

export const store = createStore({
  modules: {
    auth,
    devices,
    meta,
  },
})
