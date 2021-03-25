<template>
  <page-wrapper>
    <h1>Register Device</h1>
    <notice v-if="error">
      <template v-if="error === 'DEVICE_NOT_FOUND'">
        No device was found for this pairing code or the device is already
        registered.
      </template>
      <template v-else>An unknown error occurred.</template>
    </notice>
    <form @submit="registerDevice($event)">
      <text-input
        type="text"
        label="Pairing code"
        v-model="pairingCode"
        @input="error = undefined"
      />
      <primary-button type="submit">Register</primary-button>
    </form>
  </page-wrapper>
  <page-footer></page-footer>
</template>

<script>
import PageWrapper from "../components/page-wrapper"
import PageFooter from "../components/page-footer"
import TextInput from "../components/text-input"
import PrimaryButton from "../components/primary-button"
import Notice from "../components/notice.vue"

export default {
  name: "register-device",
  components: {
    PageWrapper,
    PageFooter,
    TextInput,
    PrimaryButton,
    Notice,
  },
  data() {
    return {
      pairingCode: "",
      error: undefined,
    }
  },
  methods: {
    async registerDevice(event) {
      event.preventDefault()
      const { ok, data } = await this.$store.dispatch("registerDevice", {
        pairingCode: this.pairingCode,
      })
      if (ok) {
        this.$router.push({ name: "devices" })
      } else {
        this.error = data.error
      }
    },
  },
}
</script>
