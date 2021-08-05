<template>
  <div id="app">
    <navbar id="navbr">
      <slot slot="slot1"><a href="#app" class="nav-link" v-smooth-scroll>Home</a></slot>
      <slot slot="slot2"><a href="#docpanel" class="nav-link" v-smooth-scroll={offset:-50}>Doctors</a></slot>
      <slot slot="slot3"><a href="#hosppanel" class="nav-link" v-smooth-scroll={offset:-150}>Hospitals</a></slot>
      <slot slot="slot4"><a href="#services" class="nav-link" v-smooth-scroll={offset:-50}>Services</a></slot>
      <slot slot="slot5" v-if="auth"><router-link to="/dashboard"><a href="#" class="nav-link">Dashboard</a></router-link></slot>
    </navbar>
    <header_main></header_main>
    <docpanel id="docpanel"></docpanel>
    <hosppanel id="hosppanel"></hosppanel>
    <services id="services"></services>
    <footer_main></footer_main>
  </div>
</template>

<script>
import navbar from "../components/Basic/navbar.vue";
import header from "../components/Index/header.vue";
import docpanel from "../components/Index/docpanel.vue";
import hosppanel from "../components/Index/hosppanel.vue";
import services from "../components/Index/services.vue";
import footer from "../components/Basic/footer.vue";

export default {
  name: 'App',
  components: {
    "navbar":navbar,
    "header_main":header,
    "docpanel":docpanel,
    "hosppanel":hosppanel,
    "services":services,
    "footer_main":footer,
  },
  computed:{
    auth(){
      return this.$store.getters.isAuthenticated;
    }
  },
  methods:{
    logout(){
      this.$store.dispatch('logout')
    }
  }
}
</script>
<style>
body{
  overflow-x:hidden;
}
</style>
