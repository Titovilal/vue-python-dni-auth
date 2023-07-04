<template>
  <div class="container">
    <h1 class="text-center mb-4 mt-5">User List</h1>

    <div class="row">
      <div class="col-md-8 mx-auto">
        <div class="d-flex justify-content-start mb-3">
          <router-link to="/" class="btn btn-danger"> Logout</router-link>
        </div>
        <div class="mb-3">
          <label for="search" class="form-label">Search:</label>
          <div class="input-group">
            <input type="text" class="form-control" placeholder="You can search by user, name, last name or dni" id="search" />
            <button class="btn btn-outline-secondary" type="button">
              Search
            </button>
          </div>
        </div>

        <div class="mb-3 form-check">
          <input
            type="checkbox"
            class="form-check-input"
            id="hideValidated"
            v-model="hideValidated"
          />
          <label class="form-check-label" for="hideValidated"
            >Hide Validated</label
          >
        </div>

        <table class="table table-striped">
          <thead>
            <tr>
              <th>User</th>
              <th>Name</th>
              <th>Last Name</th>
           
              <th>DNI</th>
              <th>Valid</th>
            </tr>
          </thead>
          <tbody>
            <!-- Loop through the filteredUsers array and create a table row for each user -->
            <tr v-for="user in filteredUsers" :key="user.id">
              <td>{{ user.user }}</td>
              <td>{{ user.name }}</td>
              <td>{{ user.surname }}</td>
            
              <td>{{ user.dni }}</td>
              <td>{{ user.valid ? "Yes" : "No" }}</td>
              <td>
                <!-- Pass the user object as a prop to the validate-user route -->
                <router-link
                  :to="'/validate-user/' + user.id"
                  class="btn btn-primary float-end"
                >
                  Validate
                </router-link>
              </td>
            </tr>
          </tbody>
        </table>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  data() {
    return {
      users: [],
      hideValidated: false,
    };
  },

  computed: {
    filteredUsers() {
      if (this.hideValidated) {
        return this.users.filter((user) => !user.valid);
      } else {
        return this.users;
      }
    },
  },

  methods: {
    getUsers() {
      const searchValue = document.querySelector("#search").value;
      fetch("http://localhost:5000/users", {
        method: "GET",
        headers: {
          "Content-Type": "application/json",
        },
      })
        .then((resp) => resp.json())
        .then((data) => {
          this.users = data.filter((user) =>
            [user.user, user.name, user.surname, user.username, user.dni]
              .join(" ")
              .toLowerCase()
              .includes(searchValue.toLowerCase())
          );

          localStorage.setItem("users", JSON.stringify(this.users));
        })
        .catch((error) => {
          console.log(error);
        });
    },
  },

  mounted() {
    document
      .querySelector("button[type='button']")
      .addEventListener("click", this.getUsers);
    document.querySelector("#search").addEventListener("input", this.getUsers);

    const users = JSON.parse(localStorage.getItem("users"));
    if (users) {
      this.users = users;
    } else {
      this.getUsers();
    }
  },
};
</script>

<style lang="scss" scoped></style>
