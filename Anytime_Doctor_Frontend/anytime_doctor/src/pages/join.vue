<template>
  <div id="app">
     <navbar>
      <slot slot="slot1"><a href="#" class="nav-link">Home</a></slot>
      <slot slot="slot2"><a href="#" class="nav-link">Doctors</a></slot>
      <slot slot="slot3"><a href="#" class="nav-link">Hospitals</a></slot>
     </navbar>
     <div class="maincontent">
        <h1>Welcome</h1>
        <p>Just few more steps</p>
     </div>
     <reg_form></reg_form>
     <footer_main></footer_main>
  </div>
</template>

<script>
import navbar from "../components/Basic/navbar.vue";
import footer from "../components/Basic/footer.vue";
import reg_form from "../components/Register/reg_form.vue";

export default {
    components:{
    "navbar":navbar,
    "footer_main":footer,
    "reg_form":reg_form,
  }
}
</script>

<style>
.maincontent{
    text-align: center;
    font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
    padding-top: 4rem;
    padding-bottom: 2rem;
}
.maincontent h1{
    color: rgb(243, 121, 14);
    font-weight: 300;
    font-size: 2.5rem;
}
.maincontent p{
    font-size: 1rem;
}
</style>
