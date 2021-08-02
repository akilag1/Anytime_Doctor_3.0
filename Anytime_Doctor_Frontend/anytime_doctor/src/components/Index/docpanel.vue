<template>
  <section class="testimonials text-center bg-light testMnil">
    <div class="container">
      <h2 class="mb-5 docpaneltext">People who here to help You..</h2>
      <div class="row">
        {{this.docList()}}
        <div class="col-lg-4" v-for="doctor in dcList" :key="doctor.id">
          <div class="testimonial-item mx-auto mb-5 mb-lg-0">
            <img class="img-fluid rounded-circle mb-3" :src="doctor.picture" alt="">
            <router-link :to="'/doctors/' + doctor.id" tag="a"><h5>{{doctor.name}}</h5></router-link>
            <p class="font-weight-light mb-0 docpanelsubtext">{{doctor.speciality}}</p>
          </div>
        </div>
      </div>
        <!-- viewmore -->

      <div class="docpanelviewmore">
          <router-link to="/doctors"><button btn btn-lg>See All <i class="fas fa-arrow-circle-right"></i></button></router-link>
      </div>
    </div>
  </section>
</template>
<script>
import axios from 'axios'
export default {
     data:function(){
       return{
        doctorList:[],
        dcList:[]
       }
     },
     methods:{
       docList(){
         let lenAr=this.doctorList.length;
         if(lenAr>3){
           lenAr=3
         }
         for(let i=0;i<lenAr;i++){
           this.dcList[i]=this.doctorList[i];
         }
       }
     },
     created(){
      axios.get('http://localhost:8001/doctors/doctors/')
        .then(res =>{
          const data=res.data
          const doctors=[]
          for(let key in data){
            const doctor=data[key]
            doctor.id=key
            doctors.push(doctor)
          }
          this.doctorList=doctors
        })
    }
}
</script>
<style>
.testMnil{
    padding-top: 4rem;
    padding-bottom: 0;
    font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
}
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
    border-radius: 5px;
}
.docpanelviewmore button:hover{
    background-color: rgb(236, 138, 52);
}

/* Doctor_Bar */

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
  padding-top: 7rem;
  padding-bottom: 5rem;
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