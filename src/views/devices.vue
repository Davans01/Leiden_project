<template>
  <page-wrapper>
    <h1>Devices</h1>
    <ul v-if="devices">
      <li v-for="device of devices" :key="device.serial">
        {{ device.serial }}
      </li>
    </ul>
    <router-link to="/devices/register" custom v-slot="{ navigate }">
      <primary-button @click="navigate">Register Device</primary-button>
    </router-link>
  </page-wrapper>
  <page-footer></page-footer>
</template>

<script>
import { mapState } from "vuex"
import PageWrapper from "../components/page-wrapper"
import PageFooter from "../components/page-footer"
import PrimaryButton from "../components/primary-button.vue"

export default {
  name: "devices",
  components: {
    PageWrapper,
    PageFooter,
    PrimaryButton,
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
