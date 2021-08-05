import Vue from 'vue';
import Vuex from 'vuex';
import axios from 'axios'
// import routes from '../routes'

Vue.use(Vuex);

export default new Vuex.Store({
    state:{
        iDtoken:null,
    },
    searchVals:{
        name:null,
        city:null,
        speciality:null,
    },
    mutations:{
        authUser(state,userData){
            state.iDtoken=userData.token
        },
        clearAuthData(state){
            state.iDtoken=null
        },
    },
    actions:{
        register({commit}, authData){
            axios.post('http://localhost:8001/api/register/',authData)
                .then(res=>{
                    console.log(res)
                    commit('authUser',{
                        token:res.data.token
                    })
                })
                .catch(error=>console.log(error))
        },
        login({commit}, authData){
            axios.post('http://localhost:8001/api/login/',authData)
                .then(res=>{
                    console.log(res)
                    commit('authUser',{
                        token:res.data.token
                    })
            })
             .catch(error=>console.log(error))
            this.getters.onLinkClicked
        },
        logout({commit}){
            commit('clearAuthData')
        },
        onLinkClicked() {
            if(this.state.iDtoken!==null) {
              this.$router.push('/');
            }
            else{
                this.$router.push('/login');
            }
          }
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