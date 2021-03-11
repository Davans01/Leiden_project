<template>
  <div class="container">
    <nav class="items">
      <router-link class="link" to="/">home</router-link> |
      <router-link class="link" to="/debug">debug</router-link> |
      <router-link class="link" to="/about">about</router-link> |
      <router-link class="link" to="/login">login</router-link>
    </nav>
  </div>
</template>

<script>
export default {
  name: "navigation-bar",
}
</script>

<style lang="scss" scoped>
.container {
  width: 100%;
  height: 64px;
  display: flex;
  justify-content: center;
}

.items {
  width: 960px;
}

.link {
  color: blue;

  &.active {
    color: red;
  }
}
</style>
