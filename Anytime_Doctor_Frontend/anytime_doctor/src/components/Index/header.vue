<template>
  <header class="masthead text-white text-center">
    <div class="overlay"></div>
    <div class="container">
      <div class="row">
        <div class="col-md-9 mx-auto">
          <h1 class="mb-5 maintext">Meet your Doctor from Home!</h1>
        </div>
      </div>
      <div class="row">
        <div class="col-md-6">
          <div class="mainbtn1">
            <router-link to="/register" tag="a"><button type="button" class="btn btn-lg joinbtn">Join</button></router-link>
          </div>
        </div>
        <div class="col-md-6">
          <div class="mainbtn2">
            <router-link to="/login" tag="a"><button type="button" class="btn btn-lg btn-primary signinbtn">SignIn</button></router-link>
          </div>  
        </div>
      </div>
    </div>
  </header>
</template>

<script>
export default {
    
}
</script>

<style>
.mainbtn1{
    text-align: right;
}
.mainbtn2{
    text-align: left;
}
.joinbtn{
    color: white;
    font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
    font-weight: 450;
    width: 6rem;
    background-color: rgb(236, 118, 15);
    text-align: center;
}
.joinbtn:hover{
    color: white;
    font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
    font-weight: 450;
    width: 6rem;
    background-color: rgb(236, 138, 52);
    text-align: center;
}
.signinbtn{
    font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
    font-weight: 450;
    width: 6rem;
    text-align: center;
}
.maintext{
    font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
    color: rgb(250, 250, 250);
}
header.masthead {
  position: relative;
  background:#333 url("../../assets/img/Pic1.jpg") no-repeat center center;
  background-size: cover;
  padding-top: 8rem;
  padding-bottom: 8rem;
}
header.masthead .overlay {
  position: absolute;
  background-color: #212529;
  height: 100%;
  width: 100%;
  top: 0;
  left: 0;
  opacity: 0.5;
}
header.masthead h1 {
  font-size: 2rem;
}
@media (min-width: 768px) {
  header.masthead {
    padding-top: 12rem;
    padding-bottom: 12rem;
  }
  header.masthead h1 {
    font-size: 3rem;
  }
}
</style>