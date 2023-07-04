<template>
  <div class="container">
    <h1 class="text-center mb-4 mt-5">Validate User</h1>
    <div class="d-flex justify-content-start mb-3">
      <router-link to="/user-list" class="btn btn-secondary">
        Go back
      </router-link>
    </div>
    <div class="row">
      <div class="col-md-8">
        <form id="accountform">
          <div class="card mb-3">
            <h5 class="card-header text-center">User Details</h5>

            <div class="card-body">
              <!-- Aquí van los campos de entrada -->
              <div class="mb-3">
                <label class="form-label">First Name</label>
                <input
                  v-model="user.name"
                  name="first_name"
                  type="text"
                  class="form-control"
                  required
                  disabled
                />
              </div>
              <div class="mb-3">
                <label class="form-label">Last Name</label>
                <input
                  v-model="user.surname"
                  name="last_name"
                  type="text"
                  class="form-control"
                  disabled
                  required
                />
              </div>
              <div class="mb-3">
                <label class="form-label">Email</label>
                <input
                  v-model="details.email"
                  name="email"
                  type="email"
                  class="form-control"
                  disabled
                  required
                />
              </div>
              <div class="mb-3">
                <label class="form-label">ID Card Number</label>
                <input
                  v-model="user.dni"
                  name="id_card"
                  type="text"
                  class="form-control"
                  disabled
                  required
                />
              </div>
              <div class="mb-3">
                <label class="form-label">Date of Birth</label>
                <input
                  v-model="details.birthdate"
                  name="date_of_birth"
                  type="date"
                  class="form-control"
                  disabled
                  required
                />
              </div>
              <div class="mb-3">
                <label class="form-label">Address</label>
                <input
                  v-model="details.address"
                  name="address"
                  type="text"
                  class="form-control"
                  disabled
                  required
                />
              </div>
              <div class="d-flex justify-content-center mt-4">
                <button
                  type="button"
                  class="btn btn-primary"
                  @click="validateUser"
                >
                  Validate User
                </button>
              </div>
            </div>
          </div>
        </form>
      </div>
      <div class="col-md-4">
        <div class="card mb-3">
          <h5 class="card-header text-center">User valid</h5>
          <div class="card-body text-center">
            {{ user.valid ? "Yes" : "No" }}
          </div>
        </div>
        <div class="card mb-3">
          <h5 class="card-header text-center">Photo</h5>
          <!-- Display the user's photo -->
          <img :src="'data:image/jpeg;base64,' + details.photo" alt="Photo" />
        </div>
        <div class="card mb-3">
          <h5 class="card-header text-center">ID Card Front</h5>
          <!-- Display the user's ID card front -->
          <img
            :src="'data:image/jpeg;base64,' + details.dni_front"
            alt="ID Card Front"
          />
        </div>
        <div class="card mb-3">
          <h5 class="card-header text-center">ID Card Back</h5>
          <!-- Display the user's ID card back -->
          <img
            :src="'data:image/jpeg;base64,' + details.dni_back"
            alt="ID Card Back"
          />
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  data() {
    return {
      user: {},
      details: {},
    };
  },
  methods: {
    getUser() {
      fetch(`http://localhost:5000/users/${this.$route.params.id}`, {
        method: "GET",
        headers: {
          "Content-Type": "application/json",
        },
      })
        .then((resp) => resp.json())
        .then((data) => {
          this.user = data;
        })
        .catch((error) => {
          console.log(error);
        });
    },
    getUserDetails() {
      fetch(`http://localhost:5000/users/${this.$route.params.id}/details`, {
        method: "GET",
        headers: {
          "Content-Type": "application/json",
        },
      })
        .then((resp) => resp.json())
        .then((data) => {
          this.details = data;
        })
        .catch((error) => {
          console.log(error);
        });
    },
    validateUser() {
      fetch(`http://localhost:5000/users/${this.$route.params.id}`, {
        method: "PUT",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify({ valid: true }),
      })
        .then((resp) => resp.json())
        .then((data) => {
          this.user = data;
        })
        .catch((error) => {
          console.log(error);
        });
    },
  },
  created() {
    this.getUser();
    this.getUserDetails();
  },
};
</script>

<style lang="scss" scoped></style>
