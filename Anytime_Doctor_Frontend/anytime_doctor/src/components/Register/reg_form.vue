<template>
<div class="signup"> 
        <form action="#" class="formsign">
            <h5>{{this.mainEr}}</h5>
            <div class="form-group formitem">
            <label for="name">First Name</label>
            <input type="text" class="form-control" id="name" v-model="fname" ref="fname" required>
            <p>{{this.error1}}</p>
            </div>
            <div class="form-group formitem">
            <label for="lname">Last Name</label>
            <input type="text" class="form-control" id="lname" v-model="lname" ref="lname"  required>
            <p>{{this.error2}}</p>
            </div>
            <div class="form-group formitem">
            <label for="email">Email</label>
            <input type="email" class="form-control" id="email" v-model="email" ref="email"  required>
            <p>{{this.error3}}</p>
            </div>
            <div class="form-group formitem">
              <label for="contact">Contact No</label>
              <input type="text" class="form-control" id="contact" v-model="contact" ref="contact"  required>
              <p>{{this.error4}}</p>
            </div>
            <div class="form-group formitem">
            <label for="pword">Password</label>
            <input type="password" class="form-control" id="pword" v-model="pword" ref="pword"  required>
            <p>{{this.error5}}</p>
            </div>
            <div class="form-group formitem lastman">
                <label for="cpword">Confirm Password</label>
                <input type="password" class="form-control" id="cpword" v-model="cpword" ref="cpword"  required>
                <p>{{this.error6}}</p>
            </div>
            <button class="btn btn-block joinformbtn" @click="sendPost()">Join</button>
        </form> 
        <div class="ar_mem">
            <a href="login">Already a member? Sign In</a>
        </div>
    </div> 
</template>
<script>
import axios from 'axios'
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
            error1:"",
            error2:"",
            error3:"",
            error4:"",
            error5:"",
            error6:"",
            j:0,
            mainEr:"",
        }
    },
    methods:{
        sendPost(){
            this.validate();
            console.log("sendPost function starts");

            if(this.j==0){
                const postData={username:this.fname,first_name:this.fname,last_name:this.lname,email:this.email,password:this.cpword};
                const postDataEx={user:(this.userList[this.userList.length-1].id), contact_no:this.contact};
                axios.post('http://localhost:8001/accounts/users/',postData);
                axios.post('http://localhost:8001/accounts/usersEx/',postDataEx);
            }
            
        },
        validate(){
            this.j=0;
            console.log("validate function started");
            if(this.$refs.fname==null){
                this.error1="This field can't be empty"
            }
            if(this.$refs.lname==null){
                this.error2="This field can't be empty"
            }
            if(this.$refs.email==null){
                this.error3="This field can't be empty"
            }
            if(this.$refs.contact==null){
                this.error4="This field can't be empty"
            }
            if(this.$refs.pword==null){
                this.error5="This field can't be empty"
            }
            if(this.$refs.cpword==null){
                this.error6="This field can't be empty"
            }

            for(let i=0;i<this.userList.length;i++){
                    if(this.userList[i].email==this.email)
                    {
                        this.mainEr="Already Exist";
                        console.log("Already Exist");
                        this.j=1;
                    }
            }

            if(this.pword!=this.cpword){    
                this.mainEr="Password and Confirm Password are not matching. Please retry ";
                console.log("Passwords mismatching");
                this.j=1;
            }
        }
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
</style>