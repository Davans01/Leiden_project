import { request } from "../../request"

export const meta = {
  state() {
    return {}
  },
  mutations: {
    setConfig(state, data) {
      Object.assign(state, data)
    },
  },
  actions: {
    async fetchConfig(context) {
      const { data } = await request("GET /config")
      if (data) {
        context.commit("setConfig", data)
      }
    },
  },
}
