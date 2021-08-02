<template>
  <div id="app">
     <navbar>
      <slot slot="slot1"><a href="#" class="nav-link">Home</a></slot>
      <slot slot="slot2"><a href="#" class="nav-link">Doctors</a></slot>
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
