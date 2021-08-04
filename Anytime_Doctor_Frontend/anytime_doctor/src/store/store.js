import Vue from 'vue';
import Vuex from 'vuex';
// import axios from 'axios'

Vue.use(Vuex);

export default new Vuex.Store({
    state:{
        idToken:null,
        userId:null
    },
    // actions:{
    //     register({commit}, authData){
    //         axios.post('http://localhost:8001/api/register/',authData)
    //             .then(res=>console.log(res))
    //             .catch(error=>console.log(error))
    //     },
    // }
})