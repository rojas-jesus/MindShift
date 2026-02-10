<template>
  <div class="container mt-5">
    <div class="row">
      <div class="col-12">
        <div class="card">
          <div class="card-header">
            <h2>Dashboard</h2>
          </div>
          <div class="card-body">
            <p>Welcome to your dashboard! You are successfully logged in.</p>
            <div class="alert alert-success">
              <strong>Success!</strong> Authentication is working correctly.
            </div>
            <button class="btn btn-primary" @click="$router.push('/')">Back to Home</button>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">
// Dashboard component logic can be added here
</script>
