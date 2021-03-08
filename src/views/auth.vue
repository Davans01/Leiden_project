<template>
  <h1>login</h1>
  <form @submit="logout($event)" v-if="isLoggedIn">
    <input type="submit" value="Logout" />
  </form>
  <form @submit="login($event)" v-else>
    <label class="input-container">
      <div class="input-label">Email</div>
      <input v-model="email" type="email" />
    </label>
    <label class="input-container">
      <div class="input-label">Password</div>
      <input v-model="password" type="password" />
    </label>
    <label class="input-container">
      <input v-model="remember" type="checkbox" />
      <div class="input-label">Remember me</div>
    </label>
    <input type="submit" value="Login" />
  </form>
</template>

<script>
import { mapGetters } from "vuex"

export default {
  name: "auth",
  data() {
    return {
      email: "",
      password: "",
      remember: false,
    }
  },
  computed: {
    ...mapGetters(["isLoggedIn"]),
  },
  methods: {
    login(event) {
      event.preventDefault()
      this.$store.dispatch("login", {
        email: this.email,
        password: this.password,
        remember: this.remember,
      })
    },

    logout(event) {
      event.preventDefault()
      this.$store.dispatch("logout")
    },
  },
}
</script>

<style lang="scss" scoped>
.input-container {
  display: block;
}

.input-label {
  display: block;
}
</style>
