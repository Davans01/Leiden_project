<template>
  <page-wrapper>
    <h1>login</h1>
    <form @submit="logout($event)" v-if="isLoggedIn">
      <primary-button type="submit">Logout</primary-button>
    </form>
    <form @submit="login($event)" v-else>
      <text-input type="email" label="Email" v-model="email" />
      <text-input type="password" label="Password" v-model="password" />
      <checkbox label="Remember me" v-model="remember" />
      <primary-button type="submit">Login</primary-button>
    </form>
  </page-wrapper>
</template>

<script>
import { mapGetters } from "vuex"
import Checkbox from "../components/checkbox.vue"
import PrimaryButton from "../components/primary-button"
import TextInput from "../components/text-input"
import PageWrapper from "../components/page-wrapper"

export default {
  name: "auth",
  components: {
    Checkbox,
    PrimaryButton,
    TextInput,
    PageWrapper,
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
