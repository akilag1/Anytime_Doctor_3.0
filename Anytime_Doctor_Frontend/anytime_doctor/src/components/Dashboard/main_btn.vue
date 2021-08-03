<template>
<div class="row contentrow">
     <div class="col-md-12 basicBtn">
          <div class="row">
            <router-link to="/doctors/online_available" tag="a"><button class="btn btn-primary btn-lg keyBtn">Contact Doctor with Video Chat</button></router-link>
          </div>  
          <div class="row">
            <router-link to="/doctors/available" tag="a"><button class="btn btn-primary btn-lg keyBtn">Contact Doctor in Person</button></router-link>
          </div> 
          <div class="row">
            <router-link to="/hospitals/test_available" tag="a"><button class="btn btn-primary btn-lg keyBtn">Schedule Test</button></router-link>
          </div> 
     </div>
</div>    
</template>
<script>
export default {
    
}
</script>
<style>
.contentrow{
    margin-top: 2rem;
    text-align: center;
    margin-bottom: 2rem;
}
.basicBtn{
    display: flex;
    flex-direction: column;
    align-items: center;
}
.keyBtn{
    width: 24rem;
    height: 6rem;
    margin-bottom: 10px;
    font-size: 1.5rem;
}
</style>