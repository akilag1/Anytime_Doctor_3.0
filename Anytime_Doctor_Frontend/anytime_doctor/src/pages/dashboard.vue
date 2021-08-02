<template>
  <div id="app">
     <navbar>
        <slot slot="slot1"><a href="#" class="nav-link">Home</a></slot>
        <slot slot="slot2"><a href="#" class="nav-link">Doctors</a></slot>
        <slot slot="slot3"><a href="#" class="nav-link">Hospitals</a></slot>
     </navbar>
     <div class="col-md-12 dashHeader">
        <h1>Welcome</h1>
      </div>
     <main_btn></main_btn>
     <footer_main></footer_main>
  </div>
</template>

<script>
import navbar from "../components/Basic/navbar.vue";
import footer from "../components/Basic/footer.vue";
import main_btn from "../components/Dashboard/main_btn.vue";


export default {
    components:{
    "navbar":navbar,
    "footer_main":footer,
    "main_btn":main_btn
  }
}
</script>

<style>
.dashHeader{
    text-align: center;
    margin-top: 3rem;
    margin-bottom: 2rem;
}
.dashHeader h1{
    font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif !important;
    color: rgb(243, 121, 14) !important;
    font-weight: 400;
    font-size: 2.5rem;
}
</style>

