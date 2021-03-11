<template>
  <page-wrapper>
    <h1>Login</h1>
    <notice v-if="$route.query.next">
      You need to be signed in to view this page.
    </notice>
    <form @submit="login($event)">
      <text-input type="email" label="Email" v-model="email" />
      <text-input type="password" label="Password" v-model="password" />
      <checkbox label="Remember me" v-model="remember" />
      <primary-button type="submit">Login</primary-button>
      <router-link
        :to="{ name: 'register', query: { next: $route.query.next } }"
        custom
        v-slot="{ navigate }"
      >
        <primary-button @click="navigate">Register</primary-button>
      </router-link>
    </form>
  </page-wrapper>
</template>

<script>
import Checkbox from "../components/checkbox.vue"
import PrimaryButton from "../components/primary-button"
import TextInput from "../components/text-input"
import PageWrapper from "../components/page-wrapper"
import Notice from "../components/notice.vue"

export default {
  name: "auth",
  components: {
    Checkbox,
    PrimaryButton,
    TextInput,
    PageWrapper,
    Notice,
  },
  data() {
    return {
      email: "",
      password: "",
      remember: false,
    }
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
  },
}
</script>
