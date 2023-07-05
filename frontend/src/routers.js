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
    path: "/user-details/:username",
    name: "user-details",
    component: UserDetails,
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

router.beforeEach((to, from, next) => {
  const userToken = localStorage.getItem("userToken");
  const adminToken = localStorage.getItem("adminToken");
  const loggedInUsername = localStorage.getItem("loggedInUsername");

  if (
    to.name === "user-details" &&
    (!userToken || to.params.username !== loggedInUsername)
  ) {
    next({ name: "Login" });
  } else if (
    (to.name === "UserList" ||
      to.name === "ValidateUser" ||
      to.name === "validate-user") &&
    !adminToken
  ) {
    next({ name: "LoginAdmin" });
  } else {
    next();
  }
});

export default router;
