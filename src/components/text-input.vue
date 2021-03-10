<template>
  <div class="text-input" :class="$attrs.class" :style="$attrs.style">
    <div class="label">
      <label :for="$attrs.id || id">{{ label }}</label>
    </div>
    <input
      class="input"
      v-bind="inputAttrs"
      :id="$attrs.id || id"
      :value="modelValue"
      @input="$emit('update:modelValue', $event.target.value)"
    />
  </div>
</template>

<script>
import { omit } from "../omit"
import { getId } from "../uid"

export default {
  name: "text-input",
  props: {
    label: String,
    modelValue: String,
  },
  computed: {
    inputAttrs() {
      return omit(this.$attrs, "class", "style")
    },
  },
  emits: ["update:modelValue"],
  inheritAttrs: false,
  data() {
    return {
      id: getId(),
    }
  },
}
</script>

<style lang="scss" scoped>
@import "../vars.scss";

.text-input {
  min-width: 0;
  display: flex;
  flex-direction: column;
}

.label {
  color: $header-primary;
  font-size: 16px;
  font-weight: 500;
  margin-bottom: 4px;
}

.input {
  padding: 0 9px;
  height: 36px;
  min-width: 0;
  max-width: 100%;

  background: $background-tertiary;
  border: 2px solid transparent;
  outline: none;

  color: $text-normal;
  font-size: 16px;

  transition: 150ms;
  transition-property: background-color, border-color, color;

  &:focus {
    border-color: $accent;
  }

  &:disabled {
    border-color: $interactive-muted;
    background: transparent;
    color: $text-muted;
  }

  &:invalid {
    box-shadow: none;
  }

  &::placeholder {
    color: $interactive-normal;
  }
}
</style>
