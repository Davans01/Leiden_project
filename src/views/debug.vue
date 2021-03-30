<template>
  <page-wrapper>
    <h1>debug</h1>
    <div>
      <primary-button @click="openTestModal">open test modal</primary-button>
    </div>
    test chart:
    <chart></chart>
    api status:
    <pre>{{ status }}</pre>
    store state:
    <pre>{{ state }}</pre>
  </page-wrapper>
  <page-footer></page-footer>
</template>

<script>
import { request } from "../request"
import PageWrapper from "../components/page-wrapper"
import PageFooter from "../components/page-footer"
import Chart from "../components/chart.vue"
import PrimaryButton from "../components/primary-button.vue"
import TestModal from "./test-modal.vue"
import { modalBus } from "../bus"

export default {
  name: "debug",
  components: {
    PageWrapper,
    PageFooter,
    Chart,
    PrimaryButton,
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
  methods: {
    openTestModal() {
      modalBus.emit("open", {
        component: TestModal,
        props: {
          testProp: Math.random(),
        },
      })
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
