<template>
  <div id="app">
     <navbar>
        <slot slot="slot1"><router-link to="/"><a href="#" class="nav-link">Home</a></router-link></slot>
      <slot slot="slot2"><router-link to="/doctors"><a href="#" class="nav-link">Doctors</a></router-link></slot>
      <slot slot="slot3"><router-link to="/hospitals"><a href="]#" class="nav-link">Hospitals</a></router-link></slot>
     </navbar>
     <div class="col-md-12 dashHeader">
        <h1>Welcome Owner</h1>
    </div>
    <h3 class="dash_text">Active Appointments</h3>
    <div class="appo_block"> 
      <hr>
      <div>
        <p>Appointment NO:</p>
        <p>date:</p>
        <p>time:</p>
      </div>
    </div>
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
.appo_block{
  display: flex;
  background-color: rgb(228, 145, 74);
  border: black solid 1px;
}
.dash_text{
  text-align: center;
}
</style>

