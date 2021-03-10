<template>
  <base-button class="primary-button">
    <slot></slot>
  </base-button>
</template>

<script>
import BaseButton from "./base-button"

export default {
  name: "primary-button",
  components: {
    BaseButton,
  },
}
</script>

<style lang="scss" scoped>
@import "../vars.scss";

.primary-button {
  background: $accent;
  border-color: $accent;
  color: $header-primary;

  &:hover {
    background: lighten($accent, 5%);
    border-color: lighten($accent, 5%);
  }

  &:focus {
    border-color: $interactive-active;
  }

  &:active {
    background: darken($accent, 10%);
    border-color: darken($accent, 10%);
  }

  &:disabled {
    background: transparent;
    border-color: $interactive-muted;
    color: $text-muted;
  }
}
</style>
