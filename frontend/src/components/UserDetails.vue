<script setup></script>

<template>
  <div class="row justify-content-center">
    <div class="col-md-8">
      <h1 class="text-center mb-4 mt-5">User Details</h1>

      <form id="accountform">
        <div class="d-flex justify-content-start mb-3">
          <button type="button" class="btn btn-danger">Logout</button>
        </div>

        <div class="row mb-3">
          <div class="col-md-6">
            <label class="form-label">First Name</label>
            <input
              name="first_name"
              type="text"
              class="form-control"
              required
              disabled
            />
          </div>
          <div class="col-md-6">
            <label class="form-label">Last Name</label>
            <input
              name="last_name"
              type="text"
              class="form-control"
              disabled
              required
            />
          </div>
        </div>

        <div class="row mb-3">
          <div class="col-md-6">
            <label class="form-label">ID Card Number</label>
            <input
              name="id_card"
              type="text"
              class="form-control"
              disabled
              required
            />
          </div>
          <div class="col-md-6">
            <label class="form-label">Date of Birth</label>
            <input
              name="date_of_birth"
              type="date"
              class="form-control"
              disabled
              required
            />
          </div>
        </div>

        <div class="mb-3">
          <label class="form-label">Email</label>
          <input
            name="email"
            type="email"
            class="form-control"
            disabled
            required
          />
        </div>

        <div class="mb-3">
          <label class="form-label">Address</label>
          <input
            name="address"
            type="text"
            class="form-control"
            disabled
            required
          />
        </div>

        <div class="mb-3">
          <label class="form-label">Upload Photo</label>
          <input
            name="photo"
            type="file"
            class="form-control"
            required
            disabled
          />
        </div>

        <div class="row mb-3">
          <div class="col-md-6">
            <label class="form-label">Upload ID Card (Front)</label>
            <input
              name="id_card_front"
              type="file"
              class="form-control"
              disabled
              required
            />
          </div>
          <div class="col-md-6">
            <label class="form-label">Upload ID Card (Back)</label>
            <input
              name="id_card_back"
              type="file"
              class="form-control"
              disabled
              required
            />
          </div>
        </div>

        <div class="d-flex justify-content-between mt-4">
          <button type="button" class="btn btn-primary">Modify Data</button>
          <button type="submit" class="btn btn-primary">Save Data</button>
        </div>
      </form>
    </div>
  </div>
</template>

<style scoped></style>
