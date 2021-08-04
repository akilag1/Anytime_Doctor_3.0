<template>
<div>
<search></search>
 <section class="testimonials text-center bg-light testMnial">
    <div class="row">
        <div class="col-lg-4 docitem" v-for="doctor in doctorList" :key="doctor.id">
          <div class="testimonial-item mx-auto mb-5 mb-lg-0">
            <img class="img-fluid rounded-circle mb-3" :src=doctor.picture alt="">
            <router-link :to="'/doctors/' + doctor.id" tag="a"><h5>{{doctor.name}}</h5></router-link>
            <p class="font-weight-light mb-0 docpanelsubtext">{{doctor.speciality}}</p>
          </div>
        </div>
    </div>
 </section>      
</div>
</template>
<script>
import axios from 'axios';
import search from '../Basic/search.vue';
export default {
    components:{
      "search":search
    },
    data:function(){
        return{
          doctorList:[]
        }   
    },
    // watch:{
    //     'this.$store.state'(){

    //     }
    //   },
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
.docitem{
    margin-bottom: 2.5rem;
}
.testMnial{
    padding-top: 4rem;
    padding-bottom: 5rem;
    font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
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
  padding-top: 7rem;
  padding-bottom: 7rem;
}

.testimonials .testimonial-item {
  max-width: 18rem;
}

.testimonials .testimonial-item img {
  max-width: 12rem;
  box-shadow: 0px 5px 5px 0px #adb5bd;
}
</style>