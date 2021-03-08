<template>
  <h1>home</h1>
  <api-status></api-status>
  <pre>{{ state }}</pre>
</template>

<script>
import ApiStatus from "../components/api-status"

export default {
  name: "home",
  components: {
    ApiStatus,
  },
  computed: {
    state() {
      return JSON.stringify(this.$store.state, undefined, 2)
    },
  },
}
</script>
