<template>
  <div class="container mt-5">
    <div class="row justify-content-center">
      <div class="col-md-8 text-center">
        <h1 class="mb-4">Welcome to MindShift</h1>
        <p class="lead mb-5">Your personal platform for growth and transformation</p>
        
        <div v-if="!isAuthenticated" class="d-grid gap-2 d-md-flex justify-content-md-center">
          <router-link to="/login" class="btn btn-primary btn-lg px-4 me-md-2">
            Login
          </router-link>
          <router-link to="/register" class="btn btn-outline-secondary btn-lg px-4">
            Register
          </router-link>
        </div>
        
        <div v-else class="d-grid gap-2 d-md-flex justify-content-md-center">
          <button class="btn btn-success btn-lg px-4 me-md-2" @click="goToDashboard">
            Dashboard
          </button>
          <button class="btn btn-danger btn-lg px-4" @click="handleLogout">
            Logout
          </button>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">
import { ref, onMounted } from 'vue';
import { useRouter } from 'vue-router';
import { authService } from '../services/auth';

const router = useRouter();
const isAuthenticated = ref(false);

onMounted(() => {
  isAuthenticated.value = authService.isAuthenticated();
});

const goToDashboard = () => {
  router.push('/dashboard');
};

const handleLogout = () => {
  authService.logout();
  isAuthenticated.value = false;
  router.push('/');
};
</script>
