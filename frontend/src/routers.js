import { createRouter, createWebHistory } from "vue-router";
import Home from "./components/Home.vue";
import AdminUserList from "./components/admin/AdminUserList.vue";
import AdminUserListValidate from "./components/admin/AdminUserListValidate.vue";
import AdminLogin from "./components/admin/AdminLogin.vue";
import ClientDetails from "./components/client/ClientDetails.vue";
import ClientLogin from "./components/client/ClientLogin.vue";
import ClientRegister from "./components/client/ClientRegister.vue";

const routes = [
  {
    path: "/",
    name: "Home",
    component: Home,
  },
  {
    path: "/login/client",
    name: "ClientLogin",
    component: ClientLogin,
  },
  {
    path: "/user-list",
    name: "AdminUserList",
    component: AdminUserList,
  },
  {
    path: "/register",
    name: "ClientRegister",
    component: ClientRegister,
  },

  {
    path: "/user-details/:username",
    name: "ClientDetails",
    component: ClientDetails,
  },

  {
    path: "/validate-user/:id",
    name: "AdminUserListValidate",
    component: AdminUserListValidate,
    props: true,
  },
  {
    path: "/login/admin",
    name: "AdminLogin",
    component: AdminLogin,
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
    next({ name: "ClientLogin" });
  } else if (
    (to.name === "AdminUserList" ||
      to.name === "AdminUserListValidate" ||
      to.name === "validate-user") &&
    !adminToken
  ) {
    next({ name: "AdminLogin" });
  } else {
    next();
  }
});

export default router;
