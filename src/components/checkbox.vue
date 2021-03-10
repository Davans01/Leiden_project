<template>
  <div class="checkbox" :class="$attrs.class" :style="$attrs.style">
    <div class="positioner">
      <input
        class="input"
        type="checkbox"
        v-bind="inputAttrs"
        :id="$attrs.id || id"
        :value="modelValue"
        @input="$emit('update:modelValue', $event.target.checked)"
      />
      <div class="button">
        <check-icon class="check" />
      </div>
    </div>
    <label class="label" :for="$attrs.id || id">{{ label }}</label>
  </div>
</template>

<script>
import { omit } from "../omit"
import { getId } from "../uid"
import CheckIcon from "../icons/check-icon"

export default {
  name: "checkbox",
  components: {
    CheckIcon,
  },
  props: {
    label: String,
    modelValue: Boolean,
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

.checkbox {
  display: flex;
  align-items: center;
  height: 32px;
  user-select: none;
}

.label {
  color: $header-primary;
  font-size: 16px;
  font-weight: 500;

  margin: 0 8px;
}

.positioner {
  width: 16px;
  height: 16px;
  position: relative;
}

.input {
  position: absolute;
  top: 0;
  right: 0;
  bottom: 0;
  left: 0;
  width: calc(100% + 16px);
  height: calc(100% + 16px);

  padding: 8px;
  margin: -8px;
  border: none;
  outline: none;

  opacity: 0;

  &:not(:disabled) {
    cursor: pointer;
  }
}

.button {
  position: absolute;
  top: 0;
  right: 0;
  bottom: 0;
  left: 0;
  width: 100%;
  height: 100%;

  background: $background-tertiary;
  border: 2px solid $background-tertiary;
  color: $interactive-active;

  pointer-events: none;

  transition: 150ms;
  transition-property: background-color, border-color, color;

  input:hover + & {
    background: $interactive-muted;
    border-color: $interactive-muted;
  }

  input:focus + & {
    border-color: $accent;
  }

  input:disabled + & {
    background: transparent;
    border-color: $interactive-muted;
    color: $interactive-muted;
  }
}

.check {
  position: absolute;
  top: 0;
  right: 0;
  bottom: 0;
  left: 0;
  width: 100%;
  height: 100%;

  opacity: 0;
  transition: 150ms;
  transition-property: opacity;

  :checked + .button > & {
    opacity: 1;
  }
}
</style>
