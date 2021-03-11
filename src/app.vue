<template>
  <navigation-bar />
  <router-view />
</template>

<script>
import NavigationBar from "./components/navigation-bar"

export default {
  name: "app",
  components: {
    NavigationBar,
  },
}
</script>

<style lang="scss">
@import "./global.scss";
</style>
