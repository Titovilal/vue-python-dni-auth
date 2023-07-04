<template>
    <div class="row justify-content-center">
      <div class="col-md-6">
        <h1 class="text-center mb-4 mt-5">Login Admin</h1>
  
        <form id="loginForm">
          <div class="mb-3">
            <label class="form-label">User</label>
            <input name="text" type="text" class="form-control" required />
          </div>
  
          <div class="mb-3">
            <label class="form-label">Password</label>
            <input
              name="password"
              type="password"
              class="form-control"
              required
            />
          </div>
  
          <div class="d-flex justify-content-between mt-4">
            <router-link to="/" class="btn btn-secondary"> Go back</router-link>
            <router-link to="/user-list" class="btn btn-primary">
              Login</router-link
            >
          </div>
        </form>
      </div>
    </div>
  </template>
  
  <script setup></script>
  
  <style lang="scss" scoped></style>
  