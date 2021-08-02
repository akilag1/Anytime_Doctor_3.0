<template>
    <div>
     <div class="row" id="picfacts">
      <section id="pic" class="col-md-4">
          <img :src="this.hospitalList[this.id].picture" alt="">
      </section>
      <section id="facts" class="col-md-8">
          <div class="docfacts">
              <ul>
                <ul>
                  <div class="docfact_li">
                    <li>Hospital</li>
                    <p>{{this.hospitalList[this.id].name}}</p>
                  </div>
                  <div class="docfact_li">
                    <li>Location</li>
                    <p>{{this.hospitalList[this.id].location}}</p>
                  </div>
                  <div class="docfact_li">
                    <li>Tel_No </li>
                    <p>{{this.hospitalList[this.id].contact_no}}</p>
                  </div>
                  <div class="docfact_li">
                    <li>Email </li>
                    <p>{{this.hospitalList[this.id].email}}</p>
                  </div>
                </ul>              
              </ul>    
              <div class="tests_present">
                <h3>Tests Available</h3>
                <ul>
                    <li v-if="this.hospitalList[this.id].biopsy">Biopsy</li>
                    <li v-if="this.hospitalList[this.id].blood">Blood Count</li>
                    <li v-if="this.hospitalList[this.id].ecg">ECG</li>
                    <li v-if="this.hospitalList[this.id].ct">CT Scan</li>
                    <li v-if="this.hospitalList[this.id].angiogram">Angiogram</li>
                    <li v-if="this.hospitalList[this.id].ultra_sound">Ultra Sound</li>
                </ul>
              </div>        
          </div>
      </section>
    </div>
    
    <!-- description -->

    <div class="row" id="description"> 
        <div class="col-md-12 descri">
            <p>{{this.hospitalList[this.id].description}}</p>
        </div>
    </div>
   </div> 
</template>
<script>
import axios from 'axios'
export default {
     data:function(){
       return{
         hospitalList:[],
         id:this.$route.params.id,
       }
     },
     watch:{
       '$route'(to,from){
         this.id=from.params.id;
         this.id=to.params.id;
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
          this.hospitalList=hospitals
        })
    }
}
</script>
<style>
</style>