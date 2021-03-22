<template>
  <page-wrapper>
    <h1>Devices</h1>
    <ul v-if="devices">
      <li v-for="device of devices" :key="device.serial">
        {{ device.serial }}
      </li>
    </ul>
  </page-wrapper>
  <page-footer></page-footer>
</template>

<script>
import { mapState } from "vuex"
import PageWrapper from "../components/page-wrapper"
import PageFooter from "../components/page-footer"

export default {
  name: "devices",
  components: {
    PageWrapper,
    PageFooter,
  },
  computed: {
    ...mapState({
      devices: (state) => state.devices.devices,
    }),
  },
  mounted() {
    this.$store.dispatch("fetchDevices")
  },
}
</script>
