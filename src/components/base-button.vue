<template>
  <clickable class="base-button">
    <slot></slot>
  </clickable>
</template>

<script>
import Clickable from "./clickable.vue"

export default {
  name: "base-button",
  components: {
    Clickable,
  },
}
</script>

<style lang="scss" scoped>
.base-button {
  display: inline-block;

  min-width: 60px;
  min-height: 36px;
  max-height: 36px;

  padding: 0 14px;
  border: 2px solid transparent;

  font-family: "Montserrat", Helvetica, Arial, sans-serif;
  font-size: 16px;
  font-weight: 600;
  white-space: nowrap;

  transition: 167ms;
  transition-property: background-color, border-color, color;
}
</style>
