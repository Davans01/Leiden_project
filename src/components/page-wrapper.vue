<template>
  <div class="wrapper">
    <div class="container">
      <slot></slot>
    </div>
  </div>
</template>

<script>
export default {
  name: "page-wrapper",
}
</script>

<style lang="scss" scoped>
.wrapper {
  width: 100%;
  display: flex;
  justify-content: center;
}

.container {
  margin: 0 32px;
  width: 960px;
}
</style>
