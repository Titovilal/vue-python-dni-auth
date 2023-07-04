<template>
  <div class="row justify-content-center">
    <div class="col-md-6">
      <h1 class="text-center mb-4 mt-5">Register</h1>

      <form id="registerForm" @submit.prevent="register">
        <div class="mb-3">
          <label class="form-label">User</label>
          <input
            v-model="username"
            name="username"
            type="text"
            class="form-control"
            required
          />
        </div>
        <div class="mb-3">
          <label class="form-label">Email</label>
          <input
            v-model="email"
            name="email"
            type="email"
            class="form-control"
            required
          />
        </div>

        <div class="mb-3">
          <label class="form-label">Password</label>
          <input
            v-model="password"
            name="password"
            type="password"
            class="form-control"
            required
          />
        </div>

        <div class="mb-3">
          <label class="form-label">Confirm Password</label>
          <input
            v-model="confirmPassword"
            name="confirmPassword"
            type="password"
            class="form-control"
            required
          />
        </div>

        <div class="d-flex justify-content-between mt-4">
          <router-link to="/" class="btn btn-secondary"> Go back</router-link>
          <button type="submit" class="btn btn-primary">Register</button>
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
      email: "",
      password: "",
      confirmPassword: "",
    };
  },
  methods: {
    register() {
      if (this.password !== this.confirmPassword) {
        alert("Passwords do not match");
        return;
      }
      fetch("http://localhost:5000/register", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify({
          username: this.username,
          email: this.email,
          password: this.password,
        }),
      })
        .then((resp) => resp.json())
        .then((data) => {
          if (data.success) {
            this.$router.push(`/user-details/${this.username}`);
          } else {
            alert(data.message);
          }
        })
        .catch((error) => {
          console.log(error);
        });
    },
  },
};
</script>

<style lang="scss" scoped></style>
