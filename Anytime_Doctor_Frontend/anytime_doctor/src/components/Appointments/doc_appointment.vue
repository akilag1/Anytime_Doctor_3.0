<template>
    <div class="confirm-form">
      <form action="#" method="POST">
        <h3>Patient's Name : Akila </h3>
        <h3>Doctor's Name : {{this.doctorList[this.id].name}} </h3>
        <h3>Hospital : {{this.hospitalList[this.doctorList[this.id].hospital_id].name}} </h3>
        <h3>date :  <input type="date" v-model="date" name="date" required> </h3>
        <h3>Time(4 p.m. - 10 p.m.) :  <input type="time" v-model="time" name="time" required> </h3>
        <h3>Patient Number : 4</h3>
        <div class="confirmapp_btn">
            <button class="btn btn-lg btn-primary">Go Back</button>
            <button class="btn btn-lg btn-primary" type="button" @click="sendPost()">Confirm</button>
        </div> 
      </form>  
    </div>
</template>
<script>
import axios from 'axios';
export default {
     data:function(){
        return{
          doctorList:[],
          hospitalList:[],
          date:"",
          time:"",
          id:this.$route.params.id,
        }   
    },
    methods:{
        sendPost(){
            const postData={doctor:this.doctorList[this.id].id,hospital:this.hospitalList[this.doctorList[this.id].hospital_id].id,date:this.date,time:this.time};
            axios.post('http://localhost:8001/appotests/doctor_appo/',postData)
              .then(res=>console.log(res))
              .catch(error=>console.log(error))
               this.$router.push('/dashboard')
        },
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