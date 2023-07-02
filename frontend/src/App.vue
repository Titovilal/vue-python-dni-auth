<script setup>
import Login from "./components/Login.vue";
import UserList from "./components/UserList.vue";
import Start from "./components/Start.vue";
import Register from "./components/Register.vue";
import UserDetails from "./components/UserDetails.vue";
import ValidateUser from "./components/ValidateUser.vue";
</script>

<template>
  <!-- <Navbar msg="Vite + Vue" />-->

  <Start />
  <hr />
  <Register />
  <hr />
  <Login />
  <hr />
  <UserList />
  <hr />
  <UserDetails />
  <hr />
  <ValidateUser />
</template>

<style scoped></style>
