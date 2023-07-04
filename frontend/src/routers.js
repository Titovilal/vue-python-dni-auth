import { createRouter, createWebHistory } from "vue-router";
import Login from "./components/Login.vue";
import UserList from "./components/UserList.vue";
import Start from "./components/Start.vue";
import Register from "./components/Register.vue";
import UserDetails from "./components/UserDetails.vue";
import ValidateUser from "./components/ValidateUser.vue";
import LoginAdmin from "./components/LoginAdmin.vue";

const routes = [
  {
    path: "/",
    name: "Start",
    component: Start,
  },
  {
    path: "/login",
    name: "Login",
    component: Login,
  },
  {
    path: "/user-list",
    name: "UserList",
    component: UserList,
  },
  {
    path: "/register",
    name: "Register",
    component: Register,
  },
  {
    path: "/user-details",
    name: "UserDetails",
    component: UserDetails,
  },
  {
    path: "/user-details/:username",
    name: "user-details",
    component: UserDetails,
  },
  {
    path: "/validate-user",
    name: "ValidateUser",
    component: ValidateUser,
  },
  {
    path: "/validate-user/:id",
    name: "validate-user",
    component: ValidateUser,
    props: true,
  },
  {
    path: "/login-admin",
    name: "LoginAdmin",
    component: LoginAdmin,
  },
];

const router = createRouter({
  history: createWebHistory(),
  routes,
});

export default router;
