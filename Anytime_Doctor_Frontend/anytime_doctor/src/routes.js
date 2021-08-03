import home from './pages/home.vue';
import doctors from './pages/doctors.vue';
import join from './pages/join.vue';
import hospitals from './pages/hospitals.vue';
import doc_avatar from './components/Doctors/doc_avatar.vue';
import doc_profile from './components/Doctors/doc_profile.vue';
import hosp_avatar from './components/Hospitals/hosp_avatar.vue';
import hosp_profile from './components/Hospitals/hosp_profile.vue';
import dashboard from './pages/dashboard.vue';
import available_doc from './components/Doctors/available_doc.vue';
import online_doc from './components/Doctors/online_doc.vue';
import test_available from './components/Hospitals/test_available.vue';
import doc_appointment from './components/Appointments/doc_appointment.vue';
import test_appointment from './components/Appointments/test_appointment.vue';

export const routes=[
    { path: '', component: home },
    { path: '/doctors', component: doctors ,children:[
        {path: '', component: doc_avatar},
        {path: 'available', component: available_doc},
        {path: 'online_available', component: online_doc},
        {path: ':id', component: doc_profile},
        {path: 'available/:id', component: doc_appointment},
    ]},
    { path: '/register', component: join },
    { path: '/hospitals', component: hospitals, children:[
        {path: '', component: hosp_avatar},
        {path: 'test_available', component: test_available},
        {path: ':id', component: hosp_profile},
        {path: 'test_available/:id', component: test_appointment},
    ] },
    { path: '/dashboard', component: dashboard },
]
