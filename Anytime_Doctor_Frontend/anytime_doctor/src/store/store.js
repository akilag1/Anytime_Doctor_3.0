import Vue from 'vue';
import Vuex from 'vuex';
import axios from 'axios'
import router from "../routes"; 

Vue.use(Vuex);

export default new Vuex.Store({
    state:{
        iDtoken:null,
        user_id:null
    },
    searchVals:{
        name:null,
        city:null,
        speciality:null,
    },
    mutations:{
        authUser(state,userData){
            state.iDtoken=userData.token
            state.user_id=userData.userid
        },
        clearAuthData(state){
            state.iDtoken=null;
            state.user_id=null;
            window.location.href="/"
        },
    },
    actions:{
        register({commit}, authData){
            axios.post('http://localhost:8001/api/register/',authData)
                .then(res=>{
                    console.log(res)
                    commit('authUser',{
                        token:res.data.data.token,
                        userid:res.data.data.user_id
                    })
                })
                .catch(error=>console.log(error))
        },
        login({commit}, authData){
            axios.post('http://localhost:8001/api/login/',authData)
                .then(res=>{
                    console.log(res)
                    commit('authUser',{
                        token:res.data.data.token,
                        userid:res.data.data.user_id
                    })
                    if(this.state.iDtoken!==null) {
                        this.$router.push('/');
                      }
                      else{
                        router.push('/login');
                      }
            })
             .catch(error=>console.log(error))
        },
        logout({commit}){
            commit('clearAuthData')
        },
        // onLinkClicked() {
        //     if(this.state.iDtoken!==null) {
        //       this.$router.push('/');
        //     }
        //     else{
        //         this.$router.push('/login');
        //     }
        //   }
    },
    getters:{
        isAuthenticated(state){
            return state.iDtoken!==null
        },
        serachVal(searchVals){
            return searchVals;
        }
    }
})