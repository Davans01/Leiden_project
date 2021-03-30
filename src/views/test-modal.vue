<template>
  <modal-base>
    <h1>test modal</h1>
    <p>{{ testProp }}</p>
    <primary-button @click="close">close</primary-button>
  </modal-base>
</template>

<script>
import { modalBus } from "../bus"
import ModalBase from "../components/modal-base"
import PrimaryButton from "../components/primary-button.vue"

export default {
  name: "test-modal",
  components: {
    ModalBase,
    PrimaryButton,
  },
  props: {
    testProp: Number,
  },
  methods: {
    close() {
      modalBus.emit("close")
    },
  },
}
</script>
