<template>
  <navigation-bar />
  <router-view />
  <modal-root />
</template>

<script>
import ModalRoot from "./components/modal-root.vue"
import NavigationBar from "./components/navigation-bar"

export default {
  name: "app",
  components: {
    ModalRoot,
    NavigationBar,
  },
}
</script>

<style lang="scss">
@import "./global.scss";
</style>
