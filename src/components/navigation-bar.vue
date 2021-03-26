<template>
  <page-wrapper>
    <nav class="container">
      <div class="logo">
        <router-link to="/">
          <img src="../assets/logo.png" alt="Logo" />
        </router-link>
      </div>
      <ul class="items">
        <li class="item">
          <router-link class="link" to="/">home</router-link>
        </li>
        <li class="item">
          <router-link class="link" to="/devices">devices</router-link>
        </li>
        <li class="item">
          <router-link class="link" to="/about">about</router-link>
        </li>
        <li class="item" v-if="!isAuthenticated">
          <router-link class="link" to="/login">login</router-link>
        </li>
        <li class="item" v-else>
          <router-link class="link" to="/logout">logout</router-link>
        </li>
        <li class="item">
          <router-link class="link" to="/debug">debug</router-link>
        </li>
      </ul>
    </nav>
  </page-wrapper>
</template>

<script>
import { mapGetters } from "vuex"
import PageWrapper from "./page-wrapper"

export default {
  name: "navigation-bar",
  components: {
    PageWrapper,
  },
  computed: {
    ...mapGetters(["isAuthenticated"]),
  },
}
</script>

<style lang="scss" scoped>
@import "../vars.scss";

.container {
  width: 100%;
  height: 84px;
  display: flex;
  justify-content: center;
}

.logo {
  flex: 1;

  img {
    max-height: 84px;
  }
}

.items {
  list-style: none;
  padding: 0;
  margin: 0;

  display: flex;
  align-items: center;
}

.link {
  text-decoration: none;
  color: black;
  display: block;
  margin: 0 20px;
  text-transform: uppercase;
  font-weight: bold;
  border-bottom: 2px solid transparent;
  transition: 0.2s;

  &:hover {
    border-bottom-color: $accent;
  }

  &.active {
    color: $accent;
  }
}
</style>
