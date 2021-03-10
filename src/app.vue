<template>
  <div id="nav">
    <router-link to="/">home</router-link> |
    <router-link to="/about">about</router-link> |
    <router-link to="/auth">auth</router-link>
  </div>
  <router-view />
</template>

<style lang="scss">
@import "./global.scss";
</style>
