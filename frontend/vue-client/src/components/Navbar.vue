<script setup lang="ts">
import { ref } from 'vue'
import { HugeiconsIcon } from '@hugeicons/vue'
import { 
  Menu01Icon,
  Mail01Icon as MessageIcon,
  InformationCircleIcon as HelpIcon,
  Notification01Icon,
  UserCircleIcon,
  Logout01Icon,
  Settings01Icon
} from '@hugeicons/core-free-icons'
import { authService } from '../services/auth'
import { useRouter } from 'vue-router'

const props = defineProps<{
  userProfile: any
}>()

const emit = defineEmits(['toggleSidebar'])

const router = useRouter()
const isDropdownOpen = ref(false)

const toggleDropdown = () => {
  isDropdownOpen.value = !isDropdownOpen.value
}

const logout = () => {
  authService.logout()
  router.push('/login')
}
</script>

<template>
  <nav class="navbar">
    <div class="left-section">
      <button class="icon-btn sidebar-toggle" @click="emit('toggleSidebar')">
        <HugeiconsIcon :icon="Menu01Icon" size="24" />
      </button>
      <div class="brand-container d-md-none">
        <div class="logo-icon small">M</div>
        <span class="logo-text small">MindShift</span>
      </div>
    </div>

    <div class="right-section">
      <div class="action-icons">
        <button class="icon-btn" title="Mensajes">
          <HugeiconsIcon :icon="MessageIcon" size="22" />
        </button>
        <button class="icon-btn" title="Ayuda">
          <HugeiconsIcon :icon="HelpIcon" size="22" />
        </button>
        <button class="icon-btn" title="Notificaciones">
          <HugeiconsIcon :icon="Notification01Icon" size="22" />
          <span class="badge"></span>
        </button>
      </div>

      <div class="user-profile" v-if="userProfile">
        <div class="profile-trigger" @click="toggleDropdown">
          <img 
            v-if="userProfile.profile_picture" 
            :src="userProfile.profile_picture" 
            class="avatar" 
          />
          <HugeiconsIcon v-else :icon="UserCircleIcon" size="40" class="avatar-placeholder" />
        </div>

        <div v-if="isDropdownOpen" class="profile-dropdown shadow animate-blur">
          <div class="dropdown-header">
            <div class="user-info">
              <span class="user-name">{{ userProfile.username || 'User' }}</span>
              <span class="user-email">{{ userProfile.email }}</span>
            </div>
          </div>
          <div class="dropdown-divider"></div>
          <button class="dropdown-item" @click="router.push('/profile'); isDropdownOpen = false">
            <HugeiconsIcon :icon="UserCircleIcon" size="18" />
            <span>Profile</span>
          </button>
          <button class="dropdown-item" @click="isDropdownOpen = false">
            <HugeiconsIcon :icon="Settings01Icon" size="18" />
            <span>Settings</span>
          </button>
          <div class="dropdown-divider"></div>
          <button class="dropdown-item logout" @click="logout">
            <HugeiconsIcon :icon="Logout01Icon" size="18" />
            <span>Logout</span>
          </button>
        </div>
      </div>
    </div>
  </nav>
</template>

<style scoped>
.navbar {
  height: 80px;
  background: white;
  border-bottom: 1px solid #edf2f7;
  display: flex;
  align-items: center;
  justify-content: space-between;
  padding: 0 24px;
  position: sticky;
  top: 0;
  z-index: 1000;
}

.left-section {
  display: flex;
  align-items: center;
  gap: 20px;
}

.icon-btn {
  background: transparent;
  border: none;
  padding: 8px;
  border-radius: 10px;
  color: #4a5568;
  cursor: pointer;
  display: flex;
  align-items: center;
  justify-content: center;
  transition: all 0.2s ease;
  position: relative;
}

.icon-btn:hover {
  background: #f7fafc;
  color: #2d3748;
}

.badge {
  position: absolute;
  top: 8px;
  right: 8px;
  width: 8px;
  height: 8px;
  background: #f56565;
  border: 2px solid white;
  border-radius: 50%;
}

.right-section {
  display: flex;
  align-items: center;
  gap: 24px;
}

.action-icons {
  display: flex;
  align-items: center;
  gap: 12px;
}

.user-profile {
  position: relative;
}

.profile-trigger {
  cursor: pointer;
  display: flex;
  align-items: center;
}

.avatar {
  width: 40px;
  height: 40px;
  border-radius: 12px;
  object-fit: cover;
}

.avatar-placeholder {
  color: #cbd5e0;
}

.profile-dropdown {
  position: absolute;
  top: calc(100% + 12px);
  right: 0;
  width: 220px;
  background: white;
  border-radius: 16px;
  padding: 8px;
  z-index: 1002;
}

.dropdown-header {
  padding: 12px 16px;
}

.user-info {
  display: flex;
  flex-direction: column;
}

.user-name {
  font-weight: 700;
  font-size: 0.95rem;
  color: #1a202c;
}

.user-email {
  font-size: 0.8rem;
  color: #a0aec0;
}

.dropdown-divider {
  height: 1px;
  background: #edf2f7;
  margin: 8px 0;
}

.dropdown-item {
  width: 100%;
  display: flex;
  align-items: center;
  gap: 12px;
  padding: 10px 16px;
  border: none;
  background: transparent;
  font-size: 0.9rem;
  font-weight: 500;
  color: #4a5568;
  border-radius: 10px;
  cursor: pointer;
  transition: all 0.2s;
}

.dropdown-item:hover {
  background: #f7fafc;
  color: #2d3748;
}

.dropdown-item.logout {
  color: #f56565;
}

.dropdown-item.logout:hover {
  background: #fff5f5;
}

.animate-blur {
  animation: fadeInBlur 0.3s ease;
}

@keyframes fadeInBlur {
  from { opacity: 0; transform: translateY(-10px); filter: blur(4px); }
  to { opacity: 1; transform: translateY(0); filter: blur(0); }
}

.brand-container {
  display: flex;
  align-items: center;
  gap: 8px;
}

.logo-icon.small {
  width: 24px;
  height: 24px;
  font-size: 0.8rem;
  border-radius: 6px;
  background: linear-gradient(135deg, #f15a24, #d4145a);
  color: white;
  display: flex;
  align-items: center;
  justify-content: center;
  font-weight: bold;
}

.logo-text.small {
  font-size: 1rem;
  font-weight: 700;
  color: #1a202c;
}
</style>
