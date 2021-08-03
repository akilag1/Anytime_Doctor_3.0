<template>
    <div class="confirm-form">
      <form action="#" method="POST">
        <h3>Patient's Name : Akila</h3>
        <h3>Available Tests :
                    <li v-if="this.hospitalList[this.id].biopsy">Biopsy <input type="radio" v-model="testR" name="testR" value="biopsy"></li>
                    <li v-if="this.hospitalList[this.id].blood">Blood Count <input type="radio" v-model="testR" name="testR"></li>
                    <li v-if="this.hospitalList[this.id].ecg">ECG <input type="radio" v-model="testR" name="testR"></li>
                    <li v-if="this.hospitalList[this.id].ct">CT Scan <input type="radio" v-model="testR" name="testR"></li>
                    <li v-if="this.hospitalList[this.id].angiogram">Angiogram <input type="radio" v-model="testR" name="testR"></li>
                    <li v-if="this.hospitalList[this.id].ultra_sound">Ultra Sound <input type="radio" v-model="testR" name="testR"></li>
        </h3>
        <h3>Hospital : {{this.hospitalList[id].name}} </h3>
        <h3>date : <input type="date" v-model="date" name="date" required> </h3>
        <h3>Time(8 a.m. - 10 p.m.) : <input type="time" v-model="time" name="time" required> </h3>
        <h3>Patient Number : 3 </h3>
        <h3>test selected: {{this.testR}}</h3>
        <div class="confirmapp_btn">
            <button class="btn btn-lg btn-primary">Go Back</button>
            <button class="btn btn-lg btn-primary">Confirm</button>
        </div>
      </form>  
    </div>
</template>
<script>
import axios from 'axios'
export default {
    data:function(){
        return{
          hospitalList:[],
          id:this.$route.params.id,
          testR:"",
          date:"",
          time:""
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
.confirm-form{
    display: flex;
    flex-direction: column;
    margin-left: 20rem;
    margin-top: 4rem;
    margin-bottom: 3rem;
}
.confirm-form h3{
    font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
    margin: 1rem;
}
.confirmapp_btn{
    text-align: center;
}
.confirmapp_btn button{
     margin-right: 1.5rem;
}
</style>