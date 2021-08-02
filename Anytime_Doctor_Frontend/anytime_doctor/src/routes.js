import home from './pages/home.vue';
import doctors from './pages/doctors.vue';
import join from './pages/join.vue';
import hospitals from './pages/hospitals.vue';
import doc_avatar from './components/Doctors/doc_avatar.vue';
import doc_profile from './components/Doctors/doc_profile.vue';
import hosp_avatar from './components/Hospitals/hosp_avatar.vue';
import hosp_profile from './components/Hospitals/hosp_profile.vue';

export const routes=[
    { path: '', component: home },
    { path: '/doctors', component: doctors ,children:[
        {path: '', component: doc_avatar},
        {path: ':id', component: doc_profile}
    ]},
    { path: '/register', component: join },
    { path: '/hospitals', component: hospitals, children:[
        {path: '', component: hosp_avatar},
        {path: ':id', component: hosp_profile}
    ] },
]
