<template>
<section class="search-sec">
        <div class="container">
            <!-- <h1>{{ count }}</h1> -->
            <form action="#" method="post" novalidate="novalidate">
                <div class="row">
                    <div class="col-lg-12">
                        <div class="row">
                            <div class="col-lg-3 col-md-3 col-sm-12 p-0">
                                <input type="text" class="form-control search-slt" v-model="name" placeholder="Name">
                            </div>
                            <div class="col-lg-3 col-md-3 col-sm-12 p-0">
                                <input type="text" class="form-control search-slt" v-model="city" placeholder="City">
                            </div>
                            <div class="col-lg-3 col-md-3 col-sm-12 p-0">
                                <select class="form-control search-slt" id="exampleFormControlSelect1" v-model="speciality">
                                    <option value="ophthalomologist">Ophthalmologist</option>
                                    <option value="cardilogist">Cardilogist</option>
                                    <option value="Neuro Sergen">Neuro Sergen</option>
                                    <option value="Neuro Sergen">Neuro Sergen</option>
                                    <option value="Gynecologist">Gynecologist</option>
                                    <option value="Allergist">Allergist</option>
                                </select>
                            </div>
                            <div class="col-lg-3 col-md-3 col-sm-12 p-0">
                                <button type="button" class="btn btn-block wrn-btn" @click="onsubmit()">Search</button>
                            </div>
                        </div>
                    </div>
                </div>
            </form>
        </div>
    </section>    
</template>
<script>
export default {
    data:function(){
        return{
            name:null,
            city:null,
            speciality:null
        }
    },
    methods:{
        onsubmit(){
            this.$store.searchVals.name=this.name;
            this.$store.searchVals.city=this.name;
            this.$store.searchVals.speciality=this.name;
        }
    }
}
</script>
<style>
.search-sec{
    padding: 2rem;
}
.search-slt{
    display: block;
    width: 100%;
    font-size: 0.875rem;
    line-height: 1.5;
    color: #55595c;
    background-color: #fff;
    background-image: none;
    border: 1px solid #ccc;
    height: calc(3rem + 2px) !important;
}
.wrn-btn{
    width: 100%;
    font-size: 16px;
    font-weight: 400;
    text-transform: capitalize;
    height: calc(3rem + 2px) !important;
    background-color: rgb(243, 121, 14);
    color: white;
}
.wrn-btn:hover{
    color: white;
    background-color: rgb(236, 138, 52);
}
</style>