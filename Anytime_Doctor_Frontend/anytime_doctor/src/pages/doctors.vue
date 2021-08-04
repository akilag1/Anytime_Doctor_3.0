<template>
  <div id="app">
     <navbar>
      <slot slot="slot1"><router-link to="/"><a href="#" class="nav-link">Home</a></router-link></slot>
      <slot slot="slot2"><router-link to="/doctors"><a href="#" class="nav-link">Doctors</a></router-link></slot>
      <slot slot="slot3"><router-link to="/hospitals"><a href="]#" class="nav-link">Hospitals</a></router-link></slot>
     </navbar>
     <router-view></router-view>
     <footer_main></footer_main>
  </div>
</template>

<script>
import navbar from "../components/Basic/navbar.vue";
import footer from "../components/Basic/footer.vue";

export default {
    components:{
    "navbar":navbar,
    "footer_main":footer,
  }
}
</script>

<style>

</style>
