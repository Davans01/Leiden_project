<template>
  <router-link
    :to="{ name: 'device-stats', params: { deviceId: $props.deviceId } }"
    custom
    v-slot="{ navigate }"
  >
    <div class="device" @click="navigate">
      {{ device.serial }}
    </div>
  </router-link>
</template>

<script>
import { mapState } from "vuex"

export default {
  name: "device-info",
  computed: {
    ...mapState({
      device(state) {
        return state.devices.devices.find(
          (device) => device.serial === this.deviceId,
        )
      },
    }),
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
