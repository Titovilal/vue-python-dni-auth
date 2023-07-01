<template>
    <div class="row justify-content-center">
      <div class="col-md-6">
        <h1 class="text-center mb-4 mt-5">Login</h1>
  
        <form id="loginForm">
          <div class="mb-3">
            <label class="form-label">Email</label>
            <input name="email" type="email" class="form-control" required />
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
  
          <div class="d-flex justify-content-start">
            <button type="submit" class="btn btn-primary">Login</button>
          </div>
        </form>
      </div>
    </div>
  </template>
  
  <script setup></script>
  
  <style lang="scss" scoped></style>
  