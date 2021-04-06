<template>
  <canvas ref="canvas"></canvas>
  <canvas ref="canvas2"></canvas>
</template>

<script>
import Chart from "chart.js"

export default {
  name: "chart",
  state() {
    return {}
  },
  mounted() {
    const context = this.$refs.canvas.getContext("2d")
    const canvas2 = this.$refs.canvas2.getContext("2d")

    this.chart = new Chart(context, {
      type: "doughnut",
      data: {
        labels: ["12pm", "1pm", "2pm", "3pm", "4pm", "5pm"],
        datasets: [
          {
            label: "# of Votes",
            data: [53, 3, 40, 3, 1, 24],
            backgroundColor: [
              "rgba(255, 99, 132, 0.2)",
              "rgba(54, 162, 235, 0.2)",
              "rgba(255, 206, 86, 0.2)",
              "rgba(75, 192, 192, 0.2)",
              "rgba(153, 102, 255, 0.2)",
              "rgba(255, 159, 64, 0.2)",
            ],
            borderColor: [
              "rgba(255, 99, 132, 1)",
              "rgba(54, 162, 235, 1)",
              "rgba(255, 206, 86, 1)",
              "rgba(75, 192, 192, 1)",
              "rgba(153, 102, 255, 1)",
              "rgba(255, 159, 64, 1)",
            ],
            borderWidth: 2,
          },
        ],
      },
      options: {
        scales: {
          yAxes: [
            {
              ticks: {
                beginAtZero: true,
              },
            },
          ],
        },
      },
    })

    this.chart = new Chart(canvas2, {
      type: "line",
      data: {
        labels: ["12pm", "1pm", "2pm", "3pm", "4pm", "5pm"],
        datasets: [
          {
            label: "# of Votes",
            data: [53, 3, 40, 3, 1, 24],
            backgroundColor: [
              "rgba(255, 99, 132, 0.2)",
              "rgba(54, 162, 235, 0.2)",
              "rgba(255, 206, 86, 0.2)",
              "rgba(75, 192, 192, 0.2)",
              "rgba(153, 102, 255, 0.2)",
              "rgba(255, 159, 64, 0.2)",
            ],
            borderColor: [
              "rgba(255, 99, 132, 1)",
              "rgba(54, 162, 235, 1)",
              "rgba(255, 206, 86, 1)",
              "rgba(75, 192, 192, 1)",
              "rgba(153, 102, 255, 1)",
              "rgba(255, 159, 64, 1)",
            ],
            borderWidth: 2,
          },
        ],
      },
      options: {
        scales: {
          yAxes: [
            {
              ticks: {
                beginAtZero: true,
              },
            },
          ],
        },
      },
    })

  },
}
</script>

<style lang="scss" scoped>
</style>