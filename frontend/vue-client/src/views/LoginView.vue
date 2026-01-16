<template>
  <div class="container mt-5">
    <div class="row justify-content-center">
      <div class="col-md-6 col-lg-4">
        <div class="card shadow">
          <div class="card-body">
            <h3 class="card-title text-center mb-4">Login</h3>
            
            <div v-if="error" class="alert alert-danger" role="alert">
              {{ error }}
            </div>
            
            <form @submit.prevent="handleLogin">
              <div class="mb-3">
                <label for="username" class="form-label">Username</label>
                <input
                  type="text"
                  class="form-control"
                  id="username"
                  v-model="username"
                  required
                  :disabled="loading"
                />
              </div>
              
              <div class="mb-3">
                <label for="password" class="form-label">Password</label>
                <input
                  type="password"
                  class="form-control"
                  id="password"
                  v-model="password"
                  required
                  :disabled="loading"
                />
              </div>
              
              <div class="d-grid">
                <button type="submit" class="btn btn-primary" :disabled="loading">
                  <span v-if="loading" class="spinner-border spinner-border-sm me-2" role="status" aria-hidden="true"></span>
                  {{ loading ? 'Logging in...' : 'Login' }}
                </button>
              </div>
            </form>
            
            <div class="text-center mt-3">
              <p>Don't have an account? <router-link to="/register">Register here</router-link></p>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">
import { ref } from 'vue';
import { useRouter } from 'vue-router';
import { authService } from '../services/auth';

const router = useRouter();
const username = ref('');
const password = ref('');
const error = ref('');
const loading = ref(false);

const handleLogin = async () => {
  try {
    loading.value = true;
    error.value = '';
    
    await authService.login(username.value, password.value);
    
    router.push('/');
  } catch (err: any) {
    error.value = err.response?.data?.detail || 'Login failed. Please check your credentials.';
  } finally {
    loading.value = false;
  }
};
</script>
