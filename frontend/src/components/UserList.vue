<template>
  <div class="container">
  <h1 class="text-center mb-4 mt-5">User List</h1>

  <div class="row">
    <div class="col-md-8 mx-auto">
      <div class="d-flex justify-content-start mb-3">
          <button type="button" class="btn btn-danger">Logout</button>
        </div>
      <div class="mb-3">
        <label for="search" class="form-label">Search:</label>
        <div class="input-group">
          <input type="text" class="form-control" id="search" />
          <button class="btn btn-outline-secondary" type="button">Search</button>
        </div>
      </div>

      <div class="mb-3 form-check">
        <input type="checkbox" class="form-check-input" id="hideValidated" />
        <label class="form-check-label" for="hideValidated">Hide Validated</label>
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
          <tr>
            <td>user1</td>
            <td>John</td>
            <td>Doe</td>
            <td>12345678A</td>
            <td>Yes</td>
            <td><button class="btn btn-primary float-end">Validate</button></td>
          </tr>
          <tr>
            <td>user2</td>
            <td>Jane</td>
            <td>Smith</td>
            <td>98765432B</td>
            <td>No</td>
            <td><button class="btn btn-primary float-end">Validate</button></td>
          </tr>
          <!-- Add more user rows here -->
        </tbody>
      </table>
    </div>
  </div>
</div>

</template>

<script setup></script>

<style lang="scss" scoped></style>
