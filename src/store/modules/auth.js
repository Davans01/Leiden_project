import { request } from "../../request"

export const auth = {
  state() {
    return {
      user: null,
    }
  },
  getters: {
    isLoggedIn(state) {
      return state.user !== null
    },
  },
  mutations: {
    setAuthUserData(state, user) {
      state.user = user
    },
  },
  actions: {
    async login(context, requestData) {
      const { ok, data } = await request("POST /auth/login", requestData)

      if (ok) {
        context.commit("setAuthUserData", data)
      } else {
        context.commit("setAuthUserData", null)
      }
    },

    async logout(context) {
      const { ok } = await request("POST /auth/logout")

      if (ok) {
        context.commit("setAuthUserData", null)
      }
    },

    async register(context, requestData) {
      const { ok } = await request("POST /auth/register", requestData)

      if (ok) {
        context.dispatch("login", {
          email: requestData.email,
          password: requestData.password,
          remember: false,
        })
      }
    },
  },
}
