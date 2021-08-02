<template>
   <div> 
     <!-- pic and facts -->
    <div class="row" id="picfacts">
      <section id="pic" class="col-md-4">
          <img :src="this.doctorList[this.id].picture" alt="">
      </section>
      <section id="facts" class="col-md-8">
          <div class="docfacts">
              <ul>
                <div class="docfact_li">
                  <li>Name</li>
                  <p>{{this.doctorList[this.id].name}}</p>
                </div>
                <div class="docfact_li">
                  <li>Speciality</li>
                  <p>{{this.doctorList[this.id].speciality}}</p>
                </div>
                <div class="docfact_li">
                  <li>Hospital</li>
                  <p>{{this.hospitalList[this.doctorList[this.id].hospital_id].name}}</p>
                </div>
                <div class="docfact_li">
                  <li>Email </li>
                  <p>{{this.doctorList[this.id].email}}</p>
                </div>
              </ul>              
          </div>
      </section>
    </div>


    <!-- description -->

    <div class="row" id="description"> 
        <div class="col-md-12 descri">
            <p>{{this.doctorList[this.id].description}}</p>
        </div>
    </div>
   </div> 
</template>

<script>
import axios from 'axios';
export default {
    data:function(){
      return{
        doctorList:[],
        hospitalList:[],
        id:this.$route.params.id
      }
    },
    watch:{
       '$route'(to,from){
         this.id=from.params.id;
         this.id=to.params.id;
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
        }),
         axios.get('http://localhost:8001/hospitals/hospitals/')
        .then(res =>{
          const data=res.data
          const hospitals=[]
          for(let key in data){
            const hospital=data[key]
            hospital.id=key
            hospitals.push(hospital)
          }
          this.hospitalList=hospitals
        })
    }
}
</script>

<style>
#pic img{
    width: 100%;
    height: 100%;
    /* border-radius: 50%; */
}
#picfacts{
    margin-top: 4rem;
    margin-left: 4rem;
    margin-right: 4rem;
    margin-bottom: 4rem;
}
#description{
    margin: 3rem;
}
#facts ul{
    list-style: none;
}
#facts ul li{
    font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
    font-size: 2rem;
    background-color: rgb(240, 163, 75);
    width: 10rem;
    text-align: right;
    border-bottom:  #fff solid 2px;
    padding-right: 1rem;
    /* margin-bottom: 1rem; */
}
#facts .docfact_li{
    display: flex;
}
#facts .docfact_li p{
    background-color: rgb(224, 167, 114);
    font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
    font-size: 1.5rem;
    width: 30rem;
    margin-bottom: 0;
    height: 3rem;
    text-align: left;
    padding-left: 2rem;
    /* text-transform: uppercase; */
}
</style>