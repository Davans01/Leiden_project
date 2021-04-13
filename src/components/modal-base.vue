<template>
  <div class="backdrop" @click="$emit('close')">
    <div class="modal" @click.stop>
      <slot></slot>
    </div>
  </div>
</template>

<script>
export default {
  name: "modal-base",
}
</script>

<style lang="scss" scoped>
@import "../vars.scss";

.backdrop {
  position: fixed;
  top: 0;
  right: 0;
  bottom: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background: rgba(0, 0, 0, 0.3);


  display: flex;
  flex-direction: row;
  justify-content: center;
  align-items: center;
  overflow-y: auto;
}

.modal {
  background: $background-primary;
  padding: 24px;
  border-radius: 4px;

  width: 1320px;
  height: calc(100vh - 32px);
}
</style>
