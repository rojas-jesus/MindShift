<script setup lang="ts">
import { RouterLink, RouterView, useRouter } from 'vue-router'
import { ref, onMounted, onUnmounted, computed, watch } from 'vue'
import { authService } from './services/auth'
import { HugeiconsIcon } from '@hugeicons/vue'
import { UserCircleIcon, Settings01Icon, Logout01Icon } from '@hugeicons/core-free-icons'

const router = useRouter()
const user = ref<any>(null)
const isDropdownOpen = ref(false)

const isAuthenticated = computed(() => {
  const _route = router.currentRoute.value
  return !!localStorage.getItem('access_token')
})

const displayUsername = computed(() => {
  if (user.value?.username) return user.value.username
  const stored = authService.getStoredUser()
  if (stored?.username) return stored.username
  return 'User'
})

const fetchUserProfile = async () => {
  if (!isAuthenticated.value) {
    user.value = null
    return
  }

  // Load from storage immediately
  const stored = authService.getStoredUser()
  if (stored) {
    user.value = stored
  }

  try {
    console.log('Fetching user profile...')
    const response = await authService.getCurrentUser()
    console.log('Profile response:', response.data)
    user.value = response.data
    localStorage.setItem('user_info', JSON.stringify(response.data))
  } catch (error: any) {
    console.error('Profile fetch failed:', error.response?.status, error.message)
    // If unauthorized, we might need to logout
    if (error.response?.status === 401) {
      // Don't auto-logout here to avoid loops, but keep null user
      user.value = null
    }
  }
}

// Watch for auth changes and route changes
watch([isAuthenticated, () => router.currentRoute.value.path], () => {
  fetchUserProfile()
}, { immediate: true })

// Fallback interval to sync if storage changes outside Vue
let syncInterval: any = null

const toggleDropdown = () => {
  isDropdownOpen.value = !isDropdownOpen.value
}

const handleOutsideClick = (event: MouseEvent) => {
  const container = document.querySelector('.profile-dropdown-container')
  if (container && !container.contains(event.target as Node)) {
    isDropdownOpen.value = false
  }
}

onMounted(() => {
  fetchUserProfile()
  window.addEventListener('click', handleOutsideClick)
  
  // Listen for storage changes (e.g. from logout/login in other contexts)
  window.addEventListener('storage', (e) => {
    if (e.key === 'access_token' || e.key === 'user_info') {
      fetchUserProfile()
    }
  })
  
  // Refresh user object from storage every 2 seconds as fallback
  syncInterval = setInterval(() => {
    if (isAuthenticated.value && !user.value) {
      const stored = authService.getStoredUser()
      if (stored) user.value = stored
    }
  }, 2000)
})

onUnmounted(() => {
  window.removeEventListener('click', handleOutsideClick)
  window.removeEventListener('storage', fetchUserProfile) // cleaned up
  if (syncInterval) clearInterval(syncInterval)
})

const logout = () => {
  authService.logout()
  user.value = null
  isDropdownOpen.value = false
  router.push('/login')
}
</script>

<template>
  <header class="top-nav">
    <div class="container-fluid">
      <div class="row align-items-center">
        <!-- Logo and Brand -->
        <div class="col-md-3">
          <div class="d-flex align-items-center">
            <h4 class="text-white mb-0 me-4">MindShift</h4>
          </div>
        </div>
        
        <!-- Navigation Links -->
        <div class="col-md-6">
          <nav class="nav justify-content-center">
            <RouterLink class="nav-link" to="/">Home</RouterLink>
            <RouterLink class="nav-link" to="/about">About</RouterLink>
            
            <template v-if="isAuthenticated">
              <RouterLink class="nav-link" to="/dashboard">Dashboard</RouterLink>
              <a href="#" class="nav-link logout-btn" @click.prevent="logout">Logout</a>
            </template>
            
            <template v-else>
              <RouterLink class="nav-link" to="/login">Login</RouterLink>
              <RouterLink class="nav-link" to="/register">Register</RouterLink>
            </template>
          </nav>
        </div>
        
        <!-- User Actions -->
        <div class="col-md-3 text-end" v-if="isAuthenticated">
          <div class="d-inline-flex align-items-center position-relative">
            <span class="me-3 text-white fw-bold">{{ displayUsername }}</span>
            <div class="profile-dropdown-container">
              <button class="btn btn-outline-light rounded-circle profile-btn" type="button" @click="toggleDropdown">
                <HugeiconsIcon :icon="UserCircleIcon" size="24" />
              </button>
              
              <div v-if="isDropdownOpen" class="profile-menu shadow" @click.stop>
                <div class="menu-header">
                  <div class="fw-bold">{{ displayUsername }}</div>
                  <small class="text-muted">{{ user?.email }}</small>
                </div>
                <div class="dropdown-divider"></div>
                <button class="menu-item" @click="router.push('/dashboard'); isDropdownOpen = false">
                  <HugeiconsIcon :icon="UserCircleIcon" size="18" class="me-2" />
                  Profile
                </button>
                <button class="menu-item" @click="isDropdownOpen = false">
                  <HugeiconsIcon :icon="Settings01Icon" size="18" class="me-2" />
                  Settings
                </button>
                <div class="dropdown-divider"></div>
                <button class="menu-item logout-item" @click="logout">
                  <HugeiconsIcon :icon="Logout01Icon" size="18" class="me-2" />
                  Logout
                </button>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </header>

  <main>
    <RouterView />
  </main>
</template>

<style scoped>
.top-nav {
  background: linear-gradient(135deg, #6A0DAD, #8A2BE2);
  box-shadow: 0 2px 15px rgba(0,0,0,0.1);
  z-index: 1000;
  padding: 1rem 0;
}

.top-nav .nav-link {
  color: rgba(255,255,255,0.8);
  border-radius: 15px;
  padding: 8px 16px;
  margin: 0 4px;
  transition: all 0.3s ease;
  display: flex;
  align-items: center;
  font-size: 0.9rem;
  text-decoration: none;
}

.top-nav .nav-link:hover,
.top-nav .nav-link.active,
.top-nav .router-link-active {
  background-color: rgba(255,255,255,0.2);
  color: white;
  transform: translateY(-2px);
  text-decoration: none;
}

.top-nav .nav-link.logout-btn {
  background-color: #dc3545;
  color: white;
}

.top-nav .nav-link.logout-btn:hover {
  background-color: #c82333;
}

.profile-dropdown-container {
  position: relative;
}

.profile-btn {
  width: 40px;
  height: 40px;
  padding: 0;
  display: flex;
  align-items: center;
  justify-content: center;
  border: 2px solid rgba(255,255,255,0.5);
  transition: all 0.3s ease;
}

.profile-btn:hover {
  background-color: rgba(255,255,255,0.2);
  border-color: white;
}

.profile-menu {
  position: absolute;
  top: calc(100% + 10px);
  right: 0;
  background: white;
  border-radius: 12px;
  width: 200px;
  padding: 8px 0;
  z-index: 2000;
  transform-origin: top right;
  animation: slideIn 0.2s ease;
}

@keyframes slideIn {
  from { opacity: 0; transform: translateY(-10px) scale(0.95); }
  to { opacity: 1; transform: translateY(0) scale(1); }
}

.menu-header {
  padding: 12px 16px;
}

.menu-item {
  width: 100%;
  padding: 10px 16px;
  border: none;
  background: none;
  text-align: left;
  display: flex;
  align-items: center;
  font-size: 0.9rem;
  color: #2C3E50;
  transition: background 0.2s ease;
}

.menu-item:hover {
  background-color: #f8f9fa;
  color: #6A0DAD;
}

.logout-item:hover {
  background-color: #fff5f5;
  color: #dc3545;
}

.dropdown-divider {
  height: 1px;
  background-color: #eee;
  margin: 4px 0;
}

main {
  min-height: calc(100vh - 80px); /* 80px is approx height of nav */
  width: 100vw;
  overflow-y: auto;
  background-color: #f8f9fa; /* Match dashboard background */
}

</style>
