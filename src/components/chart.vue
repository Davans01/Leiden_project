<template>
  <canvas ref="canvas"></canvas>
</template>

<script>
import Chart from "chart.js"

export default {
  name: "chart",
  state() {
    return {}
  },
  props: {
    options: Object,
  },
  mounted() {
    const context = this.$refs.canvas.getContext("2d")
    this.chart = new Chart(context, this.options)
  },
}
</script>

<style lang="scss" scoped>
</style>
