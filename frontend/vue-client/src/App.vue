<script setup lang="ts">
import { RouterView, useRouter } from 'vue-router'
import { ref, onMounted, onUnmounted, computed, watch } from 'vue'
import { authService } from './services/auth'
import Sidebar from './components/Sidebar.vue'
import Navbar from './components/Navbar.vue'

const router = useRouter()
const user = ref<any>(null)
const isSidebarCollapsed = ref(false)

const isAuthenticated = computed(() => {
  return !!localStorage.getItem('access_token')
})

const isAuthPage = computed(() => {
  const path = router.currentRoute.value.path
  return path === '/login' || path === '/register'
})

const fetchUserProfile = async () => {
  if (!isAuthenticated.value) {
    user.value = null
    return
  }

  const stored = authService.getStoredUser()
  if (stored) {
    user.value = stored
  }

  try {
    const response = await authService.getCurrentUser()
    user.value = response.data
    localStorage.setItem('user_info', JSON.stringify(response.data))
  } catch (error: any) {
    console.error('Profile fetch failed:', error.response?.status, error.message)
    if (error.response?.status === 401) {
      user.value = null
    }
  }
}

watch([isAuthenticated, () => router.currentRoute.value.path], () => {
  fetchUserProfile()
}, { immediate: true })

const toggleSidebar = () => {
  isSidebarCollapsed.value = !isSidebarCollapsed.value
}

onMounted(() => {
  fetchUserProfile()
  window.addEventListener('storage', (e) => {
    if (e.key === 'access_token' || e.key === 'user_info') {
      fetchUserProfile()
    }
  })
})
</script>

<template>
  <div class="app-container" :class="{ 'no-sidebar': !isAuthenticated || isAuthPage }">
    <!-- Sidebar only for authenticated users and not on login/register -->
    <Sidebar 
      v-if="isAuthenticated && !isAuthPage" 
      :is-collapsed="isSidebarCollapsed" 
    />

    <div class="main-wrapper" :class="{ 'sidebar-collapsed': isSidebarCollapsed }">
      <!-- Navbar only for authenticated users and not on login/register -->
      <Navbar 
        v-if="isAuthenticated && !isAuthPage" 
        :user-profile="user"
        @toggle-sidebar="toggleSidebar"
      />

      <!-- Fallback Header for Guest users -->
      <header v-if="!isAuthenticated && !isAuthPage" class="guest-nav">
        <div class="container d-flex justify-content-between align-items-center py-3">
          <h4 class="mb-0 fw-bold">MindShift</h4>
          <nav class="d-flex gap-3">
            <RouterLink to="/">Home</RouterLink>
            <RouterLink to="/about">About</RouterLink>
            <RouterLink to="/login" class="btn btn-primary btn-sm rounded-pill px-4">Login</RouterLink>
          </nav>
        </div>
      </header>

      <main :class="{ 'p-0': isAuthPage }">
        <RouterView />
      </main>
    </div>
  </div>
</template>

<style>
/* Global Styles */
:root {
  --sidebar-width: 260px;
  --sidebar-collapsed-width: 80px;
  --navbar-height: 80px;
}

body {
  margin: 0;
  padding: 0;
  font-family: 'Inter', system-ui, -apple-system, sans-serif;
  background-color: #f8fafc;
}

.app-container {
  display: flex;
  min-height: 100vh;
}

.main-wrapper {
  flex: 1;
  display: flex;
  flex-direction: column;
  margin-left: var(--sidebar-width);
  transition: margin-left 0.3s ease;
  min-width: 0;
}

.main-wrapper.sidebar-collapsed {
  margin-left: var(--sidebar-collapsed-width);
}

.app-container.no-sidebar .main-wrapper {
  margin-left: 0;
}

main {
  flex: 1;
  padding: 24px;
}

/* Guest Nav Styles */
.guest-nav {
  background: white;
  border-bottom: 1px solid #edf2f7;
}

.guest-nav a {
  text-decoration: none;
  color: #4a5568;
  font-weight: 500;
}

.guest-nav a:hover {
  color: #1a202c;
}

.guest-nav .btn-primary {
  color: white !important;
}

/* Auth Pages specific adjustment */
.p-0 {
  padding: 0 !important;
}
</style>
