<template>
  <button class="clickable">
    <slot></slot>
  </button>
</template>

<script>
export default {
  name: "clickable",
}
</script>

<style lang="scss" scoped>
.clickable {
  display: block;

  margin: 0;
  padding: 0;
  border: none;
  background: none;
  outline: none;
  color: inherit;
  font: inherit;

  cursor: pointer;

  &:disabled {
    cursor: default;
  }
}
</style>
