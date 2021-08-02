<template>
  <section class="call-to-action text-white text-center">
    <!-- <div class="subscribe"></div> -->
    <div class="container subcontent">
      <div class="row">
        <div class="col-xl-9 mx-auto">
          <h2 class="mb-4">Ready to get Health Tips!SignUp!</h2>
        </div>
        <div class="col-md-10 col-lg-8 col-xl-7 mx-auto">
          <form>
            <div class="form-row">
              <div class="col-12 col-md-9 mb-2 mb-md-0">
                <input type="email" class="form-control form-control-lg" placeholder="Enter your email...">
              </div>
              <div class="col-12 col-md-3">
                <button type="submit" class="btn btn-block btn-lg btn-primary">Sign up!</button>
              </div>
            </div>
          </form>
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
.subfield{
    margin-top: 2.5rem;
    padding-top: 2rem;
    padding-bottom: 2rem;
    height: 6rem;
}
.subcontent{
    font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
    color: rgb(243, 121, 14);
    font-weight: 300;
}
.call-to-action {
  position: relative;
  background-color: #ffffff;
  /* background: url("../../assets/img/bg-masthead.jpg") no-repeat center center; */
  background-size: cover;
  padding-top: 5rem;
  padding-bottom: 3rem;
}

.call-to-action .overlay {
  position: absolute;
  background-color: #212529;
  height: 100%;
  width: 100%;
  top: 0;
  left: 0;
  opacity: 0.3;
}
</style>