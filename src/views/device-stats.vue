<template>
  <page-wrapper>
    <pre>{{ JSON.stringify(device, undefined, 2) }}</pre>
    <pre>{{ JSON.stringify(measurements, undefined, 2) }}</pre>
  </page-wrapper>
  <page-footer></page-footer>
</template>

<script>
import { mapState } from "vuex"
import PageFooter from "../components/page-footer.vue"
import PageWrapper from "../components/page-wrapper.vue"

export default {
  name: "device-stats",
  components: {
    PageFooter,
    PageWrapper,
  },
  computed: {
    ...mapState({
      device(state) {
        return (state.devices.devices || []).find(
          (device) => device.serial === this.$route.params.deviceId,
        )
      },
      measurements(state) {
        return state.devices.measurements[this.$route.params.deviceId]
      },
    }),
  },
  mounted() {
    if (!this.device) {
      this.$store.dispatch("fetchDevices")
    }
    if (!this.measurements) {
      this.$store.dispatch("fetchMeasurements", this.$route.params.deviceId)
    }
  },
}
</script>

<style lang="scss" scoped>
</style>
