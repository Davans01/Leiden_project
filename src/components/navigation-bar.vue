<template>
  <div class="container">
    <div class="logo">
        <router-link to="/"> <img :src="require('/img/logo.png')"/></router-link>
    </div>
      <nav class="items">
           <!-- <div v-if="isAuthenticated">
      <h1></h1>
</div>
<div v-else>
  <h1>TEST_342323</h1>
</div> -->
        <ul><li><router-link class="link" to="/">home</router-link></li></ul>
        <ul><li><router-link class="link" to="/debug">debug</router-link></li></ul>
        <ul><li><router-link class="link" to="/about">about</router-link></li></ul>
        <ul><li><router-link class="link" to="/auth">auth</router-link></li></ul>
        <div v-if="isAuthenticated">
        <ul><li><router-link class="link" to="/logout">logout</router-link></li></ul>
        </div>
        <div v-else>
        <ul><li><router-link class="link" to="/login">login</router-link></li></ul>
        <ul><li><router-link class="link" to="/register">register</router-link></li></ul>
        </div>
      </nav>
  </div>
</template>

<script>
import { mapGetters } from "vuex"

export default {
  name: "navigation-bar",
   app_name: 'app',
  computed: {
    ...mapGetters(["isAuthenticated"])
  }
}
</script>

<style lang="scss" scoped>
.container {
  width: 100%;
  height: 84px;
  display: flex;
  justify-content: center;

  .logo{

    margin-left: 30px;

    img{
      max-height: 84px;
    }
  }
}

nav{
    width: 100%;
    float: right;
    display: inline-block;
    text-align: right;
}
.items {

  margin-right: 30px;

    ul{ 
      list-style: none;
      padding: 0;
      margin: 0;
      display: inline-block;

      li{
        

        a{
          text-decoration: none;
          color: black;
          display: block;
          margin: 25px 20px 0px 20px;
          text-transform: uppercase;
          font-weight: bold;
          border-bottom: 0px solid #6A8D00;
          -moz-transition: 0.2s;
          -o-transition: 0.2s;
          -ms-transition: 0.2s;
          -webkit-transition: 0.2s;
          transition: 0.2s;

          &:hover{
            border-bottom: 2px solid #6A8D00;
          }

        }
      }
    }
}

.link {

  &.active {
    color: #6A8D00;
  }
}
</style>
