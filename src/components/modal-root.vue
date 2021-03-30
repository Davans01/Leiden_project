<template>
  <div v-if="component">
    <component :is="component" @close="handleClose" v-bind="props" />
  </div>
</template>

<script>
import { markRaw } from "vue"
import { modalBus } from "../bus"

export default {
  name: "modal-root",
  data() {
    return {
      component: null,
      props: null,
    }
  },
  mounted() {
    modalBus.on("open", this.handleOpen)
    modalBus.on("close", this.handleClose)
    document.addEventListener("keydown", this.handleKeyDown)
  },
  unmounted() {
    this.component = null
    modalBus.off("open", this.handleOpen)
    modalBus.off("close", this.handleClose)
    document.removeEventListener("keydown", this.handleKeyDown)
  },
  methods: {
    handleOpen(event) {
      this.component = markRaw(event.component)
      this.props = event.props
    },
    handleClose() {
      this.component = null
    },
    handleKeyDown(event) {
      if (event.keyCode === 27) this.handleClose()
    },
  },
}
</script>
