<template>
  <div class="container">
    <h1 class="text-center mb-4 mt-5">Validate User</h1>
    <div class="d-flex justify-content-start mb-3">
          <button type="button" class="btn btn-secondary">Go back</button>
        </div>
    <div class="row">
      <div class="col-md-8">
        <form id="accountform">
          <div class="card mb-3">
            <h5 class="card-header">User Details</h5>
            
            <div class="card-body">
              <!-- Aquí van los campos de entrada -->
              <div class="mb-3">
                <label class="form-label">First Name</label>
                <input
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
                  name="address"
                  type="text"
                  class="form-control"
                  disabled
                  required
                />
              </div>
              <div class="d-flex justify-content-center mt-4">
                <button type="button" class="btn btn-primary">
                  Validate User
                </button>
              </div>
            </div>
          </div>
        </form>
      </div>
      <div class="col-md-4">
        <div class="card mb-3">
          <h5 class="card-header">Photo</h5>
          <img src="photo1.jpg" class="card-img-top" alt="Photo 1" />
        </div>
        <div class="card mb-3">
          <h5 class="card-header">ID Card Front</h5>
          <img src="photo2.jpg" class="card-img-top" alt="Photo 2" />
        </div>
        <div class="card mb-3">
          <h5 class="card-header">ID Card Back</h5>
          <img src="photo3.jpg" class="card-img-top" alt="Photo 3" />
        </div>
      </div>
    </div>
  </div>
</template>

<script setup></script>

<style lang="scss" scoped></style>
