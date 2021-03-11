<template>
  <page-wrapper>
    <h1>debug</h1>
    api status:
    <pre>{{ status }}</pre>
    store state:
    <pre>{{ state }}</pre>
  </page-wrapper>
</template>

<script>
import { request } from "../request"
import PageWrapper from "../components/page-wrapper"

export default {
  name: "debug",
  components: {
    PageWrapper,
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
  async mounted() {
    const { status, data } = await request("GET /status")

    if (status > 0) {
      this.status = JSON.stringify(data, undefined, 2)
    } else {
      this.status = "unreachable"
    }
  },
}
</script>
