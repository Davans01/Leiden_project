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

    setMeasurements(state, device, measurements) {
      state.measurements[device] = measurements
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
        `POST /devices/${encodeURIComponent(device)}/measurements`,
      )

      if (data) {
        context.commit("setMeasurements", device, data.measurements)
      }
    },

    async registerDevice(context, requestData) {
      const { ok, data } = await request("POST /devices", requestData)

      if (ok) {
        context.commit("addDevice", data)
      }

      return data
    },
  },
}
