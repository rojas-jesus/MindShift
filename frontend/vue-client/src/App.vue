<script setup lang="ts">
import { RouterLink, RouterView } from 'vue-router'
import { ref, onMounted } from 'vue'
import { authService } from './services/auth'

const isAuthenticated = ref(false)

onMounted(() => {
  isAuthenticated.value = authService.isAuthenticated()
})
</script>

<template>
  <nav class="navbar navbar-expand-lg navbar-dark bg-dark">
    <div class="container-fluid">
      <RouterLink class="navbar-brand" to="/">MindShift</RouterLink>
      
      <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarNav">
        <span class="navbar-toggler-icon"></span>
      </button>
      
      <div class="collapse navbar-collapse" id="navbarNav">
        <ul class="navbar-nav me-auto">
          <li class="nav-item">
            <RouterLink class="nav-link" to="/">Home</RouterLink>
          </li>
          <li class="nav-item">
            <RouterLink class="nav-link" to="/about">About</RouterLink>
          </li>
          <li class="nav-item">
            <RouterLink class="nav-link" to="/main-dashboard">Dashboard</RouterLink>
          </li>
        </ul>
        
        <ul class="navbar-nav">
          <template v-if="!isAuthenticated">
            <li class="nav-item">
              <RouterLink class="nav-link" to="/login">Login</RouterLink>
            </li>
            <li class="nav-item">
              <RouterLink class="nav-link" to="/register">Register</RouterLink>
            </li>
          </template>
          <template v-else>
            <li class="nav-item">
              <button class="btn btn-success btn-sm me-2" @click="$router.push('/main-dashboard')">Dashboard</button>
            </li>
            <li class="nav-item">
              <button class="btn btn-danger btn-sm" @click="authService.logout(); isAuthenticated = false; $router.push('/')">Logout</button>
            </li>
          </template>
        </ul>
      </div>
    </div>
  </nav>

  <main>
    <RouterView />
  </main>
</template>

<style scoped>
main {
  height: calc(100vh - 56px);
  width: 100vw;
  overflow-y: auto;
}
</style>
