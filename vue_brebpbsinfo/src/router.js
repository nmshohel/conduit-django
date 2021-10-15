import Vue from 'vue';
import Router from 'vue-router';
import Home from './views/Home.vue';
import Login from './views/Login.vue';
import Register from './views/Register.vue';
import Netmeterrpt from './views/netmeterrpt.vue';
import solarrpt from './views/solarrpt.vue';
import cstationrpt from './views/cstationrpt.vue';

Vue.use(Router);

export const router = new Router({
  mode: 'history',
  routes: [
    {
      path: '/',
      name: 'home',
      component: Home
    },
    {
      path: '/home',
      component: Home
    },
    {
      path: '/netmeterrpt',
      component: Netmeterrpt
    },
    {
      path: '/solarrpt',
      component: solarrpt
    },
     {
      path: '/cstationrpt',
      component: cstationrpt
    },
    {
      path: '/login',
      component: Login
    },
    {
      path: '/register',
      component: Register
    },
    {
      path: '/profile',
      name: 'profile',
      // lazy-loaded
      component: () => import('./views/Profile.vue')
    },
    {
      path: '/admin',
      name: 'admin',
      // lazy-loaded
      component: () => import('./views/BoardAdmin.vue')
    },
    {
      path: '/mod',
      name: 'moderator',
      // lazy-loaded
      component: () => import('./views/BoardModerator.vue')
    },
    {
      path: '/user',
      name: 'user',
      // lazy-loaded
      component: () => import('./views/BoardUser.vue')
    },
    {
      path: "/netmeterlist",
      name: "netmeterlist",
      component: () => import("./components/NetmeterList")
    },
    {
      path: "/netmeterlist/:id",
      name: "netmeter-details",
      component: () => import("./components/NetMeter")
    },
    {
      path: "/addnetmeter",
      name: "addnetmeter",
      component: () => import("./components/AddNetmeter")
    },
    {
      path: "/addchargestation",
      name: "addchargestation",
      component: () => import("./components/AddChargestation")
    },
    {
      path: "/tutorials",
      name: "tutorials",
      component: () => import("./components/TutorialsList")
    },
           {
      path: "/addsolar",
      name: "addsolar",
      component: () => import("./components/AddSolar")
    },
  ]
});

router.beforeEach((to, from, next) => {
  const publicPages = ['/login', '/register'];
  const authRequired = !publicPages.includes(to.path);
  const loggedIn = localStorage.getItem('user');

  // trying to access a restricted page + not logged in
  // redirect to login page
  if (authRequired && !loggedIn) {
    next('/login');
  } else {
    next();
  }
});