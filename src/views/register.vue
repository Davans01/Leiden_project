<template>
  <page-wrapper>
    <h1>Register</h1>
    <form @submit="register($event)">
      <text-input type="email" label="Email" v-model="email" />
      <text-input type="password" label="Password" v-model="password" />
      <primary-button type="submit">Register</primary-button>
    </form>
  </page-wrapper>
  <page-footer></page-footer>
</template>

<script>
import PrimaryButton from "../components/primary-button"
import TextInput from "../components/text-input"
import PageWrapper from "../components/page-wrapper"
import PageFooter from "../components/page-footer"


export default {
  name: "register",
  components: {
    PrimaryButton,
    TextInput,
    PageWrapper,
    PageFooter,
  },
  data() {
    return {
      email: "",
      password: "",
    }
  },
  methods: {
    register(event) {
      event.preventDefault()
      this.$store.dispatch("register", {
        email: this.email,
        password: this.password,
      })
    },
  },
}
</script>
