<template>
  <div class="notice">
    <slot></slot>
  </div>
</template>

<script>
export default {
  name: "notice",
}
</script>

<style lang="scss" scoped>
@import "../vars.scss";

.notice {
  background: transparentize($danger, 0.5);
  border: 2px solid $danger;
  padding: 16px 20px;
}
</style>
