<template>
  <div class="container mt-5">
    <div class="row justify-content-center">
      <div class="col-md-6 col-lg-5">
        <div class="card shadow">
          <div class="card-body">
            <h3 class="card-title text-center mb-4">Register</h3>
            
            <div v-if="error" class="alert alert-danger" role="alert">
              <div v-for="(err, field) in error" :key="field">
                <strong>{{ field }}:</strong> {{ Array.isArray(err) ? err.join(', ') : err }}
              </div>
            </div>
            
            <div v-if="successMessage" class="alert alert-success" role="alert">
              {{ successMessage }}
            </div>
            
            <form @submit.prevent="handleRegister">
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
                <label for="email" class="form-label">Email</label>
                <input
                  type="email"
                  class="form-control"
                  id="email"
                  v-model="email"
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
              
              <div class="mb-3">
                <label for="password2" class="form-label">Confirm Password</label>
                <input
                  type="password"
                  class="form-control"
                  id="password2"
                  v-model="password2"
                  required
                  :disabled="loading"
                />
                <div v-if="password && password2 && password !== password2" class="text-danger small mt-1">
                  Passwords do not match
                </div>
              </div>
              
              <div class="d-grid">
                <button 
                  type="submit" 
                  class="btn btn-primary" 
                  :disabled="loading || (password && password2 && password !== password2)"
                >
                  <span v-if="loading" class="spinner-border spinner-border-sm me-2" role="status" aria-hidden="true"></span>
                  {{ loading ? 'Registering...' : 'Register' }}
                </button>
              </div>
            </form>
            
            <div class="text-center mt-3">
              <p>Already have an account? <router-link to="/login">Login here</router-link></p>
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
const email = ref('');
const password = ref('');
const password2 = ref('');
const error = ref<any>(null);
const successMessage = ref('');
const loading = ref(false);

const handleRegister = async () => {
  try {
    loading.value = true;
    error.value = null;
    successMessage.value = '';
    
    await authService.register(username.value, email.value, password.value, password2.value);
    
    successMessage.value = 'Registration successful! You can now login.';
    
    setTimeout(() => {
      router.push('/login');
    }, 2000);
    
  } catch (err: any) {
    error.value = err.response?.data || 'Registration failed. Please try again.';
  } finally {
    loading.value = false;
  }
};
</script>
