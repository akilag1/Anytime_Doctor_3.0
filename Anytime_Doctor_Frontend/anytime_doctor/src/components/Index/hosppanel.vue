<template>
  <section class="testimonials bg-light text-center testMnial">
        <div class="container">
      <h2 class="mb-5 docpaneltext">Places available to take care of you..</h2>
      <div class="row">
        {{this.hospList()}}
        <div class="col-lg-4" v-for="hospital in hcList" :key="hospital.id">
          <div class="testimonial-item mx-auto mb-5 mb-lg-0">
            <img class="img-fluid rounded-circle mb-3" :src="hospital.picture" alt="">
            <router-link :to="'/hospitals/' + hospital.id" tag="a"><h5>{{hospital.name}}</h5></router-link>
            <p class="font-weight-light mb-0 docpanelsubtext">{{hospital.location}}</p>
          </div>
        </div>
      </div>
        <!-- viewmore -->

      <div class="docpanelviewmore">
          <router-link to="/hospitals"><button btn btn-lg>See All <i class="fas fa-arrow-circle-right"></i></button></router-link>
      </div>
    </div>
  </section>
</template>
<script>
import axios from 'axios'
export default {
     data:function(){
       return{
        hospitalList:[],
        hcList:[]
       }
     },
     methods:{
       hospList(){
         let lenAr=this.hospitalList.length;
         if(lenAr>3){
           lenAr=3
         }
         for(let i=0;i<lenAr;i++){
           this.hcList[i]=this.hospitalList[i];
         }
       }
     },
     created(){
      axios.get('http://localhost:8001/hospitals/hospitals/')
        .then(res =>{
          const data=res.data
          const hospitals=[]
          for(let key in data){
            const hospital=data[key]
            hospital.id=key
            hospitals.push(hospital)
          }
          this.hospitalList=hospitals;
        })  
    }
}
</script>
<style>
.docpanelviewmore{
    display: flex;
    justify-content: flex-end;
}
.docpanelviewmore button{
    font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
    font-weight: 200;
    width: 6rem;
    background-color: rgb(236, 118, 15);
    text-align: center;
    color:white;
    padding-right: 0;
    margin-right: -2rem;
    margin-bottom: -2rem;
}
.docpanelviewmore button:hover{
    background-color: rgb(236, 138, 52);
}

/* Doctor_Bar */

.testMnial{
    padding-top: 0 !important;
    padding-bottom: 5rem;
    font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
    /* background-color: rgb(248, 171, 103); */
}
.docpaneltext{
    font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
    color: rgb(243, 121, 14);
    font-weight: 300;
    font-size: 2.5rem;
}
.docpanelsubtext{
    font-size: 1rem;
}
.testimonials {
  /* background-color: rgb(212, 183, 169);; */
  /* padding-top: 7rem; */
  padding-bottom: 7rem;
}

.testimonials .testimonial-item {
  max-width: 18rem;
}

.testimonials .testimonial-item img {
  max-width: 12rem;
  box-shadow: 0px 5px 5px 0px #adb5bd;
}
a:hover {
  text-decoration: none;
}
</style>