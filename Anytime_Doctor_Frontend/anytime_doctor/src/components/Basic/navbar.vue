<template>
    <div class="row navrow">
        <div class="col-md-12">
          <nav class="navbar navbar-expand-lg navbar-light myNavbar">
            <router-link to="/" class="navbar-brand myNavTitle">ANYTIME DOCTOR</router-link>
            <!-- <a class="navbar-brand myNavTitle" href="#">ANYTIME DOCTOR</a> -->
            <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarSupportedContent" aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation">
              <span class="navbar-toggler-icon"></span>
            </button>
            <div class="collapse navbar-collapse" id="navbarSupportedContent">
              <ul class="navbar-nav mr-auto">
                <li class="nav-item">
                  <slot name="slot1" class="nav-link"></slot>
                </li>
                <li class="nav-item">
                  <slot name="slot2" class="nav-link"></slot>
                </li>
                <li class="nav-item">
                  <slot name="slot3" class="nav-link"></slot>
                </li>
                <li class="nav-item">
                  <slot name="slot4" class="nav-link"></slot>
                </li>
                <li class="nav-item">
                  <slot name="slot5" class="nav-link"></slot>
                </li>
                <li class="nav-item">
                  <slot name="slot6" class="nav-link"></slot>
                </li>
              </ul>
            </div>
          </nav>
        </div>
    </div>    
</template>

<script>
export default {
    
}
</script>

<style>
.navrow{
    position: sticky;
    top: 0;
    z-index: 1;
    /* width:100%; */
}
.myNavbar{
    background-color: #fad487;
    padding: 2rem;
    height: 4rem;
    font-size: 1.3rem;
}
.myNavTitle{
    font-size: 1.5rem;
    font-weight: 200;
    border: #901838 solid 1px ;
    border-radius: 5px;
    padding: 4px;
    background-color: #96c2f5;
}
#navbarSupportedContent li a{
    font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
    color: rgb(0, 1, 5);
}
#navbarSupportedContent li a:hover{
    padding-bottom: 6px;
    color: rgb(236, 80, 18);
    border-bottom: solid red 2px;
}

body {
  font-family: 'Lato', 'Helvetica Neue', Helvetica, Arial, sans-serif;
}

h1,
h2,
h3,
h4,
h5,
h6 {
  font-family: 'Lato', 'Helvetica Neue', Helvetica, Arial, sans-serif;
  font-weight: 700;
}
</style>