<template>
<div class="signup"> 
        <form action="#" class="formsign">
            <div class="form-group formitem">
            <label for="name">First Name</label>
            <input type="text" class="form-control" id="name" v-model="fname" ref="fname" required>
            </div>
            <div class="form-group formitem">
            <label for="lname">Last Name</label>
            <input type="text" class="form-control" id="lname" v-model="lname" ref="lname"  required>
            </div>
            <div class="form-group formitem">
            <label for="email">Email</label>
            <input type="email" class="form-control" id="email" v-model="email" @blur="$v.email.touch()" ref="email"  required>
            </div>
            <p class="warn" v-if="!$v.email.email">Please enter a valid email address</p>
            <!-- <p class="warn" v-if="!$v.email.required">This field must not be empty</p> -->
            <div class="form-group formitem">
              <label for="contact">Contact No</label>
              <input type="text" class="form-control" id="contact" v-model="contact" ref="contact"  required>
            </div>
            <div class="form-group formitem">
            <label for="pword">Password</label>
            <input type="password" class="form-control" @blur="$v.pword.touch()" id="pword" v-model="pword" ref="pword"  required>
            </div>
            <p class="warn" v-if="!$v.pword.minVal">Minimum number of characters are 3</p>
            <div class="form-group formitem lastman">
                <label for="cpword">Confirm Password</label>
                <input type="password" class="form-control" @blur="$v.cpword.touch()" id="cpword" v-model="cpword" ref="cpword"  required>
            </div>
            <p class="warn" v-if="!$v.cpword.minVal">Minimum number of characters are 3</p>
            <button type="button" class="btn btn-block joinformbtn" @click="sendPost()">Join</button>
        </form> 
        <div class="ar_mem">
            <a href="/login">Already a member? Sign In</a>
        </div>
    </div> 
</template>
<script>
import axios from 'axios'
import {required, email, minValue} from 'vuelidate/lib/validators'
export default {
    data:function(){
        return{
            fname:"",
            lname:"",
            email:"",
            contact:"",
            pword:"",
            cpword:"",
            userList:[],
        }
    },
    validations:{
        email:{
            required,
            email
        },
        pword:{
            minVal:minValue(6)
        },
        cpword:{
            minVal:minValue(6)
        }
    },
    methods:{
        sendPost(){
                const postData={username:this.email,first_name:this.fname,last_name:this.lname,email:this.email,password:this.cpword};
                // const postDataEx={user:(this.userList[this.userList.length-1].id), contact_no:this.contact};
                // axios.post('http://localhost:8001/api/register/',postData)
                //     .then(res=>console.log(res))
                //     .catch(error=>console.log(error))
                this.$store.dispatch('register',postData);
                window.location.href="/login";
        },
    },
    created(){
         axios.get('http://localhost:8001/doctors/doctors/')
        .then(res =>{
          const data=res.data
          const users=[]
          for(let key in data){
            const user=data[key]
            user.id=key
            users.push(user)
          }
          this.userList=users
        })
    }
}
</script>
<style>
.signup{
     display: flex; 
    flex: 1;
    width: 100%;
    margin-bottom: 3rem;
	flex-direction:column;
	align-items: center;
}
.signup label{
    font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
    font-size: 1rem;
    font-weight: 600;
    width: 10rem;
}
.formitem{
    display: flex;
    width: 30rem;
}
.signup form button{
    text-align: center;
    margin: auto;
    width: 50%;
}
.joinformbtn{
    text-align: center;
    color: white;
    background-color: rgb(243, 121, 14);;
}
.joinformbtn:hover{
    text-align: center;
    color: white;
    background-color: rgb(236, 138, 52);
}
.signup form .lastman{
    margin-bottom: 2rem;
}
.signup form .lastman input{
    height:38px;
}
.ar_mem{
    margin-top: 1.5rem;
    text-align: center;
    margin-left: auto;
    margin-right: auto;
    margin-bottom: 0.4rem;
    width: 20rem;
}
.warn{
    color: red;
    text-align: center;
}
</style>