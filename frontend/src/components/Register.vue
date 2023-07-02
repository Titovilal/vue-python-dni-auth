<template>
  <div class="row justify-content-center">
    <div class="col-md-6">
      <h1 class="text-center mb-4 mt-5">Register</h1>

      <form id="registerForm">
        <div class="mb-3">
          <label class="form-label">User</label>
          <input name="user" type="text" class="form-control" required />
        </div>
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

        <div class="mb-3">
          <label class="form-label">Confirm Password</label>
          <input
            name="confirmPassword"
            type="password"
            class="form-control"
            required
          />
        </div>

        <div class="d-flex justify-content-end mt-4">
          <button type="submit" class="btn btn-primary">Register</button>
        </div>
      </form>
    </div>
  </div>
</template>

<script setup></script>

<style lang="scss" scoped></style>
