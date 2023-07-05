<template>
  <div class="row justify-content-center">
    <div class="col-md-8">
      <h1 class="text-center mb-4 mt-5">User Details</h1>

      <form id="accountform" @submit.prevent="saveDataToDatabase">
        <div class="d-flex justify-content-between mb-3">
          <router-link to="/" class="btn btn-danger" @click="clearLocalStorage">
            Logout</router-link
          >
          <div>
            <button type="button" class="btn btn-primary" @click="modifyData">
              Modify Data
            </button>
            &nbsp;&nbsp;
            <button type="submit" class="btn btn-primary" @click="saveData">
              Save Data
            </button>
          </div>
        </div>

        <div class="row mb-3">
          <div class="col-md-6">
            <label class="form-label">First Name</label>
            <input
              v-model="user.name"
              name="first_name"
              type="text"
              class="form-control"
              required
              :disabled="isDisabled"
            />
          </div>
          <div class="col-md-6">
            <label class="form-label">Last Name</label>
            <input
              v-model="user.surname"
              name="last_name"
              type="text"
              class="form-control"
              :disabled="isDisabled"
              required
            />
          </div>
        </div>

        <div class="row mb-3">
          <div class="col-md-6">
            <label class="form-label">ID Card Number</label>
            <input
              v-model="user.dni"
              name="id_card"
              type="text"
              class="form-control"
              :disabled="isDisabled"
              required
            />
          </div>
          <div class="col-md-6">
            <label class="form-label">Date of Birth</label>
            <input
              v-model="details.birthdate"
              name="date_of_birth"
              type="date"
              class="form-control"
              :disabled="isDisabled"
              required
            />
          </div>
        </div>

        <div class="mb-3">
          <label class="form-label">Email</label>
          <input
            v-model="details.email"
            name="email"
            type="email"
            class="form-control"
            :disabled="isDisabled"
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
            :disabled="isDisabled"
            required
          />
        </div>

        <div class="row mb-3">
          <label class="form-label"
            >Upload Photo<span v-if="photoUploaded"
              >. You have the last photo uploaded to the database
            </span></label
          >
          <input
            name="photo"
            type="file"
            class="form-control"
            required
            :disabled="isDisabled"
            @change="handleFileUpload($event, 'photo')"
          />
        </div>
        <div class="row mb-3">
          <label class="form-label"
            >Upload ID Card (Front)<span v-if="idCardFrontUploaded"
              >. You have the last photo uploaded to the database
            </span></label
          >
          <input
            name="id_card_front"
            type="file"
            class="form-control"
            :disabled="isDisabled"
            required
            @change="handleFileUpload($event, 'id_card_front')"
          />
        </div>
        <div class="row mb-3">
          <label class="form-label"
            >Upload ID Card (Back)<span v-if="idCardBackUploaded"
              >. You have the last photo uploaded to the database
            </span></label
          >
          <input
            name="id_card_back"
            type="file"
            class="form-control"
            :disabled="isDisabled"
            required
            @change="handleFileUpload($event, 'id_card_back')"
          />
        </div>
      </form>
    </div>
  </div>
  <br />
  <br />
</template>

<script>
export default {
  data() {
    return {
      user: {},
      details: {},
      isDisabled: true,
      photoUploaded: false,
      idCardFrontUploaded: false,
      idCardBackUploaded: false,
    };
  },
  methods: {
    handleFileUpload(event, key) {
      const file = event.target.files[0];
      const reader = new FileReader();
      reader.onload = (e) => {
        this.details[key] = e.target.result;
      };
      reader.readAsDataURL(file);
    },

    clearLocalStorage() {
      localStorage.clear();
    },

    async saveDataToDatabase() {
      fetch(`http://localhost:5000/users/${this.user.id}`, {
        method: "PUT",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify(this.user),
      })
        .then((resp) => resp.json())
        .then((data) => {
          console.log("User data updated:", data);
        })
        .catch((error) => {
          console.log(error);
        });
      fetch(`http://localhost:5000/users/${this.user.id}/details`, {
        method: "PUT",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify(this.details),
      })
        .then((resp) => resp.json())
        .then((data) => {
          console.log("User details updated:", data);
        })
        .catch((error) => {
          console.log(error);
        });
    },

    getUser() {
      fetch(`http://localhost:5000/users/${this.$route.params.username}`)
        .then((resp) => resp.json())
        .then((data) => {
          this.user = data;
          this.getUserDetails(data.id);
        })
        .catch((error) => {
          console.log(error);
        });
    },

    getUserDetails(id) {
      fetch(`http://localhost:5000/users/${id}/details`)
        .then((resp) => resp.json())
        .then((data) => {
          this.details = data;
          this.photoUploaded = !!data.photo;
          this.idCardFrontUploaded = !!data.dni_front;
          this.idCardBackUploaded = !!data.dni_back;
          this.details.photo = null;
          this.details.dni_front = null;
          this.details.dni_back = null;
        })
        .catch((error) => {
          console.log(error);
        });
    },

    modifyData() {
      this.isDisabled = false;
    },

    saveData() {
      this.isDisabled = true;
      this.saveDataToDatabase();
    },
  },
  created() {
    this.getUser();
  },
};
</script>
<style scoped></style>
