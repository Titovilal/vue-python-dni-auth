<template>
  <div class="row justify-content-center">
    <div class="col-md-6">
      <h1 class="text-center mb-4 mt-5">Login</h1>

      <form id="loginForm" @submit.prevent="login">
        <div class="mb-3">
          <label class="form-label">User</label>
          <input v-model="username" type="text" class="form-control" required />
        </div>

        <div class="mb-3">
          <label class="form-label">Password</label>
          <input
            v-model="password"
            type="password"
            class="form-control"
            required
          />
        </div>

        <div class="d-flex justify-content-between mt-4">
          <router-link to="/" class="btn btn-secondary"> Go back</router-link>
          <button type="submit" class="btn btn-primary">Login</button>
        </div>
      </form>
    </div>
  </div>
</template>

<script>
export default {
  data() {
    return {
      username: "",
      password: "",
    };
  },
  methods: {
    async login() {
      try {
        const response = await fetch("http://localhost:5000/login", {
          method: "POST",
          headers: {
            "Content-Type": "application/json",
          },
          body: JSON.stringify({
            username: this.username,
            password: this.password,
          }),
        });
        const data = await response.json();
        if (data.success) {
          this.$router.push(`/user-details/${this.username}`);
        } else {
          alert(data.message);
        }
      } catch (error) {
        console.log(error);
      }
    },
  },
};
</script>

<style lang="scss" scoped></style>
