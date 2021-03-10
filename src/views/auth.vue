<template>
  <h1>login</h1>
  <form @submit="logout($event)" v-if="isLoggedIn">
    <primary-button type="submit">Logout</primary-button>
  </form>
  <form @submit="login($event)" v-else>
    <text-input type="email" label="Email" v-model="email" />
    <text-input type="password" label="Password" v-model="password" />
    <label class="input-container">
      <input v-model="remember" type="checkbox" />
      <div class="input-label">Remember me</div>
    </label>
    <primary-button type="submit">Login</primary-button>
  </form>
</template>

<script>
import { mapGetters } from "vuex"
import PrimaryButton from "../components/primary-button"
import TextInput from "../components/text-input"

export default {
  name: "auth",
  components: {
    PrimaryButton,
    TextInput,
  },
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
