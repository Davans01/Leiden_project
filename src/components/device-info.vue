
<template>
  <div class="device">
    {{ device.serial }}
  </div>
</template>

<script>
import { mapState } from "vuex"

export default {
  name: "device-info",
  computed: {
    ...mapState({
      devices: (state) => state.devices.devices,
    }),
    device() {
      return this.devices.find((device) => device.serial === this.deviceId)
    },
  },
  props: {
    deviceId: String,
  },
}
</script>

<style lang="scss" scoped>
@import "../vars.scss";

.device {
  padding: 24px;
  margin-top: 8px;
  background: $background-secondary;
}
</style>
