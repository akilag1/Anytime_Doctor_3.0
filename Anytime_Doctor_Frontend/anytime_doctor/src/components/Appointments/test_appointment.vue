<template>
    <div class="confirm-form">
      <form action="#" method="POST">
        <h3>Patient's Name : </h3>
        <h3>Test :<br/><br/></h3>
        <h3>Hospital : </h3>
        <h3>date : <input type="date" name="date" required> </h3>
        <h3>Time(8 a.m. - 10 p.m.) : <input type="time" name="time" required> </h3>
        <h3>Patient Number : </h3>
        <div class="confirmapp_btn">
            <button class="btn btn-lg btn-primary">Go Back</button>
            <button class="btn btn-lg btn-primary">Confirm</button>
        </div>
      </form>  
    </div>
</template>
<script>
export default {
    
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