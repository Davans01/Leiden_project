import { request } from "../../request"

export const devices = {
  state() {
    return {
      devices: null,
      measurements: {},
    }
  },
  mutations: {
    setDevices(state, devices) {
      state.devices = devices
    },

    addDevice(state, device) {
      if (state.devices) state.devices.push(device)
    },

    setMeasurements(state, data) {
      state.measurements[data.device] = data.measurements
    },
  },
  actions: {
    async fetchDevices(context) {
      const { data } = await request("GET /devices")

      if (data) {
        context.commit("setDevices", data.devices)
      }
    },

    async fetchMeasurements(context, device) {
      const { data } = await request(
        `GET /devices/${encodeURIComponent(device)}/measurements`,
      )

      if (data) {
        context.commit("setMeasurements", {
          device,
          measurements: data.measurements,
        })
      }
    },

    async registerDevice(context, requestData) {
      const response = await request("POST /devices", requestData)

      if (response.ok) {
        context.commit("addDevice", response.data)
      }

      return response
    },
  },
}
