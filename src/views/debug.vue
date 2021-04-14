<template>
  <page-wrapper>
    <h1>debug</h1>
    <pre>{{ state }}</pre>
  </page-wrapper>
  <page-footer></page-footer>
</template>

<script>
import PageWrapper from "../components/page-wrapper"
import PageFooter from "../components/page-footer"

export default {
  name: "debug",
  components: {
    PageWrapper,
    PageFooter,
  },
  data() {
    return {
      status: "unknown",
    }
  },
  computed: {
    state() {
      return JSON.stringify(this.$store.state, undefined, 2)
    },
  },
}
</script>
