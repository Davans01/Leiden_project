<template>
  <div>
    api status:
    <pre>{{ status }}</pre>
  </div>
</template>

<script>
export default {
  data() {
    return {
      status: "unknown",
    }
  },
  async mounted() {
    try {
      const response = await fetch("http://127.0.0.1:5000/status")
      if (response.ok) {
        const status = await response.json()
        this.status = JSON.stringify(status, undefined, 2)
      } else {
        this.status = "error"
      }
    } catch {
      this.status = "unreachable"
    }
  },
}
</script>
