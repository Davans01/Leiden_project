<template>
  <page-wrapper>
    <h1>Logout</h1>
    <p>Are you sure you want to log out?</p>
    <form @submit="logout($event)">
      <primary-button type="submit">Logout</primary-button>
    </form>
  </page-wrapper>
  <page-footer></page-footer>

</template>

<script>
import PrimaryButton from "../components/primary-button"
import PageWrapper from "../components/page-wrapper"
import PageFooter from "../components/page-footer"

export default {
  name: "auth",
  components: {
    PrimaryButton,
    PageWrapper,
    PageFooter,
  },
  methods: {
    logout(event) {
      event.preventDefault()
      this.$store.dispatch("logout")
    },
  },
}
</script>
