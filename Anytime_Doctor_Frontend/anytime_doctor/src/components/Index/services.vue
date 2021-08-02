<template>
  <section class="showcase">
    <div class="container-fluid p-0">
      <div class="row no-gutters">

        <div class="col-lg-6 order-lg-2 text-white showcase-img" id="show1"></div>
        <div class="col-lg-6 order-lg-1 my-auto showcase-text">
          <h2>Anytime Care</h2>
          <p class="lead mb-0">Connect with your favorite doctor from anywhere in the world</p>
        </div>
      </div>
      <div class="row no-gutters">
        <div class="col-lg-6 text-white showcase-img" id="show2"></div>
        <div class="col-lg-6 my-auto showcase-text">
          <h2>Time Saving</h2>
          <p class="lead mb-0">Save your time by managing all tests and scans</p>
        </div>
      </div>
      <div class="row no-gutters">
        <div class="col-lg-6 order-lg-2 text-white showcase-img" id="show3"></div>
        <div class="col-lg-6 order-lg-1 my-auto showcase-text">
          <h2>Fast and Easy</h2>
          <p class="lead mb-0">Do all the things from your fingertip</p>
        </div>
      </div>
    </div>
  </section>
</template>
<script>
export default {
    
}
</script>
<style>
.showcase{
    font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
    background-color: rgb(252, 218, 189);
}
.showcase h2{
    font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
    font-size: 3rem;
    color: rgb(243, 121, 14);
}
.showcase p{
    font-weight: 300;
}
.showcase .showcase-text {
  padding: 3rem;
}

.showcase .showcase-img {
  min-height: 30rem;
  background-size: cover;
}

@media (min-width: 768px) {
  .showcase .showcase-text {
    padding: 7rem;
  }
}
#show1{
    background-image: url('../../assets/img/Pic9.jpg');
}
#show2{
    background-image: url('../../assets/img/Pic8.jpg');
}
#show3{
    background-image: url('../../assets/img/Pic7.jpg');
}
</style>