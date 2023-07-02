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

  
  <div id="app">
    <Start />
    <router-view/>
  </div>
</template>

<style scoped></style>
