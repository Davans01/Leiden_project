<template>
  <base-button class="secondary-button">
    <slot></slot>
  </base-button>
</template>

<script>
import BaseButton from "./base-button"

export default {
  name: "secondary-button",
  components: {
    BaseButton,
  },
}
</script>

<style lang="scss" scoped>
@import "../vars.scss";

.secondary-button {
  border-color: transparentize($interactive-normal, 0.5);
  color: $header-primary;

  &:hover {
    background: $background-modifier-active;
  }

  &:focus {
    border-color: $accent;
  }

  &:active {
    background: $background-tertiary;
    border-color: $background-tertiary;
  }

  &:disabled {
    border-color: $interactive-muted;
    color: $text-muted;
  }
}
</style>
